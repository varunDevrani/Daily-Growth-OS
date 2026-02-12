from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from datetime import datetime
from src.database.base import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(String, nullable=False)

    expires_at = Column(DateTime)
    logout_at = Column(DateTime)
    last_activity_at = Column(DateTime, server_default=func.now())

    created_at = Column(DateTime, server_default=func.now())
    deleted_at = Column(DateTime)
