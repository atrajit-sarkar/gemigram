#  Termux Version:
# import requests
# import json
# from config import GEMENI_API_KEY

# GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMENI_API_KEY}"

# def convert_to_gemini_format(history):
#     return {
#         "contents": [
#             {
#                 "role": m["role"],  # must be "user" or "model"
#                 "parts": [{"text": m["content"]}]
#             }
#             for m in history
#         ]
#     }

# def get_gemini_response(history):
#     headers = {"Content-Type": "application/json"}
#     payload = convert_to_gemini_format(history)

#     response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))

#     if response.status_code == 200:
#         result = response.json()
#         try:
#             return result['candidates'][0]['content']['parts'][0]['text']
#         except (KeyError, IndexError):
#             return "Failed to parse response from Gemini."
#     else:
#         return f"Error {response.status_code}: {response.text}"

# EC2 Version:
import google.generativeai as genai
from config import GEMENI_API_KEY

genai.configure(api_key=GEMENI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def convert_to_gemini_format(history):
    return [
        {
            "role": m["role"],
            "parts": [{"text": m["content"]}]
        }
        for m in history
    ]

def get_gemini_response(history):
    formatted = convert_to_gemini_format(history)
    response = model.generate_content(formatted)
    return response.text

def detect_image_intent(user_text, history):
    """
    Detects if the user wants to generate an image based on the text and history.
    Returns "IMAGE" or "TEXT".
    """
    # Convert history to text for the prompt
    history_text = "\n".join([f"{m['role']}: {m['content']}" for m in history[-5:]]) # Last 5 messages for context
    
    with open("prompts/intent_prompt.txt", "r") as f:
        prompt_template = f.read()
        
    prompt = prompt_template.format(history_text=history_text, user_text=user_text)
    
    response = model.generate_content(prompt)
    return response.text.strip().upper()

def generate_nano_banana_prompt(user_text, history):
    """
    Generates a detailed 'Nano Banana' image prompt based on the user's request.
    """
    # Convert history to text for the prompt
    history_text = "\n".join([f"{m['role']}: {m['content']}" for m in history[-5:]])
    
    with open("prompts/nano_banana_prompt.txt", "r") as f:
        prompt_template = f.read()
        
    prompt = prompt_template.format(history_text=history_text, user_text=user_text)
    
    response = model.generate_content(prompt)
    return response.text.strip()