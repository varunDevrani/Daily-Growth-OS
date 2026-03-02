from sqlalchemy.orm import Session
from datetime import datetime, timezone

from src.exceptions import DomainException, FieldViolation
from src.models.refresh_token import RefreshToken as RefreshTokenModel
from src.models.user import User as UserModel
from src.schemas.auth import LoginResponse
from src.utils.hashing import verify_password
from src.utils.jwt_handler import create_access_token, create_refresh_token


def login(email: str, password: str, db: Session) -> LoginResponse:
    user_data = db.query(UserModel).filter(UserModel.email == email).first()

    if user_data is None:
        raise DomainException(
            404,
            "User does not exist"
        )

    if not verify_password(password, str(user_data.password_hash)):
        raise DomainException(
            401,
            "Invalid Credentials",
            [FieldViolation(
            	field="password",
             	message="password doesnt match"
            )]
        )

    refresh_token_data = (
        db.query(RefreshTokenModel)
        .filter(RefreshTokenModel.user_id == user_data.id)
        .first()
    )
    if refresh_token_data is not None and refresh_token_data.expires_at > datetime.now(timezone.utc):
        raise DomainException(
            409,
            "User is already logged in",
        )

    access_token = create_access_token(user_data.id)
    token_payload, refresh_token = create_refresh_token(user_data.id)

    refresh_token_data = RefreshTokenModel(
        user_id=user_data.id,
        token=refresh_token,
        issued_at=token_payload["iat"],
        expires_at=token_payload["exp"],
    )

    db.add(refresh_token_data)
    db.commit()
    db.refresh(refresh_token_data)

    return LoginResponse(
		token_type= "bearer",
		access_token=access_token,
		refresh_token=refresh_token
    )
