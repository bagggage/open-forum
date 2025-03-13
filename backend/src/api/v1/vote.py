from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.auth_dependencies import current_user
from src.db.engine import get_async_session
from src.service.vote import create_vote_service
from src.service.vote import get_votes_service
from src.schemas.vote import VoteCreate
from src.schemas.vote import VoteResponse
from src.models import User
from typing import List

router = APIRouter(prefix="/v1/votes", tags=["Votes"])

@router.post(
    "/",
    response_model=VoteResponse,
    summary="Create a new vote"
)
async def create_vote(
    vote_data: VoteCreate,
    db: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    vote = await create_vote_service(db, vote_data, user.id)
    return VoteResponse.from_orm(vote)

@router.get(
    "/", 
    response_model=List[VoteResponse], 
    summary="Get a list of all votes with pagination"
)
async def get_votes(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_async_session)
):
    votes = await get_votes_service(db, skip, limit)
    return [VoteResponse.from_orm(v) for v in votes]

