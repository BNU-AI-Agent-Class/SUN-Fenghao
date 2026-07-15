# Day4：启明 Agent 开发与部署

## 公网入口

- 用户端：[https://dream.qimingbot.com](https://dream.qimingbot.com)
- 健康检查：[https://dream.qimingbot.com/api/health](https://dream.qimingbot.com/api/health)
- 演示账号：`course_demo_2026`
- 演示密码：`QimingDemo2026!`

这是权限受限的普通用户账号，不含管理权限、API key 或服务器权限。

## 里程碑

| 里程碑 | 当前实现 | 证据 |
|---|---|---|
| M1 后端 | FastAPI `/api/chat`、登录鉴权、确定性危机入口/出口 | 23 个自动化测试；Day3 线上红队 |
| M2 前端 | Vue/PWA 聊天页、分段消息、常驻紧急求助、网络失败兜底 | `证据/crisis-help-*.png` |
| M3 前端上线 | Caddy 托管静态构建产物 | 公网 URL 手机可开 |
| M4 后端上线 | Ubuntu systemd 运行 FastAPI，Caddy 反向代理 `/api/*` | `/api/health` 返回 `ok` |
| M5 联调 | 同源 HTTPS、登录后一轮完整聊天、8 条危机测试 | `day3/证据/live_eval_raw.json` |

老师的样例使用 GitHub Pages + Railway；本项目使用自己的 Linux 服务器和域名。平台不同，但静态托管、后端环境变量、HTTPS、健康检查、危机护栏和手机验收一项不少。

## 文件导航

- [技术架构卡](技术架构卡.md)
- [API 契约卡](API契约卡.md)
- [部署选型](部署选型决策卡.md)
- [密钥环境变量](密钥环境变量清单.md)
- [上线检查](上线检查清单.md)
- [结项技术文档](结项技术文档.md)
- [录屏脚本](演示录屏脚本.md)
- [源码与证据说明](证据/README.md)

## 小组分工

孙凤豪负责架构、开发、部署和主要评估（75%）；魏哲煊负责提示词风格复核、部分测试话术与结果复核（25%）。
