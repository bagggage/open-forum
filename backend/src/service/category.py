from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.category import CategoryCreate
from src.repositories.category import (
    get_category_by_id,
    get_category_by_name,
    get_all_categories,
    create_category,
    delete_category
)

async def get_category_service(db: AsyncSession, category_id: int):
    category = await get_category_by_id(db, category_id)
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

async def get_categories_service(db: AsyncSession):
    return await get_all_categories(db)

async def create_category_service(db: AsyncSession, category_data: CategoryCreate):
    category = await get_category_by_name(db, category_data.name)

    if category:
        raise HTTPException(status_code=400, detail="Category already exists")
    
    return await create_category(db, category_data)

async def delete_category_service(db: AsyncSession, category_id: int):
    category = await get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    await delete_category(db, category_id)
    return {"message": "Category deleted successfully"}

