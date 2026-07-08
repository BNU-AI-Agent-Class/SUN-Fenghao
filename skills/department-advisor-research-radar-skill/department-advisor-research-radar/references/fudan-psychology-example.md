# Example Case: Fudan Psychology Faculty Recon

Use this example to understand how the skill should behave on a real academic department.

## Input Shape

```md
School: 复旦大学
Department / Program / Major: 社会发展与公共政策学院 心理学系
Country: China

Goal:
- 梳理心理学系全部教师的最新公开研究方向
- 不只看官网简介，而是优先看近 3-5 年公开证据
- 输出中文 Markdown，服务于导师筛选和院系研究画像理解

Official faculty list URL:
- https://ssdpp.fudan.edu.cn/xlxx_21379/list.htm

Inclusion rule:
- 以该页面列出的全部教师为底表

Evidence window:
- last 3-5 years

Preferred output path:
- fudan_psychology_faculty_research_report.md

Special notes:
- 官网教师页较旧，只作 roster anchor 和身份确认
- 当前研究方向要由近年论文、学术主页、学院新闻等校正
```

## What Good Execution Looks Like

### 1. Base Roster First

Start from the official roster page even if it is stale.
Do not replace the roster with names discovered from secondary sites.

### 2. Current Research Direction Is Evidence-Based

For each faculty member:
- keep the official profile as baseline wording
- search for recent papers and recent public academic activity
- decide whether the official direction is still accurate, too broad, or outdated

### 3. Outputs Must Separate "Official Direction" From "Current-Direction Synthesis"

That separation is important.
In the Fudan case, several faculty pages were old, but newer papers and school news gave a more accurate picture of active research topics.

## Example Findings Pattern

### Chen Binbin

Strong recent evidence showed active work around:
- family systems
- child and adolescent development
- parental burnout
- sibling relationships
- internalizing and externalizing problems

This is better than stopping at a broad label like "developmental psychology."

### Chen Kan

Recent public publication evidence was sparse.
The best defensible summary stayed broad:
- Jungian / analytical psychology
- sandplay
- expressive arts therapy
- child psychotherapy

The correct move was to keep the summary cautious rather than pretending there was strong recent publication evidence.

### Wang Yan

Recent evidence showed clear topic expansion beyond a generic family-psychology label:
- parenting and intimate relationships
- partner control behavior
- consumer psychology
- AI product psychology

This is a good example of why the skill should prioritize recent papers and school news over stale homepage text.

## Output Features Worth Reusing

The Fudan report worked well because it consistently included:
- method section
- source-priority explanation
- one section per faculty member
- explicit "current-direction synthesis"
- keywords
- representative recent evidence
- source URLs
- caveats where evidence was sparse

## Reusable Lesson

The biggest insight from this case:

An outdated official faculty page does not mean the roster is unusable.
It often still works well as the identity anchor, while the actual current research direction must be reconstructed from newer public evidence elsewhere.
