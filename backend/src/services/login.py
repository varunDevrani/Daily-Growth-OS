
from enum import Enum
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User as UserModel
from src.models.refresh_token import RefreshToken as RefreshTokenModel
from src.utils.hashing import verify_password
from src.utils.jwt_handler import create_access_token, create_refresh_token


class LoginErrors(Enum):
    EMAIL_NOT_FOUND = 0
    PASSWORD_MISMATCH = 1


def login(
    email: str,
    password: str,
    db: Session
):
    # stmt = select(UserModel).where(UserModel.email == email)
    # user_data = db.execute(stmt).scalar_one_or_none()

    user_data = db.query(UserModel).filter(UserModel.email == email).first()

    if user_data is None:
        return LoginErrors.EMAIL_NOT_FOUND
    
    if verify_password(password, user_data.password_hash) == False:
        return LoginErrors.PASSWORD_MISMATCH

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

    return (access_token, refresh_token)