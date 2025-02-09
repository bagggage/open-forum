from pydantic import BaseModel

class TagCreate(BaseModel):
    name: str

class TagResponse(BaseModel):
    id: int
    name: str

    @classmethod
    def from_orm(cls, tag):
        return cls(
            id=tag.id,
            name=tag.name
        )
