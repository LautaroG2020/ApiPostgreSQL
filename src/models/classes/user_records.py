from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    user_name: str
    user_email: str
    user_password: str

class NewUserRequest(BaseModel):
    user_name: str
    user_email: str
    user_password: str