import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key starts with: {api_key[:5] if api_key else 'None'}")

client = genai.Client(api_key=api_key)

try:
    for m in client.models.list():
        print(m.name)
except Exception as e:
    print(f"ListModels failed: {e}")
