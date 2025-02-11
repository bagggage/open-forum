from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.engine import get_async_session
from src.service.answer import create_answer_service
from src.schemas.answer import AnswerCreate
from src.schemas.answer import AnswerResponse

router = APIRouter(prefix="/v1/answers", tags=["Answers"])

USER_ID = 1 # While auth is not implemented user_id is a mock

@router.post(
        "/",
        response_model=AnswerResponse,
        summary="Create a new answer")
async def create_answer(
    answer_data: AnswerCreate,
    db: AsyncSession = Depends(get_async_session)
):
    answer = await create_answer_service(db, answer_data, USER_ID)
    return AnswerResponse.from_orm(answer)

@router.get(
        "/{answer_id}",
        response_model=AnswerResponse,
        summary="Get answer by ID")
async def get_answer(
    answer_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    return await get_answer_service(db, answer_id)
