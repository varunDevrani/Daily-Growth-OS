from http import HTTPStatus
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from src.exceptions import DomainException
from src.models.refresh_token import RefreshToken
from src.schemas.auth import RefreshTokenRequest, TokenResponse
from src.utils.jwt_handler import JWTToken, create_token, validate_token


def create_auth_tokens(user_id: UUID, db: Session) -> TokenResponse:
    _, access_token = create_token(user_id, JWTToken.ACCESS_TOKEN)
    refresh_token_payload, refresh_token = create_token(user_id, JWTToken.REFRESH_TOKEN)

    refresh_token_data = RefreshToken(
        user_id=user_id,
        token=refresh_token,
        issued_at=refresh_token_payload.iat,
        expires_at=refresh_token_payload.exp,
    )

    db.add(refresh_token_data)
    db.flush()

    return TokenResponse(
        token_type="Bearer", access_token=access_token, refresh_token=refresh_token
    )


def consume_refresh_token(payload: RefreshTokenRequest, db: Session) -> UUID:
    user_id = validate_token(payload.refresh_token, JWTToken.REFRESH_TOKEN)

    stmt = select(RefreshToken).where(RefreshToken.token == payload.refresh_token)
    token_data = db.scalar(stmt)
    if token_data is None:
        raise DomainException(
            status_code=HTTPStatus.NOT_FOUND,
            message="Refresh token not found",
        )

    db.delete(token_data)
    db.flush()

    return user_id
