from sqlalchemy import select
from db_settings import new_session
from models import User
from views import UserAddView, UserGetView

class UserRepository:
    @classmethod
    async def add_one(cls, data: UserAddView) -> str:
        async with new_session() as session:
            user_dict = data.model_dump()
            
            add_user_session = User(**user_dict)
            session.add(add_user_session)
            await session.flush()
            await session.commit()
            return add_user_session.name
    @classmethod
    async def find_all(cls) -> list[UserGetView]:
        async with new_session() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()    
            user_schemas = [UserGetView.model_validate(user_model) for user_model in user_models]
            return user_schemas