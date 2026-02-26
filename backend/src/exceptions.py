from enum import Enum
from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class ErrorCode(Enum):
	CONFLICT_ERROR = "CONFLICT_ERROR"
	VALIDATION_ERROR = "VALIDATION_ERROR"
	AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
	NOT_FOUND_ERROR = "NOT_FOUND_ERROR"
	INVALID_REFRESH_TOKEN_ERROR = "INVALID_REFRESH_TOKEN_ERROR"
	INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"


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
		error_code: ErrorCode, 
		message: str,
		details: ErrorDetail
	):
		self.status_code = status_code
		self.error_code = error_code
		self.message = message
		self.details = details
		super().__init__(message)
		

def register_exception_handlers(app: FastAPI):
	@app.exception_handler(DomainException)
	def domain_exception_handler(
		request: Request,
		exc: DomainException
	):
		return JSONResponse(
			status_code=exc.status_code,
			content={
				"success": False,
				"error": {
					"code": exc.error_code.value,
					"message": exc.message,
					"details": exc.details.model_dump(mode="json")
				}
			}
		)
