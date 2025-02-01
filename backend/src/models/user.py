from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.Base import Base
from src.db.engine import get_async_session


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=11), index=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=15), index=True, nullable=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    role_id: Mapped[int] = mapped_column(ForeignKey('role.id'), nullable=False)
    notification: Mapped[list['Notification']] = relationship(back_populates='user')
    answer: Mapped[list['Answer']] = relationship(back_populates='user')
    roles: Mapped['UserRole'] = relationship(back_populates='user')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role_id = 0


class UserRole(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(nullable=False)

    user: Mapped[list['User']] = relationship(back_populates='roles')


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)