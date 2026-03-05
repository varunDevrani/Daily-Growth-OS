from http import HTTPStatus
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from uuid import UUID

from src.utils.jwt_handler import verify_access_token
from src.exceptions import DomainException, FieldViolation

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UUID:
    
	if not credentials:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
			field_violations=[
				FieldViolation(
					field="token",
					message="token not present"
				)
			]
		)
    
	user_id = verify_access_token(credentials.credentials)
	
	if user_id is None:
		raise DomainException(
			status_code=HTTPStatus.UNAUTHORIZED,
			message="Invalid Credentials",
			field_violations=[
				FieldViolation(
					field="token",
					message="invalid token"
				)
			]
		)
	
	return user_id
