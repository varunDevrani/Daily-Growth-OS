from datetime import date
from uuid import UUID
from typing import Annotated, List

from pydantic import ConfigDict, Field
from src.schemas.base import BaseSchema
from src.schemas.morning_activity import (
    MorningActivityCreate,
    MorningActivityUpdate,
    MorningActivityResponse
)


class MorningCreate(BaseSchema):
    confidence_rating: Annotated[int, Field(ge=1, le=5)]
    activities: List[MorningActivityCreate] = Field(default_factory=list)


class MorningUpdate(BaseSchema):

    confidence_rating: Annotated[int | None, Field(ge=1, le=5)] = None
    activities: list[MorningActivityUpdate] | None = None


class MorningResponse(BaseSchema):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    date: date
    confidence_rating: int
    activities: list[MorningActivityResponse]

