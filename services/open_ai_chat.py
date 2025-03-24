from firebase.firestore import chats_collection
from helpers.openai_client import openai_client

def open_ai_request(chat_id: str, user_message: str, dependencies: dict) -> dict:
    chat = chats_collection.document(chat_id)
    doc = chat.get()

    if not doc.exists:
        return {"error": f"ERROR: There is no chatbot with this ID ({chat_id})"}

    chat_data = doc.to_dict()
    user_id = chat_data.get("user_id")

    if dependencies["sub"] != user_id:
        return {"error": "This chat does not belong to you"}

    history = chat_data.get("history", [])
    history.append({"role": "user", "content": user_message})
    open_ai_request = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that can answer questions and help with tasks." ## Prompt Engineering
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.5, # Que tan creativo es el modelo
        max_tokens=600, ## Cantidad de palabras/silabas que se van a generar por el model 
        top_p=1, ## El modelo va a tener en cuenta el 100% de las palabras/silabas que se le dan
        n=3, ## Cantidad de respuestas que se van a generar
        user="yahir.ponce@softtek.com" # Para poder hacer un seguimiento de las respuestas
    )

    open_ai_response = open_ai_request.choices[0].message.content
    history.append({"role": "assistant", "content": open_ai_response})
    chat.update({"history": history})
    return  open_ai_response