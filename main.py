from fastapi import FastAPI, Depends
from auth.auth import create_new_user, create_user_session, validate_token, destroy_user_session
from schemas.models import SignUpUser, LogInUser
from routes import chat, chatbot

app = FastAPI(
    description="Made by Mantequilla. Feel free to let me know if you encounter any problems."
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

@app.delete("/LogOut", tags=["Authentication"])
async def destroy_session():
     return destroy_user_session()

app.include_router(chat.router)
app.include_router(chatbot.router)