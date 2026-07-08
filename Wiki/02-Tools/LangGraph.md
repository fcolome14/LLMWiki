---
tags: [tool]
---

# LangGraph

Graph-based framework for building multi-agent/multi-step LLM workflows. Nodes = steps (LLM calls, tool calls, human checkpoints), edges = control flow (including conditional branching).

## Why we use it
- Explicit state machine — easier to reason about than free-form agent loops
- Native support for **human-in-the-loop** checkpoints (important for [[KYC Automation]] approval gates)
- Works well with [[PydanticAI]] for typed node inputs/outputs

## Gotchas
- Set a `recursion_limit` — see [[ReAct Pattern]] failure modes
- State schema changes require care once you have persisted checkpoints in Postgres

## Related
- [[Agent Orchestration]]
- [[LangSmith]] — for tracing graph runs
- [[Investor Onboarding System]]
