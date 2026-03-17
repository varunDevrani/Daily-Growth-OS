from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

import src.controllers.user as controllers
from src.dependencies.database import get_db
from src.dependencies.auth import get_current_user
from src.models.user import User
from src.schemas.api_response import SuccessResponse
from src.schemas.user import UserProfileResponse
from src.dependencies.user import get_user_or_404

router = APIRouter(prefix="/users", tags=["users"])


@router.patch(
    "/profile-picture",
    status_code=HTTPStatus.OK,
    response_model=SuccessResponse[UserProfileResponse]
)
def update_profile_picture(
    file: UploadFile = File(...),
    user: User = Depends(get_user_or_404),
    db: Session = Depends(get_db)
):
    return controllers.update_profile_picture(
        file,
        user,
        db
    )