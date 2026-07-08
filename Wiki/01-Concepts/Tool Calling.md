---
tags: [concept]
---

# Tool Calling

The mechanism by which an LLM invokes an external function (API call, DB query, document parser) instead of just generating text.

## Key considerations
- Schema strictness — [[PydanticAI]] enforces typed inputs/outputs on tool calls, reducing malformed-argument errors
- Error handling — what happens when a tool call fails or returns unexpected data?
- Logging — every tool call should be traceable for audit purposes (see [[Agent Evaluation]])

## Related
- [[ReAct Pattern]]
- [[PydanticAI]]
- [[LangGraph]]
