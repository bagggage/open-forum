from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy import delete
from sqlalchemy import update
from src.models.question import Question
from src.models.many2many.question_tag import question_tag

async def create_question(db: AsyncSession, new_question: Question):
    db.add(new_question)
    await db.commit()
    await db.refresh(new_question)
    
    return new_question

async def get_all_questions(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(Question)
        .options(joinedload(Question.category), joinedload(Question.tag)) 
        .offset(skip)
        .limit(limit)
    )
    return result.unique().scalars().all()

async def get_question_by_id(db: AsyncSession, question_id: int):
    result = await db.execute(
        select(Question)
        .options(joinedload(Question.category), joinedload(Question.tag))
        .where(Question.id == question_id)
    )
    return result.scalars().first()

async def get_questions_by_category(
    db: AsyncSession, 
    category_id: int, 
    skip: int = 0, 
    limit: int = 10
):
    result = await db.execute(
        select(Question)
        .options(joinedload(Question.category), joinedload(Question.tag))
        .where(Question.category_id == category_id)
        .offset(skip)
        .limit(limit)
    )
    return result.unique().scalars().all()

async def delete_question(db: AsyncSession, question_id: int):
    await db.execute(delete(question_tag).where(question_tag.c.question_id == question_id))

    query = delete(Question).where(Question.id == question_id)
    await db.execute(query)
    await db.commit()

async def update_question(db: AsyncSession, question_id: int, update_values: dict):
    query = (
        update(Question)
        .where(Question.id == question_id)
        .values(**update_values)
        .execution_options(synchronize_session="fetch")
    )

    await db.execute(query)
    await db.commit()
