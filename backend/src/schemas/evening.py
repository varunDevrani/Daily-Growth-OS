from pydantic import ConfigDict, Field
from uuid import UUID
from typing import Optional
import datetime
from src.schemas.base import BaseSchema


class EveningCreate(BaseSchema):
    win: str = Field(..., min_length=2, max_length=255)
    mistake: str = Field(..., min_length=2, max_length=255)
    distraction: str = Field(..., min_length=2, max_length=255)
    lesson: str = Field(..., min_length=2, max_length=255)

    mood_rating: int = Field(..., ge=1, le=5)
    energy_rating: int = Field(..., ge=1, le=5)


class EveningUpdate(BaseSchema):
    win: Optional[str] = Field(None, min_length=2, max_length=255)
    mistake: Optional[str] = Field(None, min_length=2, max_length=255)
    distraction: Optional[str] = Field(None, min_length=2, max_length=255)
    lesson: Optional[str] = Field(None, min_length=2, max_length=255)

    mood_rating: Optional[int] = Field(None, ge=1, le=5)
    energy_rating: Optional[int] = Field(None, ge=1, le=5)


class EveningResponse(BaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    date: datetime.date

    win: str
    mistake: str
    distraction: str
    lesson: str

    mood_rating: int
    energy_rating: int

    created_at: datetime.datetime
    updated_at: datetime.datetime