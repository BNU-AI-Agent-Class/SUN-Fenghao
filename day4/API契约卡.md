# API 契约卡

## `POST /api/auth/login`

请求：

```json
{"username": "course_demo_2026", "password": "***"}
```

成功返回普通用户身份和 bearer token。token 只保存在浏览器本地存储，不写进仓库或 PPT。

## `POST /api/chat`

请求头：`Authorization: Bearer <token>`

```json
{
  "conversation_id": null,
  "message": "今天宿舍的人都睡了，我有点孤单，只想说说。"
}
```

响应核心字段：

```json
{
  "conversation_id": "conv_...",
  "message_id": "msg_...",
  "reply": "自然语言完整回复",
  "segments": ["第一段", "第二段"],
  "ui_status": "",
  "state_update": {
    "relationship_stage_judge": "A",
    "safety_level": "green",
    "risk_flags": []
  },
  "tool_statuses": [],
  "context_budget": {}
}
```

## `GET /api/chat/history`

- 需要登录。
- 可传 `conversation_id` 和 `limit`。
- 返回持久化消息及 `segments/tool_statuses`，刷新页面后仍按分段显示。

## `GET /api/health`

无需登录，成功返回：

```json
{"status": "ok"}
```

## 失败约定

- `401`：token 失效，前端清理本地身份并回登录页。
- 超时/网络错误：前端写入本地兜底消息，不显示堆栈；兜底始终包含 12356、110、120。
- 危机：接口仍返回标准 ChatResponse，但 `safety_level=red`，最终文字由后端确定性护栏保证。
