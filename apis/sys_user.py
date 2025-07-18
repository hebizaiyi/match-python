from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import SessionLocal as AsyncSessionLocal
import crud.sys_user as crud
import schema.user as schema

router = APIRouter()
# 依赖注入
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# 创建用户
@router.post("/user/")
async def create_user(user: schema.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db=db,user=user)