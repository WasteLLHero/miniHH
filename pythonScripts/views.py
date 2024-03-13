from pydantic import BaseModel, ConfigDict


class UserAddView(BaseModel):
    name: str
    surname: str
    last_name: str
    phone: int
    
class UserGetView(UserAddView):
    id: int
    model_config = ConfigDict(from_attributes=True)