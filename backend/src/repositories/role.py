from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.user import UserRole

# TODO: Implement a full-fledged user service
async def get_role_by_id(db: AsyncSession, role_id: int):
    result = await db.execute(select(UserRole).where(UserRole.id == role_id))
    return result.scalars().first()