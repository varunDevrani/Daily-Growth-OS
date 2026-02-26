
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