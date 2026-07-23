---
description: Scaffold the agent — copy templates/agent/ to agents/<name>/ and set up prompt, tools, and contract
argument-hint: <name> <one-line purpose>
---

Create the agent: $ARGUMENTS

Use the `prompt-authoring` skill for the content/shell/contract rules, then:

1. Copy `templates/agent/` to `agents/<name>/` (name: lowercase-with-hyphens).
2. Draft `system-prompt.md` from the stated purpose — provider-agnostic
   content only.
3. Fill `tools.md` with only the tools the purpose justifies; every row gets
   a real justification and a risk note. Push back if a requested tool
   exceeds the purpose.
4. Draft `contract.md`: inputs, output guarantees, declared failure shape,
   non-goals. This is the only thing other agents may depend on — write it
   like they will.
5. Fill `shell.md` with the pinned model and params; note that tool schemas
   point at their definitions in `src/`.
6. Flag next steps: the injection-resistance eval this agent needs before
   it ships (`/new-eval`), and a `/red-team` pass once the prompt
   stabilizes.
