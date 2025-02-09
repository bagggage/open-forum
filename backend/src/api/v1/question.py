from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.engine import get_async_session
from src.schemas.question import QuestionCreate
from src.schemas.question import QuestionResponse
from src.schemas.question import QuestionUpdate
from src.service.question import create_question_service
from src.service.question import get_questions_service
from src.service.question import get_question_service
from src.service.question import delete_question_service
from src.service.question import update_question_service
from typing import List

router = APIRouter(prefix="/v1/questions", tags=["Questions"])

USER_ID = 1 # While auth is not implemented user_id is a mock

@router.post(
        "/", 
        response_model=QuestionResponse,
        summary="Create a new question for an authorized user")
async def create_question(
    question_data: QuestionCreate,
    db: AsyncSession = Depends(get_async_session)
):
    question = await create_question_service(db, question_data, USER_ID)
    return QuestionResponse.from_orm(question) 

@router.get(
        "/", 
        response_model=List[QuestionResponse], 
        summary="Get a list of all questions with pagination")
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
    await delete_question_service(db, question_id, USER_ID)

    return {"message": "Question deleted successfully"}

@router.put(
        "/{question_id}", 
        response_model=QuestionResponse, 
        summary="Update a question by its ID")
async def update_question(
    question_id: int,
    update_data: QuestionUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    updated_question = await update_question_service(db, question_id, USER_ID, update_data)
    return QuestionResponse.from_orm(updated_question)