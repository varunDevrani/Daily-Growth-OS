from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from uuid import UUID

from src.database.database import get_db
from src.schemas.setting import SettingsUpdateRequest
from src.utils.current_user import get_current_user
import src.controllers.setting as controllers


router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("")
def get_settings(
    request: Request,
    response: Response,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.get_settings(
		request,
		response,
		db,
		user_id
	)


@router.patch("")
def update_settings(
    request: Request,
    response: Response,
    payload: SettingsUpdateRequest,
    db: Session = Depends(get_db),
    user_id: UUID = Depends(get_current_user)
) -> JSONResponse:
	return controllers.update_settings(
		request,
		response,
		payload,
		db,
		user_id
	)


