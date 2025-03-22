from fastapi import FastAPI
from auth.auth import create_new_user, create_user_session, create_token
from schemas.models import SignUpUser, LogInUser
from fastapi.responses import JSONResponse
from routes import chat, chatbot

app = FastAPI(
    description="Made by Mantequilla, feel free to let me know problems "
)

@app.post("/SignUp", tags=["Authentication"])
async def create_user(user_data: SignUpUser):
    email = user_data.email
    password = user_data.password
    username = user_data.username
    token = create_new_user(
            email,
            password,
            username
        )
    return token

@app.post("/LogIn", tags=["Authentication"])
async def create_session(user_data: LogInUser):
    email = user_data.email
    password = user_data.password
    token = create_user_session(
        email, 
        password
        )
    return token


app.include_router(chat.router)
app.include_router(chatbot.router)