from pydantic import BaseModel, EmailStr, field_validator

class SignupRequest(BaseModel):
    
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    @classmethod
    def check_password_match(cls, confirm_password, info):
        if confirm_password != info.data.get("password"):
            raise ValueError("Passwords do not match")
        return confirm_password


class LoginRequest(BaseModel):
    email: EmailStr
    password: str