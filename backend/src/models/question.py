from datetime import datetime

import pytz
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.Base import Base
from src.models.many2many.question_tag import question_tag


class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    creation_time: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                               default=lambda: datetime.now(pytz.timezone('Europe/Moscow')),
                                               nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    tag: Mapped[list['Tag']] = relationship(secondary=question_tag, back_populates='question')
    category: Mapped['Category'] = relationship(back_populates='question')
    answer: Mapped[list['Answer']] = relationship(back_populates='question')


