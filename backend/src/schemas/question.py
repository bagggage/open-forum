from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from typing import List
from typing import Optional

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
    user_name: str 

    @classmethod
    def from_orm(cls, question, user_name: str = None):
        return cls(
            id=question.id,
            title=question.title,
            text=question.text,
            creation_time=question.creation_time,
            category_name=question.category.name if question.category else None,
            tag_names=[tag.name for tag in question.tag] if question.tag else [],
            user_name=user_name,
        )

    class Config:
        from_attributes = True

class QuestionUpdate(BaseModel):
    title: Optional[str] = Field(None, description="Updated title of the question")
    text: Optional[str] = Field(None, description="Updated text of the question")

    class Config:
        orm_mode = True