from fastapi import APIRouter, Request, Response
from sqlalchemy.orm import Session

from src.schemas.auth import SignupRequest, LoginRequest
import src.controllers.login as controllers

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(payload: SignupRequest):
    pass

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
