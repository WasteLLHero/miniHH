from pydantic import BaseModel, ConfigDict


class UserAddView(BaseModel):
    name: str
    surname: str
    last_name: str
    phone: int
    
class UserGetView(UserAddView):
    id: int
    model_config = ConfigDict(from_attributes=True)
    

class ResumeAddView(BaseModel):
    user_id: int
    text: str
    
class ResumeGetView(ResumeAddView):
    id: int
    model_config = ConfigDict(from_attributes=True)