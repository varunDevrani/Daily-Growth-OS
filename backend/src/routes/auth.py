from src.schemas.auth import SignupRequest, LoginRequest
from src.controllers.auth_controllers import signup_controller
from src.database.database import get_db
from fastapi import APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session

from src.schemas.auth import SignupRequest, LoginRequest
import src.controllers.login as controllers

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(request: SignupRequest, db: Session = Depends(get_db)):
    return signup_controller(request, db)


@router.post("/login")
def login(
    request: Request,
    response: Response,
    payload: LoginRequest,
    db: Session
):
    return controllers.login(
        request,
        response,
        payload,
        db
    )
