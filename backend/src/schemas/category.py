from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    @classmethod
    def from_orm(cls, category):
        return cls(
            id=category.id,
            name=category.name
        )