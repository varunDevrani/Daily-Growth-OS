from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Tuple

import jwt

from src.core.config import settings


ALGORITHM = "HS256"


#FixFix: user_id is UUID I guess not int
def create_access_token(user_id: int) -> str:
	expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

	payload = {
		"user_id": str(user_id),
		"exp": expire,
		"iat": datetime.now(timezone.utc),
		"type": "access"
	}

	return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: int) -> Tuple[Dict[str, Any], str]:
	expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

	payload = {
		"user_id": str(user_id),
		"exp": expire,
		"iat": datetime.now(timezone.utc),
		"type": "refresh"
	}

	return (payload, jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=ALGORITHM))


def decode_token(token: str) -> Optional[Dict]:
	try:
		payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except jwt.ExpiredSignatureError:
		#FixFix: why we are using print() instead of logging?
		print("Token Expired")
		return None
	except jwt.InvalidTokenError:
		print("Invalid Token")
		return None


# FixFix: Duplicate verification code?
def verify_access_token(token: str) -> Optional[int]:
	payload = decode_token(token)
	if payload and payload["type"] == "access":
		#FixFix: why we are returing Int if model uses UUID?
		return int(payload["user_id"])
	return None


def verify_refresh_token(token: str) -> Optional[int]:
	payload = decode_token(token)
	if payload and payload["type"] == "refresh":
		return int(payload["user_id"])
	return None
