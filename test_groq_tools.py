import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool

load_dotenv()
model = init_chat_model("llama-3.1-8b-instant", model_provider="groq")

@tool
def get_weather(location: str) -> str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

model_with_tools = model.bind_tools([get_weather])

messages = [{"role":"user","content":"What is the weather like in Edinburgh?"}]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

try:
    final_response = model_with_tools.invoke(messages)
    print("WITH TOOLS:", final_response.content)
except Exception as e:
    print("WITH TOOLS FAILED:", e)

try:
    final_response_no_tools = model.invoke(messages)
    print("WITHOUT TOOLS:", final_response_no_tools.content)
except Exception as e:
    print("WITHOUT TOOLS FAILED:", e)
