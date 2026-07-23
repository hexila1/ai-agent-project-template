#!/usr/bin/env python3
"""check-provenance.py — the one check you can't do by eye.

1. Every eval in evals/ with `status: done` pins its reproducibility fields:
   model, prompt_version, dataset, temperature, n.
2. Every datasets/<slug>/ directory carries a SOURCE.md.
3. No obvious secret patterns anywhere in tracked text files.

Exit 0 = clean, exit 1 = problems (listed on stdout).
Run directly, via /check-provenance, or automatically by the pre-commit hook.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
problems: list[str] = []

# --- 1. eval provenance -----------------------------------------------------
REQUIRED_PINS = ("model", "prompt_version", "dataset", "temperature", "n")
evals = root / "evals"
if evals.exists():
    eval_files = [f for f in sorted(evals.rglob("*.md"))
                  if "artifacts" not in f.parts]
    for f in eval_files:
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^status:\s*(\w+)", text, re.MULTILINE)
        status = m.group(1) if m else None
        if status != "done":
            continue
        for pin in REQUIRED_PINS:
            # a pin counts if it appears as `pin:` or `| pin |` with a
            # non-empty, non-placeholder value on the same line
            pat = re.compile(
                rf"(?:^{pin}\s*:|\|\s*{pin}\s*\|)\s*([^|\n]*)",
                re.MULTILINE | re.IGNORECASE,
            )
            hit = pat.search(text)
            val = hit.group(1).strip() if hit else ""
            if not val or val.startswith("<") or val.upper() == "TODO":
                problems.append(
                    f"{f.relative_to(root)}: status is done but '{pin}' is not pinned"
                )

# --- 1b. agent completeness & topology registration -------------------------
REQUIRED_AGENT_FILES = ("system-prompt.md", "tools.md", "contract.md")
agents_dir = root / "agents"
topology = root / "orchestration" / "topology.md"
topo_text = topology.read_text(encoding="utf-8") if topology.exists() else None
agent_names = []
if agents_dir.exists():
    for d in sorted(p for p in agents_dir.iterdir() if p.is_dir()):
        agent_names.append(d.name)
        for req in REQUIRED_AGENT_FILES:
            if not (d / req).exists():
                problems.append(f"agents/{d.name}/: missing {req}")
        if topo_text is not None and d.name not in topo_text:
            problems.append(
                f"agents/{d.name}/: not registered in orchestration/topology.md"
            )
if topo_text is not None:
    # topology must not reference agents that don't exist
    import re as _re
    for m in _re.finditer(r"agents/([\w-]+)/contract\.md", topo_text):
        if m.group(1) not in agent_names and m.group(1) != "<name>":
            problems.append(
                f"orchestration/topology.md: references agents/{m.group(1)}/ "
                "which does not exist"
            )

# --- 2. dataset provenance ---------------------------------------------------
datasets = root / "datasets"
if datasets.exists():
    for d in sorted(p for p in datasets.iterdir() if p.is_dir()):
        if not (d / "SOURCE.md").exists():
            problems.append(f"datasets/{d.name}/: missing SOURCE.md")

# --- 3. secret scan ----------------------------------------------------------
SECRET_PATTERNS = [
    (re.compile(r"sk-ant-[A-Za-z0-9\-_]{20,}"), "Anthropic API key"),
    (re.compile(r"\bsk-[A-Za-z0-9]{32,}"), "API secret key"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key"),
    (re.compile(r"\bghp_[A-Za-z0-9]{36}\b"), "GitHub token"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}"), "Slack token"),
    (re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----"), "private key"),
]
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
TEXT_SUFFIXES = {".md", ".py", ".ts", ".js", ".json", ".yaml", ".yml",
                 ".toml", ".txt", ".sh", ".env", ".tex", ".csv"}

for f in root.rglob("*"):
    if not f.is_file() or f.suffix not in TEXT_SUFFIXES:
        continue
    if any(part in SKIP_DIRS for part in f.parts):
        continue
    if f.name == ".env.example" or f.name == Path(__file__).name:
        continue
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        continue
    for pat, label in SECRET_PATTERNS:
        if pat.search(text):
            problems.append(
                f"{f.relative_to(root)}: possible {label} committed — "
                "move it to the environment"
            )

# ------------------------------------------------------------------------------
if problems:
    print("\n".join(problems))
    print(f"\ncheck-provenance: {len(problems)} problem(s)")
    sys.exit(1)

print("check-provenance: clean")
sys.exit(0)
