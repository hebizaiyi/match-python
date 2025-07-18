from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.sys_user import User
import schema.user as schema

# 创建用户
async def create_user(db: AsyncSession, user: scheams.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

