from http import HTTPStatus
from uuid import UUID
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.evening import Evening
from src.schemas.evening import EveningCreate, EveningUpdate, EveningResponse
from src.exceptions import DomainException



def get_evening_or_404(db: Session, user_id: UUID, evening_id: UUID):
    stmt = select(Evening).where(
        Evening.id == evening_id,
        Evening.user_id == user_id
    )

    evening = db.scalar(stmt)

    if not evening:
        raise DomainException(
            status_code=HTTPStatus.NOT_FOUND,
            message="Evening entry not found."
        )

    return evening


def create_evening(db: Session, user_id: UUID, payload: EveningCreate)-> EveningResponse:
    today = date.today()

    stmt = select(Evening).where(
        Evening.user_id == user_id,
        Evening.date == today
    )

    existing = db.scalar(stmt)

    if existing:
        raise DomainException(
            status_code=HTTPStatus.CONFLICT,
            message=f"Evening entry for date {today} already exists."
        )

    evening = Evening(
        user_id=user_id,
        win=payload.win,
        mistake=payload.mistake,
        distraction=payload.distraction,
        mood_rating=payload.mood_rating,
        energy_rating=payload.energy_rating,
        lesson=payload.lesson
    )

    db.add(evening)
    db.flush()
    db.refresh(evening)

    return EveningResponse.model_validate(evening)


def update_evening(db: Session, user_id: UUID, payload: EveningUpdate, evening_id: UUID)-> EveningResponse:
    evening = get_evening_or_404(db, user_id, evening_id)

    update_data = payload.model_dump(exclude_unset=True, exclude_none=True)

    for field, value in update_data.items():
        setattr(evening, field, value)

    db.flush()
    db.refresh(evening)

    return EveningResponse.model_validate(evening)


def get_evening(db: Session, target_date: date, user_id: UUID)-> EveningResponse:
    stmt = select(Evening).where(
        Evening.date == target_date,
        Evening.user_id == user_id
    )

    evening = db.scalar(stmt)

    if not evening:
        raise DomainException(
            status_code=HTTPStatus.NOT_FOUND,
            message="Evening entry not found."
        )

    return EveningResponse.model_validate(evening)


def delete_evening(db: Session, evening_id: UUID, user_id: UUID):
    evening = get_evening_or_404(db, user_id, evening_id)

    db.delete(evening)
    db.flush()