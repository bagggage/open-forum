from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from src.models.category import Category
from src.schemas.category import CategoryCreate

async def get_category_by_id(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).where(Category.id == category_id))
    return result.scalars().first()

async def get_category_by_name(db: AsyncSession, category_name: str):
    result = await db.execute(select(Category).where(Category.name == category_name))
    return result.scalars().first()

async def get_all_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def create_category(db: AsyncSession, category: CategoryCreate):
    new_category = Category(name=category.name)

    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    
    return new_category

async def delete_category(db: AsyncSession, category_id: int):
    await db.execute(delete(Category).where(Category.id == category_id))
    await db.commit()    