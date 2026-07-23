#!/usr/bin/env bash
# Claude Code PreToolUse hook: block `git commit` while provenance or secret
# problems exist (missing eval pins, missing dataset SOURCE.md, committed keys).
#
# Wired in .claude/settings.json (matcher: Bash). Exit 2 blocks the tool call
# and returns stderr to Claude so it can fix the problem and retry.
#
# Enforcement for commits made *outside* Claude Code (your own terminal):
#   ln -s ../../.claude/hooks/pre-commit.sh .git/hooks/pre-commit
# When run as a git hook there is no JSON on stdin, so it just runs the check.

set -u
root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"

if [ -t 0 ]; then
  cmd="git commit"   # invoked as a plain git pre-commit hook
else
  input=$(cat)
  cmd=$(printf '%s' "$input" | python3 -c \
    "import json,sys; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" \
    2>/dev/null || echo "git commit")
fi

case "$cmd" in
  *"git commit"*)
    if ! out=$(python3 "$root/check-provenance.py" 2>&1); then
      {
        echo "Commit blocked by check-provenance:"
        echo "$out"
        echo "Pin the missing eval fields, add the dataset SOURCE.md, or move the secret to .env — never fill a pin with a value that isn't the one actually used."
      } >&2
      exit 2
    fi
    ;;
esac
exit 0
