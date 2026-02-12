import secrets

import os
from datetime import datetime, timedelta
from fastapi import Depends, Request, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import select
from src.database.database import get_db
from src.models.user import User
from src.models.session import Session as Session_model
from src.schemas.auth import LoginRequest


def login_service(request: Request, response: Response, payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()

    if user is None:
        return {"message": "User not found"}

    session_id = secrets.token_hex(32)
    session_expire_days = os.getenv("SESSION_EXPIRE_DAYS", "7")

    db_session = Session_model(
        user_id=user.id,
        session_id=session_id,
        expires_at=datetime.utcnow() + timedelta(days=int(session_expire_days))
    )

    response.set_cookie(key="token", value=session_id, httponly=True, samesite="strict", max_age=int(session_expire_days) * 24 * 60 * 60)

    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return {"message": "user logged in", "session_id": session_id, "session_id_expires_in": session_expire_days }