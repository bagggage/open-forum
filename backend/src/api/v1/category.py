from fastapi import APIRouter, Depends
from src.db.engine import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.category import CategoryCreate
from src.schemas.category import CategoryResponse
from src.service.category import (
    get_category_service,
    get_categories_service,
    create_category_service,
    delete_category_service
)

router = APIRouter(prefix="/v1/categories", tags=["Categories"])

@router.get(
        "/", 
        summary="Get all categories")
async def get_categories(db: AsyncSession = Depends(get_async_session)):
    return await get_categories_service(db)

@router.get(
        "/{category_id}", 
        summary="Get category by ID")
async def get_category(
    category_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    return await get_category_service(db, category_id)

@router.post(
        "/", 
        response_model=CategoryResponse, 
        summary="Create a new category")
async def create_category(
    category_data: CategoryCreate, 
    db: AsyncSession = Depends(get_async_session)
):
    category = await create_category_service(db, category_data)
    return CategoryResponse.from_orm(category) 

@router.delete(
        "/{category_id}", 
        summary="Delete category by ID")
async def delete_category(
    category_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    return await delete_category_service(db, category_id)