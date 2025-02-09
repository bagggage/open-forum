from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from src.models.tag import Tag
from src.schemas.tag import TagCreate

async def get_tag_by_id(db: AsyncSession, tag_id: int):
    result = await db.execute(select(Tag).where(Tag.id == tag_id))
    return result.scalars().first()

async def get_tag_by_name(db: AsyncSession, tag_name: str):
    result = await db.execute(select(Tag).where(Tag.name == tag_name))
    return result.scalars().first()

async def get_all_tags(db: AsyncSession):
    result = await db.execute(select(Tag))
    return result.scalars().all()

async def create_tag(db: AsyncSession, tag_data: TagCreate):
    new_tag = Tag(name=tag_data.name)

    db.add(new_tag)
    await db.commit()
    await db.refresh(new_tag)
    
    return new_tag

async def delete_tag(db: AsyncSession, tag_id: int):
    await db.execute(delete(Tag).where(Tag.id == tag_id))
    await db.commit()
