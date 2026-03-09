from pydantic import BaseModel, EmailStr

#FixFix: No password strength validation (length, complexity)
#FixFix: No response schemas defined (SignupResponse, LoginResponse)
class SignupRequest(BaseModel):
    
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str