from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.exceptions import DomainException
from src.models.user import User
from src.schemas.auth import (
    LoginRequest,
    RefreshTokenRequest,
    SignupRequest,
    TokenResponse,
)
from src.schemas.user import UserResponse
from src.utils.hashing import hash_password, verify_password
from src.utils.token import consume_refresh_token, create_auth_tokens


def signup(
	payload: SignupRequest,
	db: Session,
) -> UserResponse:
	stmt = select(User).where(User.email == payload.email)
	user_data = db.scalar(stmt)
	if user_data is not None:
		raise DomainException(
			status_code=HTTPStatus.CONFLICT,
			message="user with email already exists",
		)

	user_data = User(
		email=payload.email,
		password_hash=hash_password(payload.password)
	)
	db.add(user_data)
	db.flush()
	db.refresh(user_data)

	return UserResponse.model_validate(user_data)


def login(
	payload: LoginRequest,
	db: Session
) -> TokenResponse:

	stmt = select(User).where(User.email == payload.email)
	user_data = db.scalar(stmt)

	if user_data is None or not verify_password(payload.password, user_data.password_hash):
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
		)

	return create_auth_tokens(user_data.id, db)


def logout(
	payload: RefreshTokenRequest,
	db: Session
) -> None:
	_ = consume_refresh_token(payload, db)


def refresh(
	payload: RefreshTokenRequest,
	db: Session
) -> TokenResponse:
	user_id = consume_refresh_token(payload, db)
	return create_auth_tokens(user_id, db)
