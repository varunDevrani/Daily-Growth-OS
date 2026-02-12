from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from src.database.base import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(String, nullable=False)

    expires_at = Column(DateTime)
    logout_at = Column(DateTime)
    last_activity_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))

    created_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)
