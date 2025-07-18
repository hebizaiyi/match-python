from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    password: str

class UserCreate(UserBase):

    class Config: 
        from_attributes = True

class User(UserBase):
    id: int
    
    class Config: 
        from_attributes = True
