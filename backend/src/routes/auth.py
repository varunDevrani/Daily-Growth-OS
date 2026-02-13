from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.auth import SignupRequest, LoginRequest
from src.controllers.auth_controllers import signup_controller
from src.database.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    return signup_controller(request, db)


@router.post("/login")
def login(payload: LoginRequest):
    pass