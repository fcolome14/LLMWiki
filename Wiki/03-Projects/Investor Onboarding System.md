---
tags: [project, compliance]
---

# Investor Onboarding System

The fund's end-to-end automation for investor intake, replacing manual review.

## Components
- Document validation (Claude Vision) — see [[KYC Automation]]
- Classification agent — routes capital calls by type/jurisdiction
- Orchestration layer — built on [[LangGraph]], typed nodes via [[PydanticAI]]
- Tracing/audit — [[LangSmith]]
- Human-in-the-loop approval before anything is finalized

## Status
- CI/CD pipeline live (GitHub Actions, compliance gates)
- Copier-based scaffolding for new agent modules
- Next: CLAUDE.md compliance rules + template scaffolding refinements

## Related
- [[Agent Orchestration]]
- [[KYC Automation]]
- [[Agent Evaluation]]
