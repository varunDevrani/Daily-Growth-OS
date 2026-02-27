from sqlalchemy.orm import Session

from src.exceptions import DomainException, ErrorCode, ErrorDetail
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
            ErrorCode.NOT_FOUND_ERROR,
            "User does not exist",
            ErrorDetail(resource="users"),
        )

    if not verify_password(password, str(user_data.password_hash)):
        raise DomainException(
            401,
            ErrorCode.AUTHENTICATION_ERROR,
            "Invalid Credentials",
            ErrorDetail(resource="users"),
        )

    refresh_token_data = (
        db.query(RefreshTokenModel)
        .filter(RefreshTokenModel.user_id == user_data.id)
        .first()
    )
    if refresh_token_data is not None:
        raise DomainException(
            409,
            ErrorCode.CONFLICT_ERROR,
            "User is already logged in",
            ErrorDetail(resource="users"),
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
