---
tags: [compliance]
---

# KYC Automation

Automating KYC/PBC checks as part of the [[Investor Onboarding System]].

## Pipeline stages
1. Document intake (ID, proof of address, source of funds)
2. Validation via Claude Vision — extract fields, cross-check against submitted form data
3. Risk classification (capital call type, jurisdiction flags)
4. **Human approval gate** — nothing auto-approves; agent recommends, human confirms
5. Daily audit log — every decision + evidence trail stored for MiFID II / GDPR review

## Related
- [[Agent Orchestration]] — supervisor pattern routes between validation/classification agents
- [[Agent Evaluation]] — groundedness matters a lot here (no hallucinated field extraction)
- [[LangSmith]] — trace storage doubles as part of the audit trail

## Open risk
- Data privacy: traces contain PII, so retention policy on LangSmith/logs needs to match GDPR requirements.
