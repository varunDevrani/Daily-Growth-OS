from sqlalchemy.orm import Session
from src.schemas.evening import EveningCreate,EveningUpdate
from src.services.evening import create_evening,update_evening,get_evening_by_date,delete_evening
from uuid import UUID
from datetime import date




def create_evening_controller(request:EveningCreate, db:Session, user_id: UUID):
    evening=create_evening(db=db, user_id=user_id, payload=request)
    return {
        "message": "Evening reflection created successfully",
        "id": evening.id,
        "date": evening.date
    }

def update_evening_controller(evening_id: UUID, request:EveningUpdate, db:Session, user_id: UUID):
    evening=update_evening(db=db, evening_id=evening_id, user_id=user_id, payload=request)
    return {
        "message": "Evening reflection updated successfully",
        "id": evening.id,
    }

def get_evening_by_date_controller(target_date: date, db:Session, user_id: UUID):
    evening=get_evening_by_date(db=db, user_id=user_id, target_date=target_date)
    if not evening:
        return {
            "message": "No evening reflection found for this date"
        }
    return evening


def delete_evening_controller(evening_id: UUID, db:Session, user_id: UUID):
    evening=delete_evening(db=db, evening_id=evening_id, user_id=user_id)
    return {
        "message": "Evening reflection deleted successfully",
        "id": evening_id
    }



