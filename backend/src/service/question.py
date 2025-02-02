from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.question import QuestionCreate
from src.repositories.question import create_question
from src.repositories.question import delete_question
from src.repositories.question import get_question_by_id
from src.repositories.question import get_all_questions

async def create_question_service(db: AsyncSession, question_data: QuestionCreate, user_id: int):
    return await create_question(db, question_data, user_id)

async def get_questions_service(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await get_all_questions(db, skip, limit)

async def get_question_service(db: AsyncSession, question_id: int):
    question = await get_question_by_id(db, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return question

async def delete_question_service(db: AsyncSession, question_id: int, user_id: int) -> bool:
    return await delete_question(db, question_id, user_id)
