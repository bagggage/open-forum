from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from src.schemas.user import UserRead, UserCreate
from src.service.user_manager import get_user_manager
from src.service.auth import auth_backend
from src.models.user import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

auth_router = APIRouter()

auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/v1/auth/jwt",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/v1/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/v1/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/v1/auth",
    tags=["auth"],
)