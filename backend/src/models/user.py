from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    profile_pic_url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime)