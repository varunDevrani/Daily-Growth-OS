from src.database.database import get_db
from src.controllers.evening import create_evening_controller,update_evening_controller,get_evening_by_date_controller,delete_evening_controller
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import date
from src.schemas.evening import EveningCreate,EveningUpdate
from src.utils.current_user import get_current_user

router = APIRouter(prefix="/evening", tags=["evening"])

@router.post("")
def create_evening(request:EveningCreate,  current_user=Depends(get_current_user),db:Session = Depends(get_db) ):
    return create_evening_controller(request=request, db=db, user_id=current_user)


@router.patch("/{evening_id}")
def update_evening(evening_id: UUID, request:EveningUpdate, current_user=Depends(get_current_user), db:Session = Depends(get_db)):
    return update_evening_controller(evening_id=evening_id, request=request, db=db, user_id=current_user)

@router.get("/date/{target_date}")
def get_evening_by_date(target_date: date,current_user=Depends(get_current_user), db:Session = Depends(get_db)):
    return get_evening_by_date_controller(target_date=target_date, db=db, user_id=current_user)


@router.delete("/{evening_id}")
def delete_evening(evening_id: UUID, current_user=Depends(get_current_user),db:Session = Depends(get_db)):
    return delete_evening_controller(evening_id=evening_id, db=db, user_id=current_user)