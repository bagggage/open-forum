from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.answer import AnswerCreate
from src.schemas.answer import AnswerResponse
from src.repositories.question import get_question_by_id
from src.repositories.answer import create_answer
from src.repositories.answer import get_answer_by_id
from src.repositories.answer import get_all_answers
from src.repositories.answer import get_answers_by_question
from src.repositories.answer import delete_answer
from src.repositories.answer import update_best_answer
from src.repositories.user import get_user_by_id

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

    answers = await get_answers_by_question(db, question_id)

    result = []
    for answer in answers:
        user = await get_user_by_id(db, answer.user_id)
        answer_response = AnswerResponse.from_orm(answer, user_name=user.name)
        result.append(answer_response)

    return result

async def update_best_answer_service(db: AsyncSession, answer_id: int, user_id: int):
    answer = await get_answer_by_id(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    LIMIT = 100
    skip = 0
    while True:
        answers = await get_all_answers(db, skip, LIMIT)

        if not answers:
            break 

        if any(a.best_answer for a in answers if a.question_id == answer.question_id):
            raise HTTPException(status_code=403, detail="There is already an answer marked as solution")

        skip += LIMIT

    question = await get_question_by_id(db, answer.question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if user_id != question.user_id:
        raise HTTPException(status_code=403, detail="Mark an answer as solution can only users that creates that question")
    
    await update_best_answer(db, answer_id)

    return await get_answer_by_id(db, answer_id)

async def delete_answer_service(db: AsyncSession, answer_id: int):
    answer = await get_answer_by_id(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    await delete_answer(db, answer_id)
    return {"message": "Answer deleted successfully"}