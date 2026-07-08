# 院系导师研究方向雷达

[English Version](./README.en.md)

`department-advisor-research-radar` 是一个可复用的 Codex/Claude 风格 skill，用来调研某个大学、院系、专业或学科方向下全部教师/导师的最新公开研究方向。

它特别适合这种场景：官网教师页还能拿来确认名单和身份，但内容已经偏旧，真正想知道的是“这些老师最近几年到底在做什么研究”。

这个 skill 的核心思路不是照抄官网简介，而是综合多源公开证据进行校正，包括：
- 近 3-5 年论文与期刊页
- ORCID / Google Scholar / 实验室主页
- 学院新闻、论著报道、讲座和项目页面
- 必要时参考 X-MOL、ResearchGate、AMiner、百度学术等二级聚合源

## 它能产出什么

这个 skill 目标是生成一份结构化 Markdown 报告，包含：
- 已核实的教师 roster
- 每位老师一段基于证据的“当前研究方向画像”
- 关键研究关键词
- 代表性近年证据
- 信息不足时的明确保守提示
- 可追溯的来源链接

## 为什么这个 skill 有价值

很多院系官网并不是“完全没用”，而是：
- 适合做 roster anchor 和身份确认
- 不适合直接当成“当前研究方向”的最终结论

这个 skill 把更稳妥的流程固定下来：
先用官网锁定边界和名单，再用更新、更强的一手公开证据去重建每位老师当前真正活跃的研究主题。

## Quick Start

最快的使用方式只有三步：

1. 安装这个 skill。
2. 给出学校、院系/专业，以及官方教师名单入口。
3. 明确要求“不要只看官网，优先看近 3-5 年公开证据，并输出 Markdown 报告”。

如果你只是想立刻试一次，可以直接复制下面这段：

```text
帮我调研某个学校某个专业全部老师最近的研究方向。
请以官网教师名单做底表，但不要只看官网简介，优先参考近 3-5 年论文、Google Scholar、ORCID、学院新闻、项目和公开讲座。
最后输出成中文 Markdown 报告。
```

## Installation

### 安装到 Codex

把整个 skill 目录复制到：

```text
C:\Users\ASUS\.codex\skills\department-advisor-research-radar
```

### 安装到 Claude Code

把整个 skill 目录复制到：

```text
C:\Users\ASUS\.claude\skills\department-advisor-research-radar
```

### 用打包文件安装/分发

如果你更喜欢分发打包文件，可以直接使用：

```text
dist/department-advisor-research-radar.skill
```

## Example Prompt Gallery

下面这些请求都很适合触发这个 skill：

```text
帮我调研北京大学心理学系全部老师最近 3-5 年的研究方向，输出中文 Markdown。
```

```text
我想申请某个项目，先帮我把这个院系所有导师的当前研究主题摸一遍，不要只看官网。
```

```text
请把这个专业所有老师按当前研究方向做画像，优先看近年论文、Google Scholar、ORCID 和学院新闻。
```

```text
帮我做一个院系 research landscape，看看这些老师现在分别集中在哪些研究主题上。
```

## 仓库结构

```text
department-advisor-research-radar/
  SKILL.md
  assets/
  references/
dist/
  department-advisor-research-radar.skill
```

## 仓库内容

- `department-advisor-research-radar/SKILL.md`
  核心 skill 定义、触发条件与执行工作流

- `department-advisor-research-radar/references/source-priority.md`
  信息源优先级、冲突处理与弱证据处理规则

- `department-advisor-research-radar/references/report-format.md`
  最终 Markdown 报告格式规范

- `department-advisor-research-radar/references/fudan-psychology-example.md`
  复旦大学心理学系案例，用来展示这个 skill 在真实院系上的执行方式

- `department-advisor-research-radar/assets/department_advisor_research_radar_input_template.md`
  可复用输入模板

- `department-advisor-research-radar/assets/department_advisor_research_radar_report_template.md`
  可复用输出模板

- `dist/department-advisor-research-radar.skill`
  已打包好的 skill 文件，可直接分发或安装

## 适用场景

- 调研某个学校某个专业全部老师最近的研究方向
- 做申请季导师筛选或套磁前的信息整理
- 理解一个院系内部的研究主题分布
- 用近年公开证据修正官网过旧的教师画像

## 使用说明

### 给人使用

如果你是手动使用这个 skill，建议按下面的方式准备输入：

1. 先明确目标范围。
   例如：学校、院系/专业、是否要全量教师、输出语言。

2. 准备一个官方教师名单入口。
   最好是院系官网的 faculty page、教师目录页、导师名单页。

3. 明确调研目标。
   例如：
   - 申请前筛选导师
   - 了解某个专业整体研究版图
   - 核对老师近几年真实研究方向

4. 明确你希望 agent 优先看的证据。
   例如：
   - 近 3-5 年论文
   - Google Scholar / ORCID
   - 学院新闻、项目、讲座
   - 不要只看官网简介

5. 要求输出成 Markdown 报告。
   这样最适合后续继续精筛、批注或二次整理。

你可以直接参考这个输入模板：
- [department_advisor_research_radar_input_template.md](C:/Users/ASUS/Documents/Codex/2026-05-25/https-chatgpt-com-share-e-6a14381a/department-advisor-research-radar/assets/department_advisor_research_radar_input_template.md)

一个典型提问方式是：

```text
帮我调研复旦大学社会发展与公共政策学院心理学系全部老师最近的研究方向。
不要只看官网，优先看近 3-5 年论文、Google Scholar、ORCID、学院新闻和公开讲座。
最后整理成中文 Markdown 报告。
```

### 给 Agent 使用

如果你是把这个 skill 装给另一个 agent，用法可以非常简单：

1. 把 skill 安装到对应 agent 的 skills 目录。
2. 在用户请求涉及“院系全量导师调研”“最新研究方向”“不要只看官网”“整理为 Markdown 报告”时触发它。
3. 按 `SKILL.md` 的工作流执行：
   - 先锁定范围
   - 再拿官方 roster
   - 再逐个老师做多源证据调研
   - 最后生成结构化 Markdown
4. 弱证据场景下保持保守，不要过度推断。

对 agent 来说，最重要的触发关键词通常是：
- 某学校/某院系/某专业所有老师
- 最新研究方向
- 不要只看官网
- 近 3-5 年论文
- 导师筛选 / 套磁 / 申请前调研
- Markdown 报告

如果用户只想了解单个老师，这个 skill 也可以用，但它最擅长的是“一个院系/专业的全量调研”。

## 重新校验与打包

如果你本地也有 skill-creator 工具链，可以这样重新校验和打包：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\ASUS\.agents\skills\skill-creator-0.1.0\scripts\quick_validate.py .\department-advisor-research-radar
python C:\Users\ASUS\.agents\skills\skill-creator-0.1.0\scripts\package_skill.py .\department-advisor-research-radar .\dist
```

## 使用提醒

- 这个 skill 做的是“公开证据下的当前研究方向重建”，不是招生承诺判断。
- 是否当年招生、是否收推免/直博/RA，仍应以最新招生通知或老师回复为准。

## License

本仓库当前采用 [MIT License](./LICENSE)。
