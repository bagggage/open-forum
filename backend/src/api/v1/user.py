from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.engine import get_async_session
from src.utils.auth_dependencies import current_user
from src.service.user_manager import get_current_user_service
from src.schemas.user import UserResponse
from src.models import User

router = APIRouter(prefix="/v1/users", tags=["Users"])

@router.get(
    "/",
    response_model=UserResponse,
    summary="Get authorized user information"
)
async def get_current_user(
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await get_current_user_service(db, user)