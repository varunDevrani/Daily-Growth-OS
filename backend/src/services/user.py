from datetime import datetime, timezone
from sqlalchemy.orm import Session

from src.models.user import User
from src.schemas.user import UserPartialUpdateRequest, UserResponse


def partial_update_user(
	payload: UserPartialUpdateRequest,
	user: User,
	db: Session
) -> UserResponse:
	updated_payload = payload.model_dump(exclude_none=True, exclude_unset=True)
	for key, value in updated_payload.items():
		setattr(user, key, value)

	db.flush()
	db.refresh(user)

	return UserResponse.model_validate(user)


def delete_user(
	user: User,
	db: Session
) -> None:
	user.deleted_at = datetime.now(timezone.utc)
