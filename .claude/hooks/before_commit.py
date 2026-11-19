"""PreToolUse(Bash) hook: gate git commits on pre-commit and pytest.

Fires before every Bash command. If the command creates a git commit
(`git commit …`, including compound commands like `git add … && git commit …`),
it runs the commit-time checks CLAUDE.md asks for, in order:

  1. `pre-commit run --all-files` — the repo's pre-commit hooks (ruff, uv-lock, …)
  2. `pytest` — the full test suite

The first failing step denies the commit and feeds its output back so it gets
fixed before committing (for pre-commit, a failure usually means re-staging the
files it auto-fixed and retrying). pytest only runs if pre-commit passed, so a
pre-commit failure doesn't waste a full test run. Non-commit commands,
`--dry-run`, and `-h/--help` pass straight through.

Tools are run from the in-project `.venv/bin/` if present, else via `uv run`.
"""

import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

# Chars of a failing step's output to surface (tail — the summary lives there).
_OUTPUT_TAIL = 4000
_PRECOMMIT_TIMEOUT = 540
_PYTEST_TIMEOUT = 300
# Shell operators that separate one command from the next.
_SEPARATORS = {"&&", "||", "|", ";", "&", "(", ")"}
# Commit flags that mean the command doesn't actually create a commit.
_SKIP_ARGS = {"--dry-run", "--help", "-h"}


def _repo_root() -> Path:
    """Project root — `CLAUDE_PROJECT_DIR` when the harness sets it, else cwd."""
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())


def _command_segments(command: str) -> list[list[str]]:
    """Split a shell command into per-command token lists, respecting quotes.

    Uses shlex's punctuation parsing so shell operators (`&&`, `;`, `|`, …)
    split commands even when glued to a token (`foo; git commit`), while quoted
    text (`echo "git commit"`) stays intact and is never seen as an operator.
    """
    lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
    lexer.whitespace_split = True
    try:
        tokens = list(lexer)
    except ValueError:
        return []  # Unbalanced quotes etc. — treat as non-commit (git's own hook is the backstop).
    segments: list[list[str]] = []
    current: list[str] = []
    for tok in tokens:
        if tok in _SEPARATORS:
            if current:
                segments.append(current)
                current = []
        else:
            current.append(tok)
    if current:
        segments.append(current)
    return segments


def _is_commit(command: str) -> bool:
    """True when a command *segment* actually creates a commit (not dry-run / help)."""
    for seg in _command_segments(command):
        if not seg or seg[0] != "git":
            continue
        i = 1  # Skip git global options (e.g. `-C <path>`, `-c <k=v>`).
        while i < len(seg) and seg[i].startswith("-"):
            i += 2 if seg[i] in {"-C", "-c"} else 1
        if i < len(seg) and seg[i] == "commit" and not _SKIP_ARGS.intersection(seg[i + 1 :]):
            return True
    return False


def _tool(root: Path, name: str, *args: str) -> list[str]:
    """Prefer the in-project venv binary; fall back to `uv run <name>`."""
    venv_bin = root / ".venv" / "bin" / name
    if venv_bin.is_file() and os.access(venv_bin, os.X_OK):
        return [str(venv_bin), *args]
    return ["uv", "run", name, *args]


def _run(cmd: list[str], root: Path, timeout: int) -> tuple[int, str]:
    """Run a step; return (exit code, trimmed combined output)."""
    try:
        proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired:
        return 1, f"`{' '.join(cmd)}` timed out after {timeout}s."
    except OSError as exc:
        return 1, f"Could not run `{' '.join(cmd)}`: {exc}"
    output = (proc.stdout + proc.stderr).strip()
    if len(output) > _OUTPUT_TAIL:
        output = "…(truncated)…\n" + output[-_OUTPUT_TAIL:]
    return proc.returncode, output


def _deny(reason: str) -> None:
    """Emit a PreToolUse deny payload, blocking the commit with `reason`."""
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )


def main() -> None:
    """Gate git commits on pre-commit and pytest passing, in that order."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    command = str((payload.get("tool_input") or {}).get("command", ""))
    if not _is_commit(command):
        return  # Not a commit — let the command through untouched.

    root = _repo_root()

    code, output = _run(_tool(root, "pre-commit", "run", "--all-files"), root, _PRECOMMIT_TIMEOUT)
    if code != 0:
        _deny(
            "pre-commit failed before the commit — fix the reported issues, and re-stage any files "
            f"pre-commit auto-fixed, before committing:\n\n```\n{output or '(no output)'}\n```"
        )
        return

    code, output = _run(_tool(root, "pytest"), root, _PYTEST_TIMEOUT)
    if code not in (0, 5):  # 0 = all passed, 5 = no tests collected
        _deny(
            "pytest failed — fix the failing tests before committing "
            f"(CLAUDE.md requires the suite to pass first):\n\n```\n{output or '(no output)'}\n```"
        )


if __name__ == "__main__":
    main()
