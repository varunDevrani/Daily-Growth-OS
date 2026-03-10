from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import src.controllers.auth as controllers
from src.dependencies.database import get_db
from src.schemas.api_response import SuccessResponse
from src.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from src.schemas.user import UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/signup",
    status_code=HTTPStatus.CREATED,
    response_model=SuccessResponse[UserResponse],
)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    return controllers.signup(payload, db)


@router.post(
    "/login", status_code=HTTPStatus.OK, response_model=SuccessResponse[TokenResponse]
)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return controllers.login(payload, db)
