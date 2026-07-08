---
tags: [agent-pattern, concept]
---

# ReAct Pattern

Short for **Reason + Act**. The agent alternates between:

1. **Thought** — reasoning about what to do next
2. **Action** — calling a tool or taking a step
3. **Observation** — reading the result and looping back to step 1

Used heavily inside [[LangGraph]] nodes, where each node can represent one reasoning step and edges control the loop/branching logic.

## Related
- [[Agent Orchestration]]
- [[Tool Calling]]
- [[Agent Evaluation]]

## Notes
- Works well for tasks needing multi-step lookups (e.g. checking a document, then deciding on a compliance action).
- Failure mode: the agent can loop indefinitely without a hard iteration cap — worth setting `recursion_limit` in LangGraph.
