from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from src.database.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    token = Column(String, nullable=False)
    issued_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    revoked_at = Column(DateTime)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
