
from fastapi import Request, Response
from sqlalchemy.orm import Session

from src.schemas.auth import LoginRequest
from src.schemas.api_response import SuccessResponse
import src.services.login as services


def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session
):
    
    token_data = services.login(
        payload.email,
        payload.password,
        db
    )
    
    return SuccessResponse(
		status_code=200,
		message="User logged in. Verify OTP from mail.",
		data={
			"user": token_data
		}
	)
