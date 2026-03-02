from sqlalchemy.orm import Session
from src.models.evening import EveningReflection
from src.schemas.evening import EveningCreate,EveningUpdate 
from uuid import UUID
from fastapi import HTTPException
from datetime import date,datetime

# function to create evening reflection
def create_evening(db:Session,user_id: UUID, payload: EveningCreate):
    # Check if an evening reflection already exists for the user on the given date
    existing = db.query(EveningReflection).filter(
        EveningReflection.user_id == user_id,
        EveningReflection.date == payload.date).first()
    if existing:
        raise HTTPException(status_code=400, detail="Evening reflection for this date already exists.")
    
    evening = EveningReflection(
        user_id=user_id,
        date=payload.date,
        win=payload.win,
        mistake=payload.mistake,
        distraction=payload.distraction,
        mood_rating=payload.mood_rating,
        energy_rating=payload.energy_rating,
        lesson=payload.lesson
    )
    db.add(evening)
    db.commit()
    db.refresh(evening)
    return evening


# for updating the evening reflection
def update_evening(db:Session, evening_id: UUID, user_id: UUID, payload: EveningUpdate):
# Check if the evening reflection exists and belongs to the user
    evening = db.query(EveningReflection).filter(
        EveningReflection.id == evening_id,
        EveningReflection.user_id == user_id).first()
    if not evening:
        raise HTTPException(status_code=404, detail="Evening reflection not found.")
    
    evening.win = payload.win
    evening.mistake = payload.mistake
    evening.distraction = payload.distraction
    evening.mood_rating = payload.mood_rating
    evening.energy_rating = payload.energy_rating
    evening.lesson = payload.lesson
    evening.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(evening)
    return evening


# for getting the evening reflection by date
def get_evening_by_date(db:Session, user_id: UUID, target_date: date):
    # Check if the evening reflection exists for the user on the given date
    evening = db.query(EveningReflection).filter(
        EveningReflection.user_id == user_id,
        EveningReflection.date == target_date
    ).first()
    if not evening:
        raise HTTPException(status_code=404, detail="Evening reflection not found for the given date.")
    return evening


# for deleting the evening reflection
def delete_evening(db:Session, evening_id: UUID, user_id: UUID):
    # Check if the evening reflection exists and belongs to the user
    evening = db.query(EveningReflection).filter(
        EveningReflection.id == evening_id,
        EveningReflection.user_id == user_id
    ).first()
    if not evening:
        raise HTTPException(status_code=404, detail="Evening reflection not found.")
    db.delete(evening)
    db.commit()
    return {"detail": "Evening reflection deleted successfully."}
