from datetime import datetime
from typing import List, Union

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.mixins.id import IDMixin
from src.models.mixins.timestamp import TimestampMixin


class User(IDMixin, TimestampMixin, Base):
    __tablename__ = "users"

    first_name: Mapped[Union[str, None]] = mapped_column()

    last_name: Mapped[Union[str, None]] = mapped_column()

    email: Mapped[str] = mapped_column(
    	index=True
    )

    password_hash: Mapped[str] = mapped_column()

    profile_pic_url: Mapped[Union[str, None]] = mapped_column()

    is_verfied: Mapped[bool] = mapped_column(
    	default=False
    )

    deleted_at: Mapped[Union[datetime, None]] = mapped_column(
    	DateTime(timezone=True)
    )

    refresh_tokens: Mapped[List["RefreshToken"]] = relationship(
   		back_populates="user",
    	cascade="all, delete-orphan"
    )
