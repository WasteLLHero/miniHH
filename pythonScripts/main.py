from db_settings import *
from fastapi import FastAPI
from contextlib import asynccontextmanager
from models import create_tables, delete_tables
from router import User_router, Resume_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print('Соединение установлено!')
    yield
    print('Close connections')


app = FastAPI(lifespan=lifespan)

app.include_router(User_router)
app.include_router(Resume_router)
