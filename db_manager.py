import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Initialize Firestore
cred = credentials.Certificate("service.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_history(chat_id):
    """Retrieve the conversation history for a specific user from Firestore."""
    history_ref = db.collection("chats").document(str(chat_id)).collection("messages")
    # Order by timestamp
    docs = history_ref.order_by("timestamp", direction=firestore.Query.ASCENDING).stream()
    
    history = []
    for doc in docs:
        data = doc.to_dict()
        history.append({"role": data["role"], "content": data["content"]})
    
    return history

def add_message(chat_id, message):
    """Add a message to the user's conversation history in Firestore."""
    history_ref = db.collection("chats").document(str(chat_id)).collection("messages")
    
    # Add timestamp for ordering
    message["timestamp"] = firestore.SERVER_TIMESTAMP
    history_ref.add(message)

def clear_history(chat_id):
    """Clear the conversation history for a specific user in Firestore."""
    history_ref = db.collection("chats").document(str(chat_id)).collection("messages")
    docs = history_ref.stream()
    
    for doc in docs:
        doc.reference.delete()

def initialize_user_db(chat_id):
    """
    No explicit initialization needed for Firestore as collections/docs 
    are created automatically on write. Kept for compatibility.
    """
    pass