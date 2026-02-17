
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.schemas.auth import LoginRequest
import src.services.login as services


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
            "status_code": 404,
        }
    
    if service_data == services.LoginErrors.PASSWORD_MISMATCH:
        return {
            "message": "password mismatch",
            "success": False,
            "status_code": 401,
        }
    
    return {
        "message": "user logged in",
        "success": False,
        "status_code": 200,
        "data": {
            "access_token": service_data[0],
            "refresh_token": service_data[1],
            "type": "bearer"
        }
    }