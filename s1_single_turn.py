from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# s1：单轮聊天。
# 目标：用户输入一次，模型回复一次。这里还没有对话历史。

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("DAY1_OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
model = os.getenv("DAY1_MODEL", "deepseek/deepseek-v4-pro")
base_url = os.getenv("DAY1_BASE_URL", "https://openrouter.ai/api/v1")

system_prompt = "You are a concise and patient Chinese assistant."
user_input = input("You: ")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_input},
]

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(model=model, messages=messages)
reply = response.choices[0].message.content
print(f"AI: {reply}")
client.close()
