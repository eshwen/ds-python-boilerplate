#!/usr/bin/env bash
# Claude Code PreToolUse hook: before a Bash `git commit`, run pre-commit (on staged files) and pytest.
# Exit code 2 blocks the commit and feeds stderr back to Claude.

cmd=$(jq -r '.tool_input.command // ""')
if ! grep -Eq '(^|[;&|([:space:]])git([[:space:]]+-C[[:space:]]+[^[:space:]]+)?[[:space:]]+commit([[:space:]]|$)' <<<"$cmd"; then
    exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

if ! out=$(uv run pre-commit run 2>&1); then
    echo "Commit blocked: pre-commit hooks failed. Fix the issues (and re-stage any files the hooks modified), then commit again." >&2
    tail -n 60 <<<"$out" >&2
    exit 2
fi

if ! out=$(uv run pytest -q 2>&1); then
    echo "Commit blocked: pytest failed. Fix the failing tests (or coverage), then commit again." >&2
    tail -n 60 <<<"$out" >&2
    exit 2
fi

exit 0
