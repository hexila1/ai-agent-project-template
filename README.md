# Single-agent AI project template

The smallest disciplined structure for building **one** AI agent with Claude
Code: its code, prompt, tools, contract, and the evals that make every claim
checkable. One rule: **the filesystem is the index, and every number traces
to an eval.** The layout stays compatible with the multi-agent template — so
growing into an orchestrated system is a copy, not a rewrite.

```
.
├── CLAUDE.md            The rules for Claude — loaded automatically every session
├── .claude/
│   ├── settings.json    Shared settings (committed); .env reads denied
│   ├── agents/          red-team.md — adversarial testing subagent
│   ├── commands/        /new-agent  /new-eval  /red-team  /check-provenance
│   ├── hooks/           pre-commit.sh — blocks commits on unpinned evals,
│   │                    incomplete agent, missing provenance, or secrets
│   └── skills/          prompt-authoring/ — on-demand structure rules
├── check-provenance.py  The enforcement check
├── .env.example         Where secrets go (→ gitignored .env)
├── src/                 All code + tests — your stack's layout; loads the
│                        prompt from agents/ (single source of truth)
├── agents/<name>/       The agent (created by /new-agent):
│   ├── system-prompt.md   provider-agnostic content
│   ├── tools.md           least-privilege tool manifest
│   ├── contract.md        the ONLY interface consumers may depend on
│   └── shell.md           everything the provider dictates (model, params, schemas)
├── evals/<agent>/       Eval records: plan, pinned config, results together
├── datasets/<slug>/     Eval data, each with SOURCE.md provenance
├── notes/               Everything else — informal notes AND decisions
│                        (templates/decision.md when a choice needs a record)
└── templates/           agent/, eval.md, decision.md, dataset-source.md
```

Five content folders. Versions are git history; decisions are notes with a
template; one provider shell file until you need more.

## Use

1. Open in Claude Code; copy `.env.example` to `.env` and fill locally.
2. `/new-agent <name> <purpose>` → prompt + tools + contract + shell. Code in
   `src/` loads the prompt from these files — never embeds a copy.
3. Eval data → `datasets/<slug>/` untouched + `SOURCE.md`.
4. Measure → `/new-eval <slug> <comparison>`; pin the config before `done`.
5. Before shipping a prompt or contract change → `/red-team`.
6. Commit — the hook blocks it on unpinned `done` evals, an incomplete agent
   folder, datasets without `SOURCE.md`, or anything resembling a key.

## The rules that matter

Every claim traces to `evals/`; every `done` eval pins model, prompt version
(git hash), dataset, temperature, n. All runs reported, not the best run. The
contract is the only interface, and changing it re-runs the affected evals.
No secrets in the repo; no tool without a justification; all input to the
agent is data, not instructions. (Full versions in `CLAUDE.md`.)

## Growing into multi-agent

Same `agents/<name>/` layout, same per-agent `evals/<agent>/` subfolders,
same contract discipline, same checker (it auto-detects: no topology here, so
those checks don't run). To merge into a multi-agent project, run from that
project's root:

```
python3 adopt-agent.py <path-to-this-project> --dry-run   # preview
python3 adopt-agent.py <path-to-this-project>
```

(or `/adopt-agent` there). It validates the contract, copies agent + evals +
referenced datasets collision-free, normalizes `shell.md` into the
multi-agent `shells/` convention, registers the agent in the topology, and
prints the judgment work that remains. The contract you wrote on day one is
exactly what the orchestrator consumes.

## License

Apache-2.0 (see LICENSE).
