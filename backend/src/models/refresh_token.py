from datetime import datetime

from sqlalchemy import UUID, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.mixins.id import IDMixin
from src.models.mixins.timestamp import TimestampMixin


class RefreshToken(IDMixin, TimestampMixin, Base):
	__tablename__ = "refresh_tokens"

	user_id: Mapped[UUID] = mapped_column(
		ForeignKey("users.id")
	)

	token: Mapped[str] = mapped_column()

	issued_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True)
	)

	expires_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True)
	)
