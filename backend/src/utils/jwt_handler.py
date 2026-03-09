import jwt
from datetime import datetime, timezone, timedelta
from typing import Dict, Optional, Tuple, Any

import os
from dotenv import load_dotenv

load_dotenv()

#FixFix: "hello" seriously?
JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "hello")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

ALGORITHM = "HS256"


#FixFix: user_id is UUID I guess not int
def create_access_token(user_id: int) -> str:
	expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

	payload = {
		"user_id": str(user_id),
		"exp": expire,
		"iat": datetime.now(timezone.utc),
		"type": "access"
	}

	return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: int) -> Tuple[Dict[str, Any], str]:
	expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

	payload = {
		"user_id": str(user_id),
		"exp": expire,
		"iat": datetime.now(timezone.utc),
		"type": "refresh"
	}

	return (payload, jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM))


def decode_token(token: str) -> Optional[Dict]:
	try:
		payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
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