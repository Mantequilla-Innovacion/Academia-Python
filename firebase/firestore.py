import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase/mantequilla-python-firebase-adminsdk-fbsvc-02f3c40f1f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

chats_collection = db.collection("chats")
users_collection = db.collection("users")

