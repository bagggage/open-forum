from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.Base import Base


class Content(Base):
    __tablename__ = 'content'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    last_update_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    type_meta: Mapped[str] = mapped_column(Enum('question', 'post', name='type_meta'),
                                           nullable=False, default='active')

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    question_id: Mapped[int] = mapped_column(ForeignKey('question.id'))

    content: Mapped[list['Vote']] = relationship(back_populates='vote')

