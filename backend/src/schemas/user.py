from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[int]):

    id: int
    name: str
    last_name: str | None
    email: EmailStr
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):

    name: str
    email: EmailStr
    password: str


class UserUpdate(schemas.BaseUserUpdate):

    password: str = None
    email: EmailStr = None


class AddUsersToGroupRequest(BaseModel):

    user_email: list[str]
    user_group_id: int


class ChangeUserRole(BaseModel):

    mode: str
    email: EmailStr

class CreateRole(BaseModel):

    id: int
    role_name: str


class CreateGroupAttributes(BaseModel):

    id: int
    attribute_name: str