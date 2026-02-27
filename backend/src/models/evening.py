from sqlalchemy import Column,Integer,String,Date,DateTime,ForeignKey,UUID,UniqueConstraint
from src.database.base import Base
import uuid
from datetime import datetime

class EveningReflection(Base):
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,index=True)
    user_id= Column(UUID(as_uuid=True),ForeignKey("users.id"),nullable=False)
    date=Column(Date,nullable=False)
    win=Column(String)
    mistake=Column(String)
    distraction=Column(String)
    mood_rating=Column(Integer)
    energy_rating=Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    __table_args__=(UniqueConstraint("user_id","date"))