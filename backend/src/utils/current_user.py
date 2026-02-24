from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from uuid import UUID

from src.utils.jwt_handler import verify_access_token

security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> UUID:
    
	if not credentials:
		raise HTTPException(
			status_code=401,
			detail="not authenticated"
		)
    
	user_id = verify_access_token(credentials.credentials)
	
	if user_id is None:
		raise HTTPException(
			status_code=401,
			detail="invalid token"
		)
	
	return user_id
