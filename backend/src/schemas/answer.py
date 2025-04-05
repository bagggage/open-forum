from datetime import datetime
from pydantic import BaseModel

class AnswerCreate(BaseModel):
    text: str
    question_id: int

class AnswerResponse(BaseModel):
    id: int
    text: str
    creation_time: datetime
    last_update_time: datetime
    best_answer: bool
    user_name: str
    question_id: int

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, answer, user_name: str = None):
        return cls(
            id=answer.id,
            text=answer.text,
            creation_time=answer.creation_time,
            last_update_time=answer.last_update_time,
            best_answer=answer.best_answer,
            user_id=answer.user_id,
            question_id=answer.question_id,
            user_name = user_name,
        )
