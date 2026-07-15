"""Day2 作业：在 c1 工具箱上增加一个全项目搜索工具。"""
from pathlib import Path
import json
import os
import subprocess
import sys

from dotenv import load_dotenv
from openrouter import OpenRouter


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR.parent / ".env")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODEL = os.getenv("DAY1_MODEL", "google/gemini-3-flash-preview")
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules"}
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".pyc"}


def read_file(path):
    return Path(path).read_text(encoding="utf-8")


def write_file(path, text):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return f"已写入 {target}"


def bash(cmd):
    """执行用于复现和测试的普通命令，拦下明显危险操作。"""
    dangerous = ("rm ", "del ", "rmdir ", "format ", "shutdown", "remove-item")
    if any(word in cmd.lower() for word in dangerous):
        return f"命令被安全检查拦截：{cmd}"
    completed = subprocess.run(cmd, shell=True, capture_output=True, timeout=30)
    output_bytes = completed.stdout + completed.stderr
    for encoding in ("utf-8", "gbk"):
        try:
            output = output_bytes.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        output = output_bytes.decode("utf-8", errors="replace")
    return f"返回码：{completed.returncode}\n{output}".strip()


def search(keyword, path=".", max_results=50):
    """递归搜索文本，返回“文件:行号:内容”。"""
    root = Path(path)
    if not root.exists():
        return f"路径不存在：{root}"

    matches = []
    files = [root] if root.is_file() else root.rglob("*")
    for file_path in files:
        if not file_path.is_file():
            continue
        if any(part in SKIP_DIRS for part in file_path.parts):
            continue
        if file_path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            lines = file_path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(lines, start=1):
            if keyword.lower() in line.lower():
                matches.append(f"{file_path}:{line_number}: {line.strip()}")
                if len(matches) >= int(max_results):
                    return "\n".join(matches) + "\n（结果过多，已经截断）"

    return "\n".join(matches) if matches else f"没有找到：{keyword}"


TOOLS = {
    "read_file": read_file,
    "write_file": write_file,
    "search": search,
    "bash": bash,
}


SYSTEM = """你是一个编程助手。每次只回复一个 JSON，不要 markdown 包裹：
- 读文件：{"tool":"read_file","args":{"path":"..."}}
- 写文件：{"tool":"write_file","args":{"path":"...","text":"..."}}
- 搜索项目：{"tool":"search","args":{"keyword":"...","path":"..."}}
- 运行复现或测试命令：{"tool":"bash","args":{"cmd":"..."}}
- 完成：{"done":"给用户的总结"}

规则：
1. 不知道代码在哪时先 search，再 read_file，不能凭空猜。
2. 工具结果会由程序发回来；看到结果后再决定下一步。
3. 修改代码前先读原文件，修改后要运行测试或复现命令。
"""


def parse_action(text):
    """兼容模型偶尔加上的 json 代码围栏。"""
    cleaned = text.strip().strip("`").removeprefix("json").strip()
    start, end = cleaned.find("{"), cleaned.rfind("}")
    if start == -1 or end < start:
        raise ValueError("回复中没有完整 JSON")
    return json.loads(cleaned[start:end + 1])


def run_agent(client, task, max_steps=12):
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": task},
    ]
    consecutive_errors = 0

    for _ in range(max_steps):
        reply = client.chat.send(model=MODEL, messages=messages).choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"[模型] {reply}")

        try:
            action = parse_action(reply)
        except (ValueError, json.JSONDecodeError) as exc:
            consecutive_errors += 1
            messages.append({"role": "user", "content": f"JSON 格式错误：{exc}。请只重发一个合法 JSON。"})
            if consecutive_errors >= 3:
                return "连续 3 次 JSON 格式错误，本轮停止。"
            continue

        if "done" in action:
            return action["done"]

        name = action.get("tool")
        args = action.get("args", {})
        if name not in TOOLS:
            consecutive_errors += 1
            result = f"没有 {name} 这个工具。可用工具：{', '.join(TOOLS)}"
        else:
            try:
                result = TOOLS[name](**args)
                consecutive_errors = 0
            except (OSError, TypeError, ValueError) as exc:
                consecutive_errors += 1
                result = f"工具执行失败：{type(exc).__name__}: {exc}"

        print(f"[调用] {name}({args})")
        print(f"[结果]\n{result}")
        messages.append({"role": "user", "content": f"工具返回：\n{result}"})
        if consecutive_errors >= 3:
            return "连续 3 次工具错误，本轮停止。"

    return f"达到最多 {max_steps} 步，本轮停止，避免无限循环。"


def main():
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("DAY1_OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("没有找到 OPENROUTER_API_KEY")

    with OpenRouter(api_key=api_key) as client:
        while True:
            try:
                task = input("\n你：").strip()
            except EOFError:
                break
            if not task:
                continue
            if task.lower() in {"exit", "quit"} or task == "退出":
                break
            print(f"[完成] {run_agent(client, task)}")


if __name__ == "__main__":
    main()
