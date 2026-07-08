---
tags: [agent-pattern, concept]
---

# Agent Evaluation

How to measure whether an agent/graph is behaving correctly — especially important in regulated contexts where outputs need to be auditable.

## Dimensions
- **Correctness** — did it reach the right final answer/classification?
- **Groundedness** — did it hallucinate, or was every claim backed by a retrieved document?
- **Determinism** — same input, same output? (temperature, tool ordering, retries all affect this)
- **Latency/cost** — especially relevant for daily audit runs

## Tooling
- [[LangSmith]] — tracing and eval runs
- [[Tool Calling]] — logs of which tools were invoked and with what arguments

## Related
- [[Agent Orchestration]]
- [[KYC Automation]]
