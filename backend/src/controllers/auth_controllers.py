from sqlalchemy.orm import Session
from src.schemas.auth import SignupRequest
from src.services.signup import signup_user

def signup_controller(request: SignupRequest, db: Session):
    user = signup_user(
        db=db,
        email=request.email,
        password=request.password
    )

    return {
        "message": "Signup successful",
        "user_id": user.id,
        "email": user.email
    }