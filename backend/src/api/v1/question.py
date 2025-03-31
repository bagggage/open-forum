import fastapi_users
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.auth_dependencies import current_user
from src.db.engine import get_async_session
from src.schemas.question import QuestionCreate
from src.schemas.question import QuestionResponse
from src.schemas.question import QuestionUpdate
from src.service.question import create_question_service
from src.service.question import get_questions_service
from src.service.question import get_question_service
from src.service.question import delete_question_service
from src.service.question import update_question_service
from src.service.question import get_questions_by_category_name_service
from src.models import User
from typing import List

router = APIRouter(prefix="/v1/questions", tags=["Questions"])

@router.post(
    "/", 
    response_model=QuestionResponse,
    summary="Create a new question for an authorized user"
)
async def create_question(
    question_data: QuestionCreate,
    db: AsyncSession = Depends(get_async_session,),
    user: User = Depends(current_user)
):
    question = await create_question_service(db, question_data, user.id)
    return QuestionResponse.from_orm(question) 

@router.get(
    "/", 
    response_model=List[QuestionResponse], 
    summary="Get a list of all questions with pagination"
)
async def get_questions(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session)
):
    return await get_questions_service(db, skip, limit)

@router.get(
    "/{question_id}", 
    response_model=QuestionResponse,
    summary="Get one question by its ID"
)
async def get_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    return await get_question_service(db, question_id)

@router.get(
    "/by-category/",
    response_model=List[QuestionResponse], 
    summary="Get all questions by category name"
)
async def get_questions_by_category_name(
    category: str, 
    db: AsyncSession = Depends(get_async_session)
):
    questions = await get_questions_by_category_name_service(db, category)
    return [QuestionResponse.from_orm(q) for q in questions]

@router.delete(
    "/{question_id}",
    summary="Delete a question by its ID if authorized user created that question"
)
async def delete_question(
    question_id: int,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    await delete_question_service(db, question_id, user.id)
    return {"message": "Question deleted successfully"}

@router.put(
    "/{question_id}",
    response_model=QuestionResponse,
    summary="Update a question by its ID")
async def update_question(
    question_id: int,
    update_data: QuestionUpdate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    updated_question = await update_question_service(db, question_id, user.id, update_data)
    return QuestionResponse.from_orm(updated_question)
