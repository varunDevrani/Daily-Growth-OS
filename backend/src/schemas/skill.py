from datetime import date
from typing import Annotated, List, Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.schemas.base import BaseSchema



class SkillActivityResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: UUID
	entry_date: date
	name: str
	is_priority: bool
	is_habit_to_protect: bool
	is_completed: bool
	minutes_practised: int


class SkillActivityCreateRequest(BaseSchema):
	name: Annotated[str, Field(min_length=2, max_length=100)]
	is_priority: bool = False
	is_habit_to_protect: bool = False
	is_completed: bool = False
	minutes_practised: Annotated[int, Field(ge=0, le=1440)] = 0



class SkillActivityUpdateRequest(BaseSchema):
	id: UUID
	name: Annotated[str, Field(min_length=2, max_length=100)]
	is_priority: bool
	is_habit_to_protect: bool
	is_completed: bool
	minutes_practised: Annotated[int, Field(ge=0, le=1440)]



class SkillActivityPartialUpdateRequest(BaseSchema):
	id: UUID
	name: Annotated[Union[str, None], Field(min_length=2, max_length=100)] = None
	is_priority: Union[bool, None] = None
	is_habit_to_protect: Union[bool, None] = None
	is_completed: Union[bool, None] = None
	minutes_practised: Annotated[Union[int, None], Field(ge=0, le=1440)] = None


class SkillActivitiesCreateRequest(BaseSchema):
	activities: List[SkillActivityCreateRequest]

class SkillActivitiesUpdateRequest(BaseSchema):
	activities: List[SkillActivityUpdateRequest]

class SkillActivitiesPartialUpdateRequest(BaseSchema):
	activities: List[SkillActivityPartialUpdateRequest]

class SkillActivitiesResponse(BaseModel):
	activities: List[SkillActivityResponse]

class SkillResponse(BaseModel):
    id: UUID
    name: str
    is_completed: bool
    total_activities: int
    activities: List[SkillActivityResponse]

class SkillCreateRequest(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=20)]
    activities: Union[List[SkillActivityCreateRequest], None] = None

class SkillUpdateRequest(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=20)]
    is_completed: bool

class SkillPartialUpdateRequest(BaseSchema):
    name: Annotated[Union[str, None], Field(min_length=2, max_length=20)] = None
    is_completed: Union[bool, None] = None


class SkillsResponse(BaseModel):
	total_skills: int
	skills: List[SkillResponse]
