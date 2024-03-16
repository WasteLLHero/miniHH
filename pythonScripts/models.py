from sqlalchemy import BigInteger, Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from db_settings import engine
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer , autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    last_name = Column(String)
    phone = Column(BigInteger, unique=True)
        
class Resume(Base):
    __tablename__ = "Resumes"
    id = Column(Integer , autoincrement=True, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey("Users.id"))    
    
async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        
async def delete_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        