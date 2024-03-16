from typing import Annotated
from fastapi import APIRouter, Depends
from views import ResumeAddView, ResumeGetView, UserAddView, UserGetView
from repository import ResumesRepository, UserRepository
User_router = APIRouter(
    prefix='/adduser',
    tags=['Пользователи']
)

@User_router.post("")
async def add_user(user: Annotated[UserAddView, Depends()]):
    user_name = await UserRepository.add_one(user)
    return {
        "Выполнено: ": "Успешно",
        'Имя: ': user_name
    }
    
    
@User_router.get("")
async def get_user() -> list[UserGetView]:
    users_list = await UserRepository.find_all()
    return users_list


Resume_router = APIRouter(
    prefix='/addresume',
    tags=['Резюме']
)

@Resume_router.post("")
async def add_resume(resume: Annotated[ResumeAddView, Depends()]):
    resume_text = await ResumesRepository.add_one(resume)
    return {
        "Выполнено: ": "Успешно",
        'Текст: ': resume_text
    }
@Resume_router.get("")
async def get_resume() -> list[ResumeGetView]:
    resume_list = await ResumesRepository.find_all()
    return resume_list