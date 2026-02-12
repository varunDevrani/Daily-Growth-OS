from fastapi import APIRouter, Request, Response
from fastapi import Depends
from sqlalchemy.orm import Session

from src.schemas.auth import SignupRequest, LoginRequest
from src.services.login import login_service
from src.database.database import get_db


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(payload: SignupRequest):
    pass

@router.post("/login")
def login(request: Request, response: Response, payload: LoginRequest, db: Session = Depends(get_db)):
    return login_service(request, response, payload, db)
