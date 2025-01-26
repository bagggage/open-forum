from __future__ import annotations
from sqlalchemy import Table, Column, Integer, ForeignKey

from src.db.Base import Base

question_tag = Table(
    "question_tag",
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)