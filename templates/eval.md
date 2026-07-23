---
status: planned     # planned | running | done | abandoned
updated: YYYY-MM-DD
---

# Eval: <what is being tested, vs what>

**Question:** <what this eval decides, and the decision or claim it serves.>

## Provenance

Fill before marking done. A result without its provenance is not a result.
(check-provenance.py verifies these fields on every `done` eval.)

| Item | Value |
|---|---|
| model | <exact model ID + version> |
| prompt_version | <git commit hash of agents/<name>/ used; for system evals, of the repo> |
| dataset | <datasets/<slug> + version from its SOURCE.md> |
| temperature | <and any other sampling params> |
| n | <runs per condition> |
| tools/deps | <tool + dependency versions that matter> |

```bash
# exact command to reproduce
```

## Plan

<Conditions compared, metric and how it's scored (rubric, exact-match,
LLM-judge + judge model/version), and what result would change what decision.
State the strongest reason this eval might not answer its own question.>

## Results

<All runs, not the best run. n and variance, not bare point estimates.
Discarded runs listed with reasons. Failure cases worth reading verbatim get
quoted here or linked from evals/artifacts/.>

## Conclusion

<What this settles, what it doesn't, and the follow-up it implies.>
