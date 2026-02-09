from fastapi import APIRouter
from src.schemas.auth import SignupRequest, LoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(payload: SignupRequest):
    pass

@router.post("/login")
def login(payload: LoginRequest):
    pass
