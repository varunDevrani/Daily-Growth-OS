from datetime import datetime, timezone
from http import HTTPStatus

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.exceptions import DomainException
from src.models.refresh_token import RefreshToken
from src.models.user import User
from src.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from src.schemas.user import UserResponse
from src.utils.hashing import hash_password, verify_password
from src.utils.jwt_handler import JWTToken, create_token


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
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
		)

	if not verify_password(payload.password, user_data.password_hash):
		raise DomainException(
			status_code=401,
			message="Invalid Credentials",
		)

	stmt = select(RefreshToken).where(RefreshToken.user_id == user_data.id)
	refresh_token_data = db.scalar(stmt)
	if refresh_token_data is not None and refresh_token_data.expires_at > datetime.now(timezone.utc):
		raise DomainException(
			status_code=HTTPStatus.CONFLICT,
			message="User is already logged in"
		)

	_, access_token = create_token(user_data.id, JWTToken.ACCESS_TOKEN)
	refresh_token_payload, refresh_token = create_token(user_data.id, JWTToken.REFRESH_TOKEN)

	refresh_token_data = RefreshToken(
		user_id=user_data.id,
		token=refresh_token,
		issued_at=refresh_token_payload.iat,
		expires_at=refresh_token_payload.exp
	)

	db.add(refresh_token_data)
	db.flush()
	db.refresh(refresh_token_data)

	return TokenResponse(
		token_type="Bearer",
		access_token=access_token,
		refresh_token=refresh_token
	)
