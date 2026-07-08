---
name: department-advisor-research-radar
description: 当用户想调研某个学校、院系、专业、实验室集群或学科方向下全部老师/导师/教师的最新研究方向时使用，尤其适用于“不要只看官网”“看近3-5年真实研究主题”“整理成Markdown报告”“为申请/套磁/导师筛选做院系画像”等请求。 Use when the user wants a reproducible, evidence-based investigation of all faculty members in a specific university, department, major, lab cluster, or discipline, focused on each person's latest research directions rather than stale profile text. Triggers on requests to survey all teachers/advisors in a target unit, verify current research themes across multiple public sources, and produce a structured Markdown report for graduate application targeting, advisor selection, or academic landscape review.
---

# Department Advisor Research Radar

## Overview

This skill turns a one-off faculty survey into a repeatable multi-source research workflow.
Use it when the user wants the latest research directions for all teachers in a target school/program, not just official homepage summaries.

The core output is a Markdown report with:
- a verified faculty list
- per-faculty research direction summaries grounded in recent evidence
- source links
- explicit confidence notes when evidence is weak, stale, or conflicting

## Quick Start

Collect these inputs first:
- school name
- school/department/program/major name
- faculty list page or the best official entry page
- desired output path if the user has one
- optional year window, default `last 3-5 years`

If the user has not supplied an official roster page, find one before profiling individuals.
Do not start from scattered names unless the user explicitly wants a partial sample.

## Workflow

### Step 1: Lock The Scope

Define the survey boundary clearly:
- exact institution
- exact department, institute, or program
- whether to include only tenure-track faculty or also lecturers, researchers, postdocs, adjuncts, clinicians
- whether the output is for graduate application, advisor matching, landscape review, or general background research

If scope is ambiguous, prefer the official faculty directory for the named unit.

### Step 2: Build The Base Roster

Use the official faculty directory as the base table.
Capture for each person when available:
- Chinese name and English name
- title / role
- email
- official profile URL
- lab or center affiliation

The official page is the identity anchor, but not the final authority on current research direction.

If the directory looks stale, still use it as the baseline roster unless there is a newer official roster elsewhere in the same institution.

### Step 3: Investigate Each Faculty Member

For each person, gather evidence from multiple public sources, prioritizing recency and author identity certainty.

Always look beyond the official profile:
- recent papers
- scholar profiles
- ORCID
- lab pages
- society pages
- conference pages
- recent school news about publications, grants, talks, or projects
- interviews or public lectures when these reveal active themes

When a name is common, identity-match carefully using:
- institution
- department
- coauthors
- topic consistency
- email domain
- profile photo or CV if available

Do not attribute papers to a faculty member unless identity confidence is reasonably strong.

### Step 4: Infer Current Research Directions

The goal is not to list every topic ever mentioned.
Infer the faculty member's current research directions from the best recent evidence.

Give strongest weight to:
- papers from the last 3-5 years
- active projects or grants
- recent school news or lab updates
- recent talks or conference participation

Give lower weight to:
- stale official profile text
- old book translations
- generic directory blurbs
- low-quality aggregator pages

Your summary should answer:
- What does this person appear to be actively studying now?
- What older topics are still background only?
- Is the public evidence rich, mixed, or sparse?

### Step 5: Write The Report

Write the final report in Markdown.
Use the report pattern in [references/report-format.md](references/report-format.md).

The report should include:
- method note
- source priority note
- faculty roster source
- optional admissions context if relevant
- one section per faculty member

For each faculty member include:
- identity block
- official direction
- current-direction synthesis
- keywords
- representative recent evidence
- caution note if the evidence is stale or ambiguous
- source list

### Step 6: Handle Weak Evidence Explicitly

When public evidence is weak, do not overclaim.
Use language like:
- "Public evidence in the last 3 years is sparse."
- "Current direction is inferred mainly from older official materials."
- "This appears more practice-oriented than publication-heavy."
- "Recruitment status should be confirmed through current admissions notices or direct email."

The skill is successful when it is honest, not when every profile looks equally complete.

## Evidence Rules

Follow [references/source-priority.md](references/source-priority.md) for ranking sources and handling conflicts.

Default evidence order:
1. recent papers / journal pages / DOI-backed records
2. ORCID / Google Scholar / institutional repositories / lab pages
3. school news about publications, grants, awards, talks, or projects
4. official faculty page
5. external aggregators such as X-MOL, ResearchGate, AMiner, Baidu Xueshu
6. media, interviews, lecture blurbs, conference speaker pages

Never let a weak source override a stronger recent source without explanation.

## Output Standard

The final report should optimize for decision usefulness, not exhaustiveness.
That means:
- summarize research directions, not just dump citations
- keep the evidence traceable
- separate current themes from legacy themes
- surface uncertainty clearly

Use the reusable templates in:
- [assets/department_advisor_research_radar_input_template.md](assets/department_advisor_research_radar_input_template.md)
- [assets/department_advisor_research_radar_report_template.md](assets/department_advisor_research_radar_report_template.md)
- [references/fudan-psychology-example.md](references/fudan-psychology-example.md)

## Common Failure Modes

Avoid these mistakes:
- treating the official profile as the final answer
- confusing roster freshness with research freshness
- mapping publications to the wrong person with the same name
- overusing one aggregator instead of triangulating
- inferring admissions eligibility from research activity alone
- turning sparse evidence into fake specificity

## Trigger Examples

This skill should trigger on requests like:
- "帮我调研某个学校某个专业所有老师最近在做什么研究"
- "做一个院系老师研究方向全景，重点看近几年，不要只看官网"
- "把这个学院所有导师的最新研究方向整理成 Markdown"
- "帮我筛一个专业的 faculty，按最近研究主题做画像"

## Notes

When the user wants current information, browse and verify with live sources.
When a report will influence school applications, advisor selection, or major decisions, prefer stronger evidence and clearer caveats over faster completion.
