from pydantic import BaseModel, EmailStr, field_validator, ConfigDict

class SignupRequest(BaseModel):
	model_config = ConfigDict(extra="forbid")
    
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
	model_config = ConfigDict(extra="forbid")
	
	email: EmailStr
	password: str
    
class LoginResponse(BaseModel):
	token_type: str
	access_token: str
	refresh_token: str

