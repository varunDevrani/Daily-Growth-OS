from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import date
from http import HTTPStatus

from src.dependencies.database import get_db
from src.dependencies.auth import get_current_user

import src.controllers.morning as controllers

from src.schemas.morning import MorningCreate, MorningResponse, MorningUpdate
from src.schemas.morning_activity import MorningActivityCreate, MorningActivityResponse
from src.schemas.api_response import SuccessResponse

router = APIRouter(prefix="/morning", tags=["Morning"])


@router.post(
    "",
    status_code=HTTPStatus.CREATED,
    response_model=SuccessResponse[MorningResponse]
)
def create_morning(
    payload: MorningCreate,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
) -> SuccessResponse[MorningResponse]:
    return controllers.create_morning(payload, db, user_id)


@router.post(
    "/{checkin_id}/activities",
    status_code=HTTPStatus.CREATED,
    response_model=SuccessResponse[MorningActivityResponse]
)
def add_activity(
    checkin_id: UUID,
    payload: MorningActivityCreate,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
) -> SuccessResponse[MorningActivityResponse]:
    return controllers.add_activity(checkin_id, payload, db, user_id)


@router.patch(
    "/{checkin_id}",
    status_code=HTTPStatus.OK,
    response_model=SuccessResponse[MorningResponse]
)
def update_morning(
    checkin_id: UUID,
    payload: MorningUpdate,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
) -> SuccessResponse[MorningResponse]:
    return controllers.update_morning(checkin_id, payload, db, user_id)


@router.get(
    "/{target_date}",
    status_code=HTTPStatus.OK,
    response_model=SuccessResponse[MorningResponse]
)
def get_morning(
    target_date: date,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
) -> SuccessResponse[MorningResponse]:
    return controllers.get_morning(target_date, db, user_id)


@router.delete(
    "/{checkin_id}/activities/{activity_id}",
    status_code=HTTPStatus.OK,
    response_model=SuccessResponse
)
def delete_activity(
    activity_id: UUID,
    db: Session = Depends(get_db),
    user_id=Depends(get_current_user)
) -> SuccessResponse:
    return controllers.delete_activity(activity_id, db, user_id)

