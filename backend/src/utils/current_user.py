
from fastapi import Header
from typing import Optional

from src.utils.jwt_handler import verify_access_token


def get_current_user(authorization: str = Header(None)) -> Optional[int]:
    if not authorization:
        return None
    
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        return None
    
    token = parts[1]
    user_id = verify_access_token(token)
    if not user_id:
        return None
    
    return user_id