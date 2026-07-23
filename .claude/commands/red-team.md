---
description: Run an adversarial pass on the agent via the red-team subagent
argument-hint: [specific section or concern — omit for a full pass]
---

Use the `red-team` subagent to attack the agent. Focus (if any): $ARGUMENTS

Delegate the full adversarial pass to the red-team agent (fresh context,
read-only). When its report comes back:

1. Present the findings as-is — do not soften severities.
2. For each attack, privilege, or contract finding, propose a concrete fix
   and where it lands (a prompt or contract edit, a manifest reduction, a
   new eval, or a decisions/ file if it changes architecture).
3. Ask which fixes to apply before editing anything.
