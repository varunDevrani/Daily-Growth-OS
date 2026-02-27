from  pydantic import BaseModel
from datetime import date,datetime


class EveningCreate(BaseModel):
    date: date
    win: str
    mistake: str
    distraction: str
    mood_rating: int
    energy_rating: int
    lesson: str

class EveningUpdate(BaseModel):
    win: str
    mistake: str
    distraction: str
    mood_rating: int
    energy_rating: int
    lesson: str

class EveningResponse(BaseModel):
    id: str
    user_id: int
    date: date
    win: str
    mistake: str
    distraction: str
    mood_rating: int
    energy_rating: int
    lesson: str
    created_at: datetime
    updated_at: datetime
   
    class Config:
        orm_mode = True