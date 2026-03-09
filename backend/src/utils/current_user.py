from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.utils.jwt_handler import verify_access_token

security = HTTPBearer(auto_error=False)

#FixFix: fck man, Utils raising HTTPException
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> int:
    
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
	#FixFix: why returing it as int?
	return user_id
