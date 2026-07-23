---
description: Verify eval pins, agent-folder completeness, dataset SOURCE.md files, and absence of committed secrets
allowed-tools: Bash(python3 check-provenance.py)
---

Run the project provenance check from the repository root:

```
python3 check-provenance.py
```

Then:

1. If it exits 0, confirm all `done` evals are pinned, all datasets have
   SOURCE.md, and no secret patterns were found.
2. If it exits 1, address each finding: complete the agent folder, fill
   missing pins with the values *actually used* (never invent one — if the true value is unknown, the
   eval's status goes back to `running` or its results are marked
   UNVERIFIED), add the missing SOURCE.md, or move the secret to `.env` and
   rotate it.
3. Never "fix" a failure by deleting the eval or dataset without asking.
