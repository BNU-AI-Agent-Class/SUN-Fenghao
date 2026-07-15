# Day3 证据索引

## 当前版本真实测试

- `run_live_eval.py`：可复现的线上测试脚本；账号密码只从环境变量读取。
- `live_eval_before_crisis_guard.json`：2026-07-15 修复前的 13 条服务器原始响应。
- `live_eval_raw.json`：部署确定性危机护栏后，用相同输入重跑的 13 条原始响应。
- 后端自动化测试：`python -m pytest 13_backend_api/tests -q`，结果为 `23 passed`。

## 第一版研究证据

- 数据源：第一版启明形成的 177 份匿名用户摘要（P0001–P0177）。
- 用途：只用于 DEFINE 的需求和失败模式归纳，不宣称是当前版本的效果数据。
- 隐私：作业仓库不复制原始聊天和身份目录，只保留聚合结论；公开展示不含姓名、手机号、学校、城市等可识别信息。

## 真实故障证据

- 2026-07-14 聊天记录暴露了三类问题：工具路径猜错后停止探索、对上下文参数进行无依据推断、畸形 JSON 暴露给前端。
- 相应回归测试包括：
  - `test_tool_loop_can_recover_after_wrong_memory_path`
  - `test_singleton_array_c0_executes_tool_instead_of_leaking_json`
  - `test_malformed_protocol_payload_is_never_exposed_as_reply`
  - `test_crisis_guard_overrides_immediate_self_harm_reply`
  - `test_crisis_guard_blocks_harm_to_others`

原始研究数据不进入 GitHub，避免把课程展示变成隐私泄漏。
