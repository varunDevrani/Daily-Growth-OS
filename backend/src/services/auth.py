from http import HTTPStatus
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.exceptions import DomainException
from src.models.refresh_token import RefreshToken
from src.models.user import User
from src.schemas.auth import LoginRequest, RefreshTokenRequest, SignupRequest, TokenResponse
from src.schemas.user import UserResponse
from src.utils.hashing import hash_password, verify_password
from src.utils.jwt_handler import JWTToken, create_token, decode_token


def create_auth_tokens(
	user_id: UUID,
	db: Session
) -> TokenResponse:
	_, access_token = create_token(user_id, JWTToken.ACCESS_TOKEN)
	refresh_token_payload, refresh_token = create_token(user_id, JWTToken.REFRESH_TOKEN)

	refresh_token_data = RefreshToken(
		user_id=user_id,
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
) -> UserResponse:
	
	stmt = select(RefreshToken).where(RefreshToken.token == payload.refresh_token)
	token_data = db.scalar(stmt)
	if token_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="refresh token not found"
		)
	
	refresh_token_payload = decode_token(payload.refresh_token)
	if refresh_token_payload is None or refresh_token_payload.token_type != JWTToken.REFRESH_TOKEN:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid refresh token",
		)
	
	stmt = select(User).where(User.id == token_data.user_id)
	user_data = db.scalar(stmt)
	if user_data is None:
		raise DomainException(
			status_code=HTTPStatus.NOT_FOUND,
			message="User not found"
		)

	db.delete(token_data)
	db.flush()

	return UserResponse.model_validate(user_data)


def refresh(
	payload: RefreshTokenRequest,
	db: Session
) -> TokenResponse:
	user_id = logout(payload, db).id
		
	return create_auth_tokens(user_id, db)
	
