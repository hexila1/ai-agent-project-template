---
description: Scaffold evals/<slug>.md from the template and pressure-test the plan
argument-hint: <slug> <what's being compared or tested>
---

Set up a new eval: $ARGUMENTS

Use the `eval-design` skill for metric, judge, dataset, and n choices, then:

1. Create `evals/<agent>/<slug>.md` from `templates/eval.md`, status
   `planned` (the per-agent subfolder keeps slugs collision-free if this
   project later merges into a multi-agent system). Slug names the
   comparison: `prompt-v3-vs-v2.md`, not `test1.md`.
2. Fill the plan: conditions, metric and scoring method (if LLM-judge, pin
   the judge model too), and the decision the result will inform.
3. Leave provenance pins as explicit placeholders to fill before running —
   the pre-commit hook blocks `done` evals with unpinned fields.
4. Pressure-test before handing back: name the decision the result will
   change (if no result would change anything, say the eval isn't worth
   running), then state the strongest reason it might not answer its own
   question — contaminated dataset, judge bias (never judge with the model
   under test; pin the judge's version), n too small for a comparative
   claim, metric that rewards the wrong thing — and propose the fix in the
   plan itself.
