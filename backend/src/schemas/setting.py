from pydantic import BaseModel
from datetime import time
from typing import Union

class SettingsResponse(BaseModel):
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
    total_target_activities: int
    
    
class SettingsUpdateRequest(BaseModel):
    morning_start_time: Union[time, None] = None
    morning_end_time: Union[time, None] = None
    evening_start_time: Union[time, None] = None
    evening_end_time: Union[time, None] = None
    is_morning_reminder_enabled: Union[bool, None] = None
    is_evening_reminder_enabled: Union[bool, None] = None
    total_target_activities: Union[int, None] = None
