import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import SystemMessage

load_dotenv()
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

@tool
def get_weather(location: str) -> str:
    """Get the weather at a location"""
    return f"It's sunny in {location}"

model_with_tools = model.bind_tools([get_weather])

messages = [
    SystemMessage(content="You are a helpful assistant with access to real-time tools. Use the tool results to answer the user's questions confidently without apologizing."),
    {"role":"user","content":"What is the weather like in Edinburgh?"}
]
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    tool_result = get_weather.invoke(tool_call)
    messages.append(tool_result)

final_response = model_with_tools.invoke(messages)
print("CONTENT:", final_response.content)
