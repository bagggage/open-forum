from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.engine import get_async_session
from src.schemas.question import QuestionCreate, QuestionResponse
from src.service.question import create_question_service, get_questions_service, delete_question_service
from typing import List
from fastapi import HTTPException

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.post("/create", response_model=QuestionResponse)
async def create_question_endpoint(
    question_data: QuestionCreate,
    db: AsyncSession = Depends(get_async_session)
):
    question = await create_question_service(db, question_data, user_id=1)
    return QuestionResponse.from_orm(question) 

@router.get("/all", response_model=List[QuestionResponse])
async def get_questions_endpoint(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session)
):
    questions = await get_questions_service(db, skip, limit)
    return [QuestionResponse.from_orm(q) for q in questions]

@router.delete("/{question_id}")
async def delete_question_endpoint(
    question_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    user_id = 1
    success = await delete_question_service(db, question_id, user_id)
    
    if not success:
        raise HTTPException(status_code=403, detail="You can delete only your own questions")
    
    return {"message": "Question deleted successfully"}
