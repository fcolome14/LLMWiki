---
tags: [agent-pattern, concept]
---

# Agent Orchestration

The layer that decides which agent/tool runs next, how state is passed between them, and when the workflow terminates.

## Common orchestration styles
- **Supervisor pattern** — one controller agent routes tasks to specialist agents
- **Graph-based** — explicit nodes/edges define flow ([[LangGraph]] uses this)
- **Sequential chains** — simplest form, no branching

## Related
- [[LangGraph]]
- [[ReAct Pattern]]
- [[Investor Onboarding System]] — real-world use case combining document validation, classification, and human approval gates

## Open questions
- How to handle partial failures mid-graph (retry vs escalate to human-in-the-loop)?
- Determinism: same input should ideally produce the same routing decision — see [[Agent Evaluation]].
