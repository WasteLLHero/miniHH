from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

database_url = "postgresql+asyncpg://postgres:@localhost/miniHH"
engine = create_async_engine(database_url, echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)