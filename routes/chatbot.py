from fastapi import APIRouter, HTTPException
from schemas.models import Message
from services.open_ai_chat import open_ai_request

router = APIRouter()

@router.post("/{chat_id}", tags=["Bot"])
def chat_with_bot(chat_id: str, message_content: Message):
    response = open_ai_request(chat_id, message_content.message)
    if response is None:
        raise HTTPException(status_code=404, detail="chat not found")
    return {"response": response}