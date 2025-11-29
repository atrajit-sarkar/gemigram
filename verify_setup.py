import os
import time
from db_manager import add_message, get_history, clear_history
from gemini_client import detect_image_intent, generate_nano_banana_prompt

def test_firestore():
    print("Testing Firestore...")
    chat_id = "test_user_123"
    
    # Clear existing history
    clear_history(chat_id)
    
    # Add message
    msg = {"role": "user", "content": "Hello Firestore"}
    add_message(chat_id, msg)
    print("Added message.")
    
    # Get history
    history = get_history(chat_id)
    print(f"Retrieved history: {history}")
    
    if len(history) == 1 and history[0]["content"] == "Hello Firestore":
        print("Firestore test PASSED.")
    else:
        print("Firestore test FAILED.")

def test_gemini_logic():
    print("\nTesting Gemini Logic...")
    history = [{"role": "user", "content": "Hello"}]
    
    # Test Intent Detection
    text_intent = detect_image_intent("How are you?", history)
    print(f"Intent for 'How are you?': {text_intent}")
    
    image_intent = detect_image_intent("Draw a futuristic city", history)
    print(f"Intent for 'Draw a futuristic city': {image_intent}")
    
    if text_intent == "TEXT" and image_intent == "IMAGE":
        print("Intent detection PASSED.")
    else:
        print("Intent detection FAILED.")
        
    # Test Prompt Generation
    if image_intent == "IMAGE":
        prompt = generate_nano_banana_prompt("Draw a futuristic city", history)
        print(f"Generated Prompt: {prompt[:100]}...")
        if len(prompt) > 10:
            print("Prompt generation PASSED.")
        else:
            print("Prompt generation FAILED.")

if __name__ == "__main__":
    try:
        test_firestore()
        test_gemini_logic()
    except Exception as e:
        print(f"Verification failed with error: {e}")
