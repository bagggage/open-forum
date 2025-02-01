from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.Base import Base
from src.models.many2many.question_tag import question_tag


class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    answer_id: Mapped[int] = mapped_column(ForeignKey('content.id'), nullable=True)

    tag: Mapped[list['Tag']] = relationship(secondary=question_tag, back_populates='question')
    category: Mapped['Category'] = relationship(back_populates='question')
    content: Mapped[list['Content']] = relationship(back_populates='question')


