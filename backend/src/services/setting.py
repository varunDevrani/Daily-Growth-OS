from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.setting import Setting
from src.schemas.setting import SettingsUpdateRequest



def get_settings(
	user_id: UUID,
	db: Session
) -> Setting:
		
	stmt = select(Setting).where(Setting.user_id == user_id)
	setting_data = db.scalar(stmt)
	if setting_data is None:
		raise HTTPException(
			status_code=404,
			detail="settings not found"
		)
		
	return setting_data
	


def update_settings(
	payload: SettingsUpdateRequest,
	user_id: UUID,
	db: Session
) -> Setting:
	
	stmt = select(Setting).where(Setting.user_id == user_id)
	setting_data = db.scalar(stmt)

	if not setting_data:
		raise HTTPException(
			status_code=404,
			detail="settings[user_id] not found"
		)
		
	updated_payload = payload.model_dump(exclude_unset=True, exclude_none=True)
	for key, value in updated_payload.items():
		setattr(setting_data, key, value)
		
	db.commit()
	db.refresh(setting_data)		
		
	return setting_data

