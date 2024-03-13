from sqlalchemy import BigInteger, Column, String, Integer
from sqlalchemy.orm import DeclarativeBase
from db_settings import engine
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"
    id = Column(Integer , autoincrement=True, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    last_name = Column(String)
    phone = Column(BigInteger, unique=True)


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
        
async def delete_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)