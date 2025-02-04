from datetime import datetime

from sqlalchemy import Integer, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.Base import Base


class Answer(Base):
    __tablename__ = 'answer'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    last_update_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    best_answer: Mapped[bool] = mapped_column(Boolean, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    question_id: Mapped[int] = mapped_column(ForeignKey('question.id'), nullable=True)

    vote: Mapped[list['Vote']] = relationship(back_populates='answer')
    question: Mapped['Question'] = relationship(back_populates='answer')
    user: Mapped['User'] = relationship(back_populates='answer')

