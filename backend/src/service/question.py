from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.question import create_question, get_all_questions
from src.schemas.question import QuestionCreate
from src.repositories.question import delete_question

async def create_question_service(db: AsyncSession, question_data: QuestionCreate, user_id: int):
    return await create_question(db, question_data, user_id)

async def get_questions_service(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await get_all_questions(db, skip, limit)

async def delete_question_service(db: AsyncSession, question_id: int, user_id: int) -> bool:
    return await delete_question(db, question_id, user_id)
