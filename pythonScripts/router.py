from typing import Annotated
from fastapi import APIRouter, Depends
from views import UserAddView, UserGetView
from repository import UserRepository
router = APIRouter(
    prefix='/adduser',
    tags=['Пользователи']
)

@router.post("")
async def add_user(user: Annotated[UserAddView, Depends()]):
    user_name = await UserRepository.add_one(user)
    return {
        "Выполнено: ": "Успешно",
        'Имя: ': user_name
    }
    
    
@router.get("")
async def get_user() -> list[UserGetView]:
    users_list = await UserRepository.find_all()
    return users_list