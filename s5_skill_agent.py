from pathlib import Path
import os
import subprocess

from dotenv import load_dotenv
from openai import OpenAI


# s5：领域 Skill Agent。
# 目标：agent.md 是行动规则，skill.md 是领域技能。

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("DAY1_OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
model = os.getenv("DAY1_MODEL", "deepseek/deepseek-v4-pro")
base_url = os.getenv("DAY1_BASE_URL", "https://openrouter.ai/api/v1")

agent_rules = (BASE_DIR / "agent.md").read_text(encoding="utf-8")
skill_rules = (BASE_DIR / "skill.md").read_text(encoding="utf-8")
system_prompt = agent_rules + "\n\n" + skill_rules

messages = [{"role": "system", "content": system_prompt}]
client = OpenAI(api_key=api_key, base_url=base_url)


def is_dangerous_command(command):
    """教学演示用的极简安全检查。"""
    dangerous_words = [
        "del ",
        "erase ",
        "remove-item",
        "rm ",
        "rmdir ",
        "format ",
        "shutdown",
        "restart-computer",
        "reg delete",
    ]
    lower_command = command.lower()
    return any(word in lower_command for word in dangerous_words)


def run_shell_command(command):
    """执行 shell 命令，并尽量正确解码中文输出。"""
    completed = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        timeout=30,
    )
    output_bytes = completed.stdout + completed.stderr

    for encoding in ("utf-8", "gbk"):
        try:
            output = output_bytes.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        output = output_bytes.decode("utf-8", errors="replace")

    if completed.returncode != 0:
        output = f"命令返回码：{completed.returncode}\n{output}"

    return output


while True:
    user_input = input("\nYou: ")
    if user_input.strip().lower() in {"exit", "quit"} or user_input.strip() == "退出":
        print("Exited.")
        break

    messages.append({"role": "user", "content": user_input})

    while True:
        response = client.chat.completions.create(model=model, messages=messages)
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"[AI] {reply}")

        cleaned_reply = reply.strip()
        if cleaned_reply.startswith("完成:"):
            break

        if not cleaned_reply.startswith("命令:"):
            messages.append({
                "role": "user",
                "content": "Format error. Please reply only with 命令:XXX or 完成:XXX.",
            })
            continue

        command = cleaned_reply.split("命令:", 1)[1].strip()

        if is_dangerous_command(command):
            result = f"Command blocked for safety: {command}"
            print(f"[System] {result}")
            messages.append({"role": "user", "content": f"执行完毕:{result}"})
            continue

        confirm = input(f"[Confirm command] {command}\nRun it? y/N: ").strip().lower()
        if confirm != "y":
            result = f"User refused to run command: {command}"
            print(f"[System] {result}")
            messages.append({"role": "user", "content": f"执行完毕:{result}"})
            continue

        # 原版教学代码常写 result = os.popen(command).read()：
        # os.popen(command) 会把 command 字符串交给操作系统 shell 执行，
        # .read() 会读取命令输出。但是 Windows 上它常按 GBK 解码，
        # 读取 UTF-8 中文文件时可能报 UnicodeDecodeError。
        # 所以这里用 subprocess 先拿到原始字节，再尝试 utf-8/gbk 解码。
        result = run_shell_command(command)
        print(f"[System] {result}")
        messages.append({"role": "user", "content": f"执行完毕:{result}"})

client.close()
