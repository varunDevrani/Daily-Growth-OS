from http import HTTPStatus
from typing import List, Union
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class FieldViolation(BaseModel):
	field: str
	message: Union[str, None] = None


class DomainException(Exception):
	def __init__(
		self,
		status_code: int,
		message: str = "Request Failed",
		field_violations: List[FieldViolation] = []
	):
		self.status_code = status_code
		self.message = message
		self.field_violations = field_violations
		super().__init__(message)


def register_exception_handlers(app: FastAPI):
	@app.exception_handler(DomainException)
	def domain_exception_handler(
		request: Request,
		exc: DomainException
	) -> JSONResponse:
		
		segments = [value for value in request.url.path.split("/") if value and not value.isdigit()]
		resource = segments[-1] if segments else "unknown"
		
		return JSONResponse(
			status_code=exc.status_code,
			content={
				"success": False,
				"message": exc.message,
				"errors": {
					"resource": resource,
					"field_violations": [violation.model_dump(mode="json") for violation in exc.field_violations]
				}
			}
		)
	
	
	@app.exception_handler(RequestValidationError)
	def request_validation_exception_handler(
		request: Request,
		exc: RequestValidationError
	) -> JSONResponse:
		
		segments = [value for value in request.url.path.split("/") if value and not value.isdigit()]
		resource = segments[-1] if segments else "unknown"
		
		field_violations: List[FieldViolation] = []
		for error in exc.errors():
			loc = error.get("loc", [])
			field_path = ".".join([str(value) for value in loc if value != "body"])
			field_violations.append(
				FieldViolation(
					field=field_path,
					message=error.get("msg", "Something went wrong")
				)
			)
		
		return JSONResponse(
			status_code=HTTPStatus.UNPROCESSABLE_CONTENT,
			content={
				"success": False,
				"message": HTTPStatus.UNPROCESSABLE_CONTENT.phrase,
				"errors": {
					"resource": resource,
					"field_violations": [violation.model_dump(mode="json") for violation in field_violations]
				}
			}
		)


