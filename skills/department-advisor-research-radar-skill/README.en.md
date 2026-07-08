# Department Advisor Research Radar

[中文版](./README.md)

`department-advisor-research-radar` is a reusable Codex/Claude-style skill for investigating the latest public research directions of all faculty members or advisors in a target university department, program, major, or discipline cluster.

It is especially useful when official faculty pages are still good enough for roster and identity verification, but too stale to answer the real question: what is each faculty member actively working on in recent years?

Instead of copying faculty bios, this skill triangulates across multiple public evidence sources, including:
- papers and journal pages from the last 3-5 years
- ORCID / Google Scholar / lab pages
- school news, publication highlights, talks, and project pages
- secondary aggregators such as X-MOL, ResearchGate, AMiner, and Baidu Scholar when needed

## What It Produces

The skill is designed to generate a structured Markdown report with:
- a verified faculty roster
- one evidence-based current research profile per faculty member
- research keywords
- representative recent evidence
- explicit caution notes when evidence is sparse
- traceable source links

## Why This Skill Exists

Many department websites are not useless, just limited:
- they are often still good roster anchors
- they are often not reliable as the final authority on current research direction

This skill formalizes a better workflow:
use the official site to lock scope and identity, then reconstruct each faculty member's current active topics from newer and stronger public evidence.

## Quick Start

The fastest way to use this skill is:

1. Install the skill.
2. Provide the school, department/program, and an official faculty-list entry page.
3. Explicitly ask for recent multi-source evidence and a Markdown report.

If you want to test it immediately, you can start with:

```text
Help me investigate the latest research directions of all faculty members in a target department.
Use the official faculty roster as the base table, but do not rely only on official bios.
Prioritize papers from the last 3-5 years, Google Scholar, ORCID, school news, grants, and public talks.
Return the final result as a Markdown report.
```

## Installation

### Install for Codex

Copy the skill directory to:

```text
C:\Users\ASUS\.codex\skills\department-advisor-research-radar
```

### Install for Claude Code

Copy the skill directory to:

```text
C:\Users\ASUS\.claude\skills\department-advisor-research-radar
```

### Install or distribute via packaged artifact

You can also use the packaged artifact directly:

```text
dist/department-advisor-research-radar.skill
```

## Example Prompt Gallery

These requests are strong matches for this skill:

```text
Help me map the latest research directions of all faculty members in the Department of Psychology at Peking University. Output the result in Markdown.
```

```text
I am preparing graduate applications. Please investigate the current research themes of all advisors in this department, and do not rely only on the official website.
```

```text
Profile all faculty members in this program based on recent papers, Google Scholar, ORCID, and school news.
```

```text
Build a department-level research landscape report showing what each faculty member appears to be actively studying now.
```

## Repository Structure

```text
department-advisor-research-radar/
  SKILL.md
  assets/
  references/
dist/
  department-advisor-research-radar.skill
```

## Repository Contents

- `department-advisor-research-radar/SKILL.md`
  Core skill definition, trigger conditions, and execution workflow

- `department-advisor-research-radar/references/source-priority.md`
  Evidence ranking, conflict handling, and sparse-evidence rules

- `department-advisor-research-radar/references/report-format.md`
  Final Markdown report format

- `department-advisor-research-radar/references/fudan-psychology-example.md`
  A real example based on Fudan University psychology faculty mapping

- `department-advisor-research-radar/assets/department_advisor_research_radar_input_template.md`
  Reusable input template

- `department-advisor-research-radar/assets/department_advisor_research_radar_report_template.md`
  Reusable output template

- `dist/department-advisor-research-radar.skill`
  Packaged skill artifact ready for sharing or installation

## Use Cases

- Survey all faculty members in a department and map their latest research directions
- Build an advisor-targeting report for graduate applications
- Understand topic clusters within a program
- Update stale official faculty profiles with recent public evidence

## Usage Guide

### For Humans

If you want to use this skill manually, prepare the request like this:

1. Define the scope clearly.
   For example: school, department/program, whether you want all faculty members, and output language.

2. Provide an official faculty-list entry point.
   The best input is usually a department faculty page, teacher directory, or advisor roster page.

3. State the research goal.
   For example:
   - advisor screening before applications
   - understanding the research landscape of a program
   - verifying what faculty members are actually working on in recent years

4. Specify preferred evidence sources.
   For example:
   - papers from the last 3-5 years
   - Google Scholar / ORCID
   - school news, grants, talks, and projects
   - do not rely on official bios alone

5. Ask for a Markdown report.
   That format is easiest to review, annotate, and refine later.

You can start from this template:
- [department_advisor_research_radar_input_template.md](C:/Users/ASUS/Documents/Codex/2026-05-25/https-chatgpt-com-share-e-6a14381a/department-advisor-research-radar/assets/department_advisor_research_radar_input_template.md)

A typical request looks like:

```text
Help me investigate the latest research directions of all faculty members in the Department of Psychology,
School of Social Development and Public Policy, Fudan University.
Do not rely only on the official website. Prioritize papers from the last 3-5 years, Google Scholar, ORCID,
school news, and public talks. Produce the final result as a Markdown report.
```

### For Agents

If you are installing this skill for another agent, the usage pattern is simple:

1. Install the skill into the target agent's skills directory.
2. Trigger it when the request involves full-department faculty research mapping, current research directions, multi-source verification, or Markdown reporting.
3. Follow the workflow in `SKILL.md`:
   - lock the scope
   - build the official roster
   - investigate each faculty member with multi-source evidence
   - generate a structured Markdown report
4. Stay conservative when evidence is sparse or ambiguous.

For agent triggering, the most useful signals are:
- all teachers/advisors in a school, department, or program
- latest research directions
- do not rely only on the official website
- papers from the last 3-5 years
- advisor screening / outreach / application research
- Markdown report

This skill can still be used for a single faculty member, but it is strongest when used for a full department or program-wide investigation.

## Revalidate And Repackage

If you have the local skill-creator toolchain, you can rebuild with:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\ASUS\.agents\skills\skill-creator-0.1.0\scripts\quick_validate.py .\department-advisor-research-radar
python C:\Users\ASUS\.agents\skills\skill-creator-0.1.0\scripts\package_skill.py .\department-advisor-research-radar .\dist
```

## Notes

- This skill reconstructs current research directions from public evidence; it does not guarantee recruitment status.
- For admissions-related decisions, always verify current recruiting status through official notices or direct faculty contact.

## License

This repository is currently released under the [MIT License](./LICENSE).
