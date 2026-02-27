from  pydantic import BaseModel
from datetime import date,datetime
from uuid import UUID


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
    id: UUID
    user_id: UUID
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