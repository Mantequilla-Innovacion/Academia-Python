import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

cred = credentials.Certificate(os.getenv("FIRE_STORE_PATH_CRED"))
firebase_admin.initialize_app(cred)
db = firestore.client()

chats_collection = db.collection("chats")
users_collection = db.collection("users")

