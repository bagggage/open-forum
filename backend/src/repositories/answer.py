from datetime import datetime
from datetime import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.answer import Answer
from src.schemas.answer import AnswerCreate
from sqlalchemy.future import select
from sqlalchemy import delete

async def create_answer(db: AsyncSession, answer_data: AnswerCreate, user_id: int):
    now = datetime.now(timezone.utc).replace(tzinfo=None)

    new_answer = Answer(
        text=answer_data.text,
        creation_time=now,
        last_update_time=now,
        best_answer=False,
        question_id=answer_data.question_id,
        user_id=user_id
    )

    db.add(new_answer)
    await db.commit()
    await db.refresh(new_answer)

    return new_answer

async def get_answer_by_id(db: AsyncSession, answer_id: int):
    result = await db.execute(select(Answer).where(Answer.id == answer_id))
    return result.scalars().first()

async def get_all_answers(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(Answer)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

async def get_answers_by_question(db: AsyncSession, question_id: int):
    result = await db.execute(select(Answer).where(Answer.question_id == question_id))
    return result.scalars().all()

async def delete_answer(db: AsyncSession, answer_id: int):
    await db.execute(delete(Answer).where(Answer.id == answer_id))
    await db.commit()