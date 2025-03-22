import os
from dotenv import load_dotenv
from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from firebase.firebase import auth
from firebase.firestore import users_collection
import jwt
import datetime

load_dotenv()
ALGORITHM = os.getenv("AUTH_ALGORITHM")
SECRET_WORD = os.getenv("AUTH_SECRET_KEY")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="LogIn")


def create_token(user):
    time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    request = {"sub": user, "exp": time}
    token = jwt.encode(request, SECRET_WORD, algorithm=ALGORITHM)
    return token


def create_new_user(email, password, username):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        doc_ref = users_collection.document()
        doc_ref.set({"id": doc_ref.id, "email": email, "username": username})

        token = create_token(user["localId"])

        response = JSONResponse(
            content={"token": token},
            status_code=200
            )
        response.set_cookie(key="session", value=token, httponly=True, secure=True)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def create_user_session(email: str, password: str):
    try:
        user = auth.sign_in_with_email_and_password(email, password)

        token = create_token(user["localId"])

        response = JSONResponse(
            content={"token": token},
            status_code=200
            )
        response.set_cookie(key="session", value=token, httponly=True, secure=True)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
def validate_token(request: Request):
    token = request.cookies.get("session")
    if not token:
        raise HTTPException(status_code=400, detail="request no authorized")
    try:
        decoded_token = jwt.decode(token, SECRET_WORD, algorithms=ALGORITHM)
        return decoded_token
    except:
        pass
