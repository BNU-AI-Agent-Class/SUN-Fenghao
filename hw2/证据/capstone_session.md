# Capstone 完整过程记录

测试时间：2026-07-15  
初始数据：两条笔记，均没有标签。

## 用户任务

> `hw2_demo` 的 `stats` 在没有标签时会崩。请不要直接猜答案：先运行命令复现，再搜索和读取相关代码，说明根因，做最小修改，最后重新运行 `stats` 验证。

## Agent 过程

1. 调用 `search(keyword="stats", path="hw2_demo")`，定位到 README、TODO、日志、`cli.py`。
2. 调用 `read_file` 读取 `cli.py`、`analyze.py` 和 `store.py`。
3. 调用：

```text
cd hw2_demo && python -m notes_app.cli stats
```

实际返回码为 1，堆栈落在：

```text
top_tag = counts[0][0]
IndexError: list index out of range
```

4. Agent 判断：`tag_counts()` 在没有标签时返回空列表，`summary()` 无条件读取 `counts[0]`。
5. 调用 `write_file` 修改 `analyze.py`：有标签时沿用原逻辑；无标签时输出“还没有任何标签”。
6. 重新运行无标签场景，返回码 0。
7. 新增一条带 `#bug #fix` 的笔记，验证有标签场景仍正常。
8. 删除该笔记，再次验证回到无标签场景仍正常。

模型第一次总结时在 JSON 字符串中直接放了英文双引号，解析器没有误把它当最终结果，而是要求重发合法 JSON。第二次返回：

> bug 修好了。`analyze.py` 的 `summary()` 现在会先检查 `counts` 是否为空：空时输出“还没有任何标签”，不再抛 `IndexError`。已测试无标签、有标签、删除标签后恢复无标签三种场景，均正常运行。

## 我怎么看

最像真 Claude Code 的地方，是它没有直接改代码，而是先搜索、读调用链、运行看到真实堆栈，再做最小修改和回归测试。最不像的地方，是手写 JSON 仍会因为引号失误，需要 harness 帮它纠错；真实工具调用协议会更稳。

