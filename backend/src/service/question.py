from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.question import QuestionCreate
from src.schemas.question import QuestionUpdate
from src.schemas.question import QuestionResponse
from src.repositories.question import create_question
from src.repositories.question import delete_question
from src.repositories.question import get_question_by_id
from src.repositories.question import get_all_questions
from src.repositories.question import update_question
from src.repositories.question import get_questions_by_category
from src.repositories.tag import get_tag_by_names
from src.repositories.user import get_user_by_id
from src.repositories.role import get_role_by_id
from src.repositories.category import get_category_by_name
from src.models.question import Question

async def create_question_service(db: AsyncSession, question_data: QuestionCreate, user_id: int):
    category = await get_category_by_name(db, question_data.category_name)
    if not category:
        raise HTTPException(status_code=404, detail=f"Category '{question_data.category_name}' not found")

    new_question = Question(
        title=question_data.title,
        text=question_data.text,
        category_id=category.id,
        user_id=user_id
    )

    tags = await get_tag_by_names(db, question_data.tag_names)
    if tags:
        new_question.tag.extend(tags)
    
    created_question = await create_question(db, new_question)
    user = await get_user_by_id(db, created_question.user_id)
    return QuestionResponse.from_orm(created_question, user_name=user.name)

async def get_questions_service(db: AsyncSession, skip: int = 0, limit: int = 10):
    questions = await get_all_questions(db, skip, limit)

    result = []
    for question in questions:
        user = await get_user_by_id(db, question.user_id)
        question_response = QuestionResponse.from_orm(question, user_name=user.name)
        result.append(question_response)

    return result

async def get_question_service(db: AsyncSession, question_id: int):
    question = await get_question_by_id(db, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    user = await get_user_by_id(db, question.user_id)
    return QuestionResponse.from_orm(question, user_name=user.name)

async def get_questions_by_category_name_service(
    db: AsyncSession, 
    category_name: str, 
    skip: int = 0, 
    limit: int = 10
):
    category = await get_category_by_name(db, category_name)

    if not category:
        raise HTTPException(status_code=404, detail=f"Category '{category_name}' not found")

    questions = await get_questions_by_category(db, category.id, skip, limit)

    result = []
    for question in questions:
        user = await get_user_by_id(db, question.user_id)
        question_response = QuestionResponse.from_orm(question, user_name=user.name)
        result.append(question_response)

    return result

async def delete_question_service(db: AsyncSession, question_id: int, user_id: int):
    question = await get_question_by_id(db, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    if question.user_id != user_id:
        raise HTTPException(status_code=403, detail="Can delete only own questions")
    
    await delete_question(db, question_id)

async def update_question_service(db: AsyncSession, question_id: int, user_id: int, update_data: QuestionUpdate):
    question = await get_question_by_id(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    user = await get_user_by_id(db, user_id)
    role = await get_role_by_id(db, user.role_id)

    EDITING_ROLE = "Moderator"
    if question.user_id != user_id and role.role_name != EDITING_ROLE:
        raise HTTPException(status_code=403, detail="Can only edit own questions or be a Moderator")

    update_values = update_data.model_dump(exclude_unset=True)
    if not update_values:
        return question

    await update_question(db, question_id, update_values)

    return await get_question_service(db, question_id)
