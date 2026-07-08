---
tags: [tool]
---

# PydanticAI

Agent framework built on Pydantic, giving structured/typed outputs and tool schemas by default. Reduces the "LLM returned malformed JSON" class of bugs.

## Why we use it
- Type-safe tool definitions — pairs naturally with [[Tool Calling]]
- Validation errors surface immediately rather than downstream
- Plays well with FastAPI models already used in the fund's backend

## Related
- [[LangGraph]] — often used together, PydanticAI for typed nodes/tools inside a LangGraph flow
- [[Agent Evaluation]]
