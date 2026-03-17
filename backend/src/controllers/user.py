from sqlalchemy.orm import Session
from fastapi import UploadFile
from src.models.user import User
from src.schemas.api_response import SuccessResponse
from src.schemas.user import UserProfileResponse
import src.services.user as services
from uuid import UUID

def update_profile_picture(
    file: UploadFile,
    user: User,  
    db: Session
) -> SuccessResponse[UserProfileResponse]:

    user_data = services.update_profile_picture(
        file,
        user,
        db
    )

    return SuccessResponse[UserProfileResponse](
        message="profile picture updated successfully",
        data=user_data
    )