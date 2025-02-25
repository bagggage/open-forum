from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.auth_dependencies import current_user
from src.db.engine import get_async_session
from src.service.answer import create_answer_service
from src.schemas.answer import AnswerCreate
from src.schemas.answer import AnswerResponse
from src.service.answer import get_answer_service
from src.service.answer import get_answers_service
from src.service.answer import get_answers_by_question_service
from src.service.answer import delete_answer_service
from src.models import User
from typing import List

router = APIRouter(prefix="/v1/answers", tags=["Answers"])

@router.post(
    "/",
    response_model=AnswerResponse,
    summary="Create a new answer"
)
async def create_answer(
    answer_data: AnswerCreate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    answer = await create_answer_service(db, answer_data, user.id)
    return AnswerResponse.from_orm(answer)

@router.get(
    "/{answer_id}",
    response_model=AnswerResponse,
    summary="Get answer by ID"
)
async def get_answer(
    answer_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    return await get_answer_service(db, answer_id)

@router.get(
    "/", 
    response_model=List[AnswerResponse], 
    summary="Get a list of all answers with pagination"
)
async def get_answers(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session)
):
    answers = await get_answers_service(db, skip, limit)
    return [AnswerResponse.from_orm(q) for q in answers]

@router.get(
    "/by-question/", 
    response_model=List[AnswerResponse], 
    summary="Get answer by question ID"
)
async def get_answers_by_question_id(
    question_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    answers = await get_answers_by_question_service(db, question_id)
    return [AnswerResponse.from_orm(q) for q in answers]

@router.delete(
    "/{answer_id}", 
    summary="Delete answer by ID"
)
async def delete_answer(
    answer_id: int, 
    db: AsyncSession = Depends(get_async_session)
):
    return await delete_answer_service(db, answer_id)