import uuid
from typing import Union
from datetime import time, datetime, timezone
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Setting(Base):
	__tablename__ = "settings"
    
	id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		primary_key=True,
		default=uuid.uuid4
	)

	user_id: Mapped[uuid.UUID] = mapped_column(
		ForeignKey("users.id")
	)

	morning_start_time: Mapped[time] = mapped_column()

	morning_end_time: Mapped[time] = mapped_column()

	is_morning_reminder_enabled: Mapped[bool] = mapped_column()

	evening_start_time: Mapped[time] = mapped_column()

	evening_end_time: Mapped[time] = mapped_column()

	is_evening_reminder_enabled: Mapped[bool] = mapped_column()

	total_target_activities: Mapped[int] = mapped_column(
		default=0
	)

	last_password_changed_at: Mapped[Union[datetime, None]] = mapped_column()

	created_at: Mapped[datetime] = mapped_column(
		default=lambda: datetime.now(timezone.utc)
	)

	updated_at: Mapped[datetime] = mapped_column(
		default=lambda: datetime.now(timezone.utc),
		onupdate=lambda: datetime.now(timezone.utc)
	)
