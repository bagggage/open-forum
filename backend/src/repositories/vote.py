from sqlalchemy.ext.asyncio import AsyncSession
from src.models.vote import Vote
from sqlalchemy.future import select
from sqlalchemy import delete
from src.schemas.vote import VoteCreate

async def create_vote(db: AsyncSession, vote: VoteCreate, user_id: int):
    new_vote = Vote(
        answer_id=vote.answer_id,
        user_id=user_id
    )

    db.add(new_vote)
    await db.commit()
    await db.refresh(new_vote)
    
    return new_vote

async def get_all_votes(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(Vote)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

async def get_votes_by_answer_id(db: AsyncSession, answer_id: int):
    result = await db.execute(select(Vote).where(Vote.answer_id == answer_id))
    return result.scalars().all()

async def get_vote_by_id(db: AsyncSession, vote_id: int):
    result = await db.execute(select(Vote).where(Vote.id == vote_id))
    return result.scalars().first()

async def delete_vote(db: AsyncSession, vote_id: int):
    await db.execute(delete(Vote).where(Vote.id == vote_id))
    await db.commit()
