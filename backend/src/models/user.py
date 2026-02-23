from sqlalchemy import Column, Integer, String, DateTime, UUID
from datetime import datetime
from src.database.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    profile_pic_url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)