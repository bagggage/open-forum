from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.question import QuestionCreate
from src.schemas.question import QuestionUpdate
from src.repositories.question import create_question
from src.repositories.question import delete_question
from src.repositories.question import get_question_by_id
from src.repositories.question import get_all_questions
from src.repositories.question import update_question
from src.repositories.user import get_user_by_id
from src.repositories.role import get_role_by_id

async def create_question_service(db: AsyncSession, question_data: QuestionCreate, user_id: int):
    return await create_question(db, question_data, user_id)

async def get_questions_service(db: AsyncSession, skip: int = 0, limit: int = 10):
    return await get_all_questions(db, skip, limit)

async def get_question_service(db: AsyncSession, question_id: int):
    question = await get_question_by_id(db, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return question

async def delete_question_service(db: AsyncSession, question_id: int, user_id: int):
    question = await get_question_by_id(db, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if question.user_id != user_id:
        raise HTTPException(status_code=403, detail="You can delete only your own questions")
    
    await delete_question(db, question_id)

async def update_question_service(db: AsyncSession, question_id: int, user_id: int, update_data: QuestionUpdate):
    question = await get_question_by_id(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    user = await get_user_by_id(db, user_id)
    role = await get_role_by_id(db, user.role_id)

    if question.user_id != user_id and role.role_name != "Moderator":
        raise HTTPException(status_code=403, detail="You can only edit your own questions or be a Moderator")

    update_values = update_data.model_dump(exclude_unset=True)
    if not update_values:
        return question

    return await update_question(db, question_id, update_values)