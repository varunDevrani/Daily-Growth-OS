import jwt
from datetime import datetime, timezone, timedelta
from typing import Dict, Optional, Tuple, Any
from uuid import UUID

import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "hello")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

ALGORITHM = "HS256"


def create_access_token(user_id: UUID) -> str:
	expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

	payload = {
		"user_id": str(user_id),
		"exp": expire,
		"iat": datetime.now(timezone.utc),
		"type": "access"
	}

	return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: UUID) -> Tuple[Dict[str, Any], str]:
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
		print("Token Expired")
		return None
	except jwt.InvalidTokenError:
		print("Invalid Token")
		return None
	

def verify_access_token(token: str) -> Optional[UUID]:
	payload = decode_token(token)
	if payload and payload["type"] == "access":
		return UUID(payload["user_id"])
	return None


def verify_refresh_token(token: str) -> Optional[UUID]:
	payload = decode_token(token)
	if payload and payload["type"] == "refresh":
		return UUID(payload["user_id"])
	return None