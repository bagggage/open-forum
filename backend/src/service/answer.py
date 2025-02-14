from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.answer import AnswerCreate
from src.repositories.question import get_question_by_id
from src.repositories.answer import create_answer
from src.repositories.answer import get_answer_by_id
from src.repositories.answer import get_all_answers
from src.repositories.answer import get_answers_by_question

async def create_answer_service(db: AsyncSession, answer_data: AnswerCreate, user_id: int):
    question = await get_question_by_id(db, answer_data.question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return await create_answer(db, answer_data, user_id)

async def get_answer_service(db: AsyncSession, answer_id: int):
    answer = await get_answer_by_id(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return answer

async def get_answers_service(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await get_all_answers(db, skip, limit)

async def get_answers_by_question_service(db: AsyncSession, question_id: int):
    question = await get_question_by_id(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return await get_answers_by_question(db, question_id)