from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.tag import TagCreate
from src.repositories.tag import (
    get_tag_by_id,
    get_tag_by_name,
    get_all_tags,
    create_tag,
    delete_tag
)

async def get_tag_service(db: AsyncSession, tag_id: int):
    tag = await get_tag_by_id(db, tag_id)
    
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    return tag

async def get_tags_service(db: AsyncSession):
    return await get_all_tags(db)

async def create_tag_service(db: AsyncSession, tag_data: TagCreate):
    tag = await get_tag_by_name(db, tag_data.name)

    if tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    
    return await create_tag(db, tag_data)

async def delete_tag_service(db: AsyncSession, tag_id: int):
    tag = await get_tag_by_id(db, tag_id)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    await delete_tag(db, tag_id)
    return {"message": "Tag deleted successfully"}
