from datetime import datetime

from sqlalchemy import String, Enum, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.Base import Base


class Vote(Base):
    __tablename__ = 'vote'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    content_id: Mapped[int] = mapped_column(ForeignKey('content.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    content: Mapped[list['Content']] = relationship(back_populates='vote')