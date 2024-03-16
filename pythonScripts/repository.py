from sqlalchemy import select
from db_settings import new_session
from models import Resume, User
from views import ResumeGetView, ResumeAddView, UserAddView, UserGetView

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


class ResumesRepository:
    @classmethod
    async def add_one(cls, data: ResumeAddView):
        async with new_session() as session:
            resume_dict = data.model_dump()
            add_resume_session = Resume(**resume_dict)
            session.add(add_resume_session)
            await session.flush()
            await session.commit()
            return add_resume_session.text
    @classmethod
    async def find_all(cls) -> list[ResumeGetView]:
        async with new_session() as session:
            query = select(Resume)
            result = await session.execute(query)
            resume_models = result.scalars().all()    
            resume_schemas = [ResumeGetView.model_validate(resume_model) for resume_model in resume_models]
            return resume_schemas