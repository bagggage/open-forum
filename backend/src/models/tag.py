from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.Base import Base
from src.models.many2many.question_tag import question_tag


class Tag(Base):
    __tablename__ = 'tag'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    question: Mapped[list['Question']] = relationship(secondary=question_tag, back_populates='tag')