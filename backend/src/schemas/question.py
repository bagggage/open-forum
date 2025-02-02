from pydantic import BaseModel
from datetime import datetime
from typing import List

class QuestionCreate(BaseModel):
    title: str
    text: str
    category_name: str
    tag_names: List[str]

class QuestionResponse(BaseModel):
    id: int
    title: str
    text: str
    creation_time: datetime
    category_name: str 
    tag_names: List[str] 
    user_id: int

    @classmethod
    def from_orm(cls, question):
        return cls(
            id=question.id,
            title=question.title,
            text=question.text,
            creation_time=question.creation_time,
            category_name=question.category.name if question.category else None,
            tag_names=[tag.name for tag in question.tag] if question.tag else [],
            user_id=question.user_id
        )

    class Config:
        from_attributes = True
