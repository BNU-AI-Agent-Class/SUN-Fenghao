# Agent 作业运行说明

建议按下面顺序逐个运行，每次只关注本版本新增了什么能力。

## 运行顺序

```powershell
python s0_min_api.py
python s1_single_turn.py
python s2_multi_turn_memory.py
python s3_agent_loop.py
python s4_prompt_file.py
python s5_skill_agent.py
```

退出交互程序时，可以输入：

```text
退出
```

也可以输入：

```text
exit
```

## 每个版本看什么

### s0_min_api.py

只做一次固定请求。重点看：

- `.env` 怎么被读取。
- `OpenAI(api_key=..., base_url=...)` 怎么创建客户端。
- `messages` 怎么发给模型。

### s1_single_turn.py

用户输入一次，模型回答一次。重点看：

- `input()` 负责接收用户输入。
- 这一步没有历史，所以模型不会记住上一轮。

### s2_multi_turn_memory.py

加入外层 `while True` 和 `messages.append()`。重点看：

- 用户消息 append 到 `messages`。
- 模型回复也 append 到 `messages`。
- 因为上下文一直保留，所以可以追问。

### s3_agent_loop.py

加入 Agent 循环。重点看：

- 外层循环：等待用户给新任务。
- 内层循环：Agent 自己决定下一步。
- `命令:XXX`：模型请求程序执行 shell 命令。
- `完成:XXX`：模型宣布本次任务结束。
- 程序会先拦截明显危险的命令；普通命令也会询问 `Run it? y/N`，输入 `y` 才真正执行。

教学原理可以先理解成：

```python
result = os.popen(command).read()
```

含义：

- `command` 是模型给出的命令字符串，比如 `dir`。
- `os.popen(command)` 把这个字符串交给操作系统 shell 执行。
- `.read()` 读取 shell 命令打印出来的文本。
- `result` 不是“要执行的命令”，而是“命令执行后的输出结果”。

不过 Windows 读取 UTF-8 中文文件时，`os.popen(...).read()` 可能按 GBK 解码而报错。
所以当前代码实际使用 `subprocess.run(...)`：

```python
result = run_shell_command(command)
```

它先拿到命令输出的原始字节，再尝试用 UTF-8 和 GBK 解码，稳定性更好。

然后程序把结果追加回 `messages`：

```python
messages.append({"role": "user", "content": f"执行完毕:{result}"})
```

这一步的意思是：把工具执行结果反馈给模型，让模型继续判断下一步。

### s4_prompt_file.py

把系统规则放进 `agent.md`。重点看：

- Python 主程序基本不变。
- 改 Agent 行为时，可以先改 `agent.md`。
- 命令执行部分仍然和 `s3` 一样，只是规则从文件读取。

### s5_skill_agent.py

加入 `skill.md`。重点看：

- `agent.md` 是行动规则。
- `skill.md` 是领域能力和回答风格。
- 换一个 `skill.md`，同一个框架就能变成另一个专业 Agent。

## 环境变量说明

真实 key 放在 `.env`，不要上传 GitHub。

本作业脚本优先读取：

```env
DAY1_OPENROUTER_API_KEY=...
```

同时保留：

```env
OPENROUTER_API_KEY=...
```

这是为了兼容老师原来的 `s3_agent.py`。

`.env.example` 可以上传 GitHub，因为里面没有真实 key。
