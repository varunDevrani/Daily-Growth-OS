from sqlalchemy.orm import Session

import src.services.auth as services
from src.schemas.api_response import SuccessResponse
from src.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from src.schemas.user import UserResponse


def signup(
	payload: SignupRequest,
	db: Session
) -> SuccessResponse[UserResponse]:
    user_data = services.signup(
    	payload,
     	db
    )

    return SuccessResponse[UserResponse](
    	message="user created successfully",
     	data=user_data
    )


def login(
    payload: LoginRequest,
    db: Session
) -> SuccessResponse[TokenResponse]:
	token_data = services.login(
		payload,
		db
	)

	return SuccessResponse[TokenResponse](
		message="User logged in.",
		data=token_data
	)
