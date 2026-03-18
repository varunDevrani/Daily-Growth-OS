from http import HTTPStatus
from typing import Union
from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.exceptions import DomainException
from src.utils.jwt_handler import JWTToken, validate_token

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Union[HTTPAuthorizationCredentials, None] = Depends(security)
) -> UUID:

	if not credentials:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials"
		)

	return validate_token(credentials.credentials, JWTToken.ACCESS_TOKEN)
