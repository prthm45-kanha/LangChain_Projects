import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

models = [
    "gemini-1.5-flash", 
    "gemini-1.5-flash-latest", 
    "gemini-pro", 
    "gemini-1.0-pro",
    "gemini-1.5-flash-001"
]

for m in models:
    try:
        print(f"Testing {m}...")
        model = init_chat_model(m, model_provider="google_genai")
        response = model.invoke("hi")
        print(f"Success with {m}: {response.content}")
        break
    except Exception as e:
        print(f"Failed {m}: {e}")
