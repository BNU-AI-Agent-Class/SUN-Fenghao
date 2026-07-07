from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# s0：最小 API 调用。
# 目标：读取 .env，创建客户端，发送一次固定请求。

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("DAY1_OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
model = os.getenv("DAY1_MODEL", "deepseek/deepseek-v4-pro")
base_url = os.getenv("DAY1_BASE_URL", "https://openrouter.ai/api/v1")

messages = [
    {"role": "system", "content": "You are a concise Chinese assistant."},
    {"role": "user", "content": "Please explain in one Chinese sentence: what does a minimal Agent framework need?"},
]

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(model=model, messages=messages)
reply = response.choices[0].message.content
print(reply)
client.close()
