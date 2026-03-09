from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: UUID
	first_name: Union[str, None] = None
	last_name: Union[str, None] = None
	email: str
	profile_pic_url: Union[str, None] = None
