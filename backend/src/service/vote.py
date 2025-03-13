from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.vote import VoteCreate
from src.repositories.vote import create_vote
from src.repositories.vote import get_votes_by_answer_id
from src.repositories.answer import get_answer_by_id

async def create_vote_service(db: AsyncSession, vote_data: VoteCreate, user_id: int):
    answer = await get_answer_by_id(db, vote_data.answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    votes = await get_votes_by_answer_id(db, vote_data.answer_id)

    if any(vote.user_id == user_id for vote in votes):
        raise HTTPException(status_code=403, detail="User has already voted for this answer")
    
    return await create_vote(db, vote_data, user_id)
