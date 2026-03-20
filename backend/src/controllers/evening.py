from uuid import UUID
from datetime import date
from sqlalchemy.orm import Session

import src.services.evening as Service

from src.schemas.api_response import SuccessResponse
from src.schemas.evening import EveningCreate, EveningUpdate, EveningResponse


def create_evening(
    payload: EveningCreate,
    db: Session,
    user_id: UUID
) -> SuccessResponse[EveningResponse]:
    evening = Service.create_evening(db, user_id, payload)

    return SuccessResponse[EveningResponse](
        message="Evening entry created successfully",
        data=evening
    )


def update_evening(
    payload: EveningUpdate,
    db: Session,
    evening_id: UUID,
    user_id: UUID
) -> SuccessResponse[EveningResponse]:
    evening = Service.update_evening(db, user_id, payload, evening_id)

    return SuccessResponse[EveningResponse](
        message="Evening entry updated successfully",
        data=evening
    )


def get_evening(
    target_date: date,
    db: Session,
    user_id: UUID
) -> SuccessResponse[EveningResponse]:
    evening = Service.get_evening(db, target_date, user_id)

    return SuccessResponse[EveningResponse](
        message="Evening entry retrieved successfully",
        data=evening
    )


def delete_evening(
    evening_id: UUID,
    db: Session,
    user_id: UUID
) -> SuccessResponse[EveningResponse]:
    Service.delete_evening(db, evening_id, user_id)

    return SuccessResponse[EveningResponse](
        message="Evening entry deleted successfully"
    )