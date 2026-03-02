from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class FieldViolation(BaseModel):
	field: str
	message: Union[str, None] = None

class ErrorDetail(BaseModel):
	resource: str
	field_violations: Union[List[FieldViolation], None] = None

class DomainException(Exception):
	def __init__(
		self, 
		status_code: int, 
		message: str,
		field_violations: Union[List[FieldViolation], None] = None
	):
		self.status_code = status_code
		self.message = message
		self.field_violations = field_violations
		super().__init__(message)
		
	
def map_status_code_to_error_code(status_code: int) -> str:
	mapping = {
		409: "CONFLICT_ERROR",
		422: "VALIDATION_ERROR",
		401: "AUTHENTICATION_ERROR",
		404: "NOT_FOUND_ERROR",
		403: "FORBIDDEN",
		500: "INTERNAL_SERVER_ERROR"
	}
	
	return mapping.get(status_code, "UNKNOWN_ERROR_CODE")


def register_exception_handlers(app: FastAPI):
	@app.exception_handler(DomainException)
	def domain_exception_handler(
		request: Request,
		exc: DomainException
	):
		
		segments = [value for value in request.url.path.split("/") if value and not value.isdigit()]
		resource = segments[-1] if segments else "unknown resource"
		
		return JSONResponse(
			status_code=exc.status_code,
			content={
				"success": False,
				"message": exc.message,
				"error": {
					"code": map_status_code_to_error_code(exc.status_code),
					"details": ErrorDetail(
						resource=resource,
						field_violations=exc.field_violations
					).model_dump(mode="json")
				}
			}
		)
	
	@app.exception_handler(RequestValidationError)
	def validation_exception_handler(
		request: Request,
		exc: RequestValidationError
	):
		
		field_violations = []
		for error in exc.errors():
			loc = error.get("loc", [])
			field_path = ".".join([str(value) for value in loc if value != "body"])
			field_violations.append(
				FieldViolation(
					field=field_path,
					message=error.get("msg", "something went wrong")
				)
			)
			
		segments = [value for value in request.url.path.split("/") if value and not value.isdigit()]
		resource = segments[-1] if segments else "unknown resource"
		
		return JSONResponse(
			status_code=422,
			content={
				"success": False,
				"message": "Request Validation Failed",
				"error": {
					"code": map_status_code_to_error_code(422),	
					"details": ErrorDetail(
						resource=resource,
						field_violations=field_violations
					).model_dump(mode="json")
				}
			}
		) 

