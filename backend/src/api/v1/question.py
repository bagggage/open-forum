from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.engine import get_async_session
from src.schemas.question import QuestionCreate
from src.schemas.question import QuestionResponse
from src.service.question import create_question_service
from src.service.question import get_questions_service
from src.service.question import get_question_service
from src.service.question import delete_question_service
from typing import List

router = APIRouter(prefix="/v1/questions", tags=["Questions"])

@router.post(
        "/", 
        response_model=QuestionResponse,
        summary="Create a new question on a forum for authorized user")
async def create_question(
    question_data: QuestionCreate,
    db: AsyncSession = Depends(get_async_session)
):
    question = await create_question_service(db, question_data, user_id=1)
    return QuestionResponse.from_orm(question) 

@router.get(
        "/", 
        response_model=List[QuestionResponse], 
        summary="Get a list of all questions with pagination (default amount of elements is 10)")
async def get_questions(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session)
):
    questions = await get_questions_service(db, skip, limit)
    return [QuestionResponse.from_orm(q) for q in questions]

@router.get(
        "/{question_id}", 
        response_model=QuestionResponse,
        summary="Get one question by its ID")
async def get_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    question = await get_question_service(db, question_id)
    return QuestionResponse.from_orm(question)

@router.delete(
        "/{question_id}",
        summary="Delete a question by its ID if authorized user created that question")
async def delete_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    user_id = 1  # While auth is not implemented user_id is a mock

    await delete_question_service(db, question_id, user_id)

    return {"message": "Question deleted successfully"}

