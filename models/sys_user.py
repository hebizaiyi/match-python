from sqlalchemy import Column, Integer, String, Boolean
from db.session import Base

class User(Base):
    __tablename__ = "sys_user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)