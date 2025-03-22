from fastapi import APIRouter, HTTPException, Depends
from schemas.models import Chat
from firebase.firestore import chats_collection
from auth.auth import validate_token

router = APIRouter()

@router.post("/chat", tags=["Chat"], dependencies=[Depends(validate_token)])
def create_chat(chat: Chat):
    doc_ref = chats_collection.document()
    doc_ref.set({"id": doc_ref.id, "name": chat.name, "history": []})
    return {"id": doc_ref.id, "name": chat.name, "history": []}

@router.get("/chats", tags=["Chat"], dependencies=[Depends(validate_token)])
def get_all_chats():
    docs = chats_collection.stream()
    chat_list = []

    for doc in docs:
        data = doc.to_dict()
        chat_list.append(data)

    return {"chats": chat_list}

@router.delete("/chat/{chat_id}", tags=["Chat"], dependencies=[Depends(validate_token)])
def delete_chat(chat_id: str):
    doc = chats_collection.document(chat_id)
    if not doc.get().exists:
        raise HTTPException(status_code=404, detail="chat not found")
    doc.delete()
    return {"message": "Chat deleted Successfully"}

@router.put("/chat/{chat_id}", tags=["Chat"], dependencies=[Depends(validate_token)])
def update_chat(chat_id: str, chat: Chat):
    doc = chats_collection.document(chat_id)
    if not doc.get().exists:
        raise HTTPException(status_code=404, detail="chat not found")
    doc.update({"name": chat.name})
    return {"message": "Chat name updated Successfully"}

@router.get("/chat/{chat_id}", tags=["Chat"], dependencies=[Depends(validate_token)])
def get_chat(chat_id: str):
    doc = chats_collection.document(chat_id)
    chat = doc.get()
    if not chat.exists:
        raise HTTPException(status_code=404, detail="chat not found")
    return chat.to_dict()