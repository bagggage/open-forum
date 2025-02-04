from datetime import datetime

import pytz
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.Base import Base


class Notification(Base):
    __tablename__ = 'notification'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    create_date: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                               default=lambda: datetime.now(pytz.timezone('Europe/Moscow')),
                                               nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped['User'] = relationship(back_populates='notification')

