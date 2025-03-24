from pydantic import BaseModel, EmailStr

class Chat(BaseModel):
    name: str
    user_id: str

class Message(BaseModel):
    chat_id: str
    message: str

class SignUpUser(BaseModel):
    email: str
    password: str
    username: str

class LogInUser(BaseModel):
    email: str
    password: str