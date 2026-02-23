from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from datetime import datetime
import uuid

from src.database.base import Base

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)

    token = Column(String, nullable=False)
    issued_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    revoked_at = Column(DateTime)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
