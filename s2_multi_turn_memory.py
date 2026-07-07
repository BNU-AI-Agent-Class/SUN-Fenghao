from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# s2：多轮聊天 + 记忆。
# 目标：messages 变成对话历史，模型可以看到前面的上下文。

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("DAY1_OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
model = os.getenv("DAY1_MODEL", "deepseek/deepseek-v4-pro")
base_url = os.getenv("DAY1_BASE_URL", "https://openrouter.ai/api/v1")

messages = [
    {"role": "system", "content": "You are a concise and patient Chinese assistant."}
]

client = OpenAI(api_key=api_key, base_url=base_url)

while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() in {"exit", "quit"} or user_input.strip() == "退出":
        print("Exited.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model=model, messages=messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}")

client.close()
