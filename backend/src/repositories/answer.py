from datetime import datetime
from datetime import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.answer import Answer
from src.schemas.answer import AnswerCreate
from sqlalchemy.future import select

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