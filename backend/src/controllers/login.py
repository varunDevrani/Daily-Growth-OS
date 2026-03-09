
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.schemas.auth import LoginRequest
import src.services.login as services

#FixFix: request and response are not getting used.
def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session
):
    
    service_data = services.login(
        payload.email,
        payload.password,
        db
    )

    if service_data == services.LoginErrors.EMAIL_NOT_FOUND:
        return {
            "message": "email not found",
            "success": False,
            #FixFix:  The status_code in the response body has no effect. FastAPI will return HTTP 200.
            "status_code": 404,
        }
    
    if service_data == services.LoginErrors.PASSWORD_MISMATCH:
        return {
            "message": "password mismatch",
            "success": False,
            "status_code": 401,
        }
    #FixFix: why success is false on login?
    return {
        "message": "user logged in",
        "success": False,
        "status_code": 200,
        "data": service_data.model_dump(mode="json")
    }