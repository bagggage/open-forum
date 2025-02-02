from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy import delete
from src.schemas.question import QuestionCreate
from src.models.question import Question
from src.models.category import Category
from src.models.tag import Tag
from src.models.many2many.question_tag import question_tag

async def create_question(db: AsyncSession, question_data: QuestionCreate, user_id: int):
    category = await db.execute(select(Category).filter(Category.name == question_data.category_name))
    category = category.scalars().first()

    if not category:
        raise ValueError(f"Category '{question_data.category_name}' not found")

    new_question = Question(
        title=question_data.title,
        text=question_data.text,
        category_id=category.id,
        user_id=user_id
    )
    
    tags = await db.execute(select(Tag).filter(Tag.name.in_(question_data.tag_names)))
    tags = tags.scalars().all()

    if tags:
        new_question.tag.extend(tags)

    db.add(new_question)
    await db.commit()
    await db.refresh(new_question)

    question_with_relations = await db.execute(
        select(Question)
        .options(joinedload(Question.category), joinedload(Question.tag))
        .filter(Question.id == new_question.id)
    )
    return question_with_relations.scalars().first()


async def get_all_questions(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(Question)
        .options(joinedload(Question.category), joinedload(Question.tag)) 
        .offset(skip)
        .limit(limit)
    )
    return result.unique().scalars().all()

async def delete_question(db: AsyncSession, question_id: int, user_id: int) -> bool:
    query = select(Question).where(Question.id == question_id)
    result = await db.execute(query)
    question = result.scalars().first()

    if not question or question.user_id != user_id:
        return False

    await db.execute(delete(question_tag).where(question_tag.c.question_id == question_id))

    await db.delete(question)
    await db.commit()

    return True