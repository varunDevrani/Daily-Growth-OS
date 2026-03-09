from typing import Union
from pydantic import BaseModel, EmailStr

from src.schemas.base import BaseSchema

#FixFix: No password strength validation (length, complexity)
#FixFix: No response schemas defined (SignupResponse, LoginResponse)
class SignupRequest(BaseSchema):
    email: EmailStr
    password: str


class LoginRequest(BaseSchema):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
	token_type: str
	access_token: str
	refresh_token: Union[str, None] = None
    