import os
from uuid import UUID
from fastapi import UploadFile
from sqlalchemy import UUID
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserProfileResponse

UPLOAD_DIR = "uploads/profile_pictures"


def update_profile_picture(
    file: UploadFile,
    user: User,
    db: Session
) -> UserProfileResponse:

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = f"{UPLOAD_DIR}/{user.id}_{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    user.profile_pic_url = file_path

    db.flush()
    db.refresh(user)

    return UserProfileResponse.model_validate(user)