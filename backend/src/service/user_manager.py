from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.schemas.user import UserResponse
from src.repositories.role import get_role_by_id
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from src.models.user import User, get_user_db

SECRET = "SECRET"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

async def get_current_user_service(db: AsyncSession, user: User):
    role = await get_role_by_id(db, user.role_id)

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    return UserResponse.from_orm(user, role.role_name)
