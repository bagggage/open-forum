from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.tag import TagCreate, TagResponse
from src.db.engine import get_async_session
from src.service.tag import (
    get_tag_service,
    get_tags_service,
    create_tag_service,
    delete_tag_service
)

router = APIRouter(prefix="/v1/tags", tags=["Tags"])

@router.get(
        "/", 
        summary="Get all tags")
async def get_tags(
    db: AsyncSession = Depends(get_async_session)
):
    return await get_tags_service(db)

@router.get(
        "/{tag_id}", 
        summary="Get tag by ID")
async def get_tag(
    tag_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    return await get_tag_service(db, tag_id)

@router.post(
        "/", 
        response_model=TagResponse, 
        summary="Create a new tag")
async def create_tag(
    tag_data: TagCreate, 
    db: AsyncSession = Depends(get_async_session)
):
    tag = await create_tag_service(db, tag_data)
    return TagResponse.from_orm(tag)

@router.delete(
        "/{tag_id}", 
        summary="Delete tag by ID")
async def delete_tag(
    tag_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    return await delete_tag_service(db, tag_id)
