from pydantic import BaseModel, Field, model_validator, ConfigDict
from datetime import time
from typing import Union, Annotated

class SettingsResponse(BaseModel):
	model_config = ConfigDict(from_attributes=True)
	
	morning_start_time: time
	morning_end_time: time
	evening_start_time: time
	evening_end_time: time
	is_morning_reminder_enabled: bool
	is_evening_reminder_enabled: bool
	total_target_activities: int
    
    
class SettingsCreateRequest(BaseModel):
	morning_start_time: time
	morning_end_time: time
	evening_start_time: time
	evening_end_time: time
	is_morning_reminder_enabled: bool
	is_evening_reminder_enabled: bool
	total_target_activities: Annotated[int, Field(ge=1, le=15)]

	@model_validator(mode="after")
	def end_from_start(self):
		if self.morning_end_time < self.morning_start_time or self.evening_end_time < self.evening_start_time:
			raise ValueError("morning end time must be after morning start time, and evening end time must be after evening start time")
		return self
    	
    
    
class SettingsUpdateRequest(BaseModel):
	morning_start_time: Union[time, None] = None
	morning_end_time: Union[time, None] = None
	evening_start_time: Union[time, None] = None
	evening_end_time: Union[time, None] = None
	is_morning_reminder_enabled: Union[bool, None] = None
	is_evening_reminder_enabled: Union[bool, None] = None
	total_target_activities: Annotated[Union[int, None], Field(ge=1, le=15)] = None

	@model_validator(mode="after")
	def end_from_start(self):
		if self.morning_start_time and self.morning_end_time:
			if self.morning_end_time < self.morning_start_time:
				raise ValueError("morning end_date must be after start_date")
		
		if self.evening_start_time and self.evening_end_time:
			if self.evening_end_time < self.evening_start_time:
				raise ValueError("evening end_date must be after start_date")
			
		return self

