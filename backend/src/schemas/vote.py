from pydantic import BaseModel

class VoteCreate(BaseModel):
    answer_id: int

class VoteResponse(BaseModel):
    id: int
    user_id: int
    answer_id: int

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, vote):
        return cls(
            id=vote.id,
            user_id=vote.user_id,
            answer_id=vote.answer_id
        )
