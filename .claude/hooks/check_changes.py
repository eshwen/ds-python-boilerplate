# Standalone Claude Code hook script (invoked via `python3`), not a package module.
# ruff: noqa: INP001
"""Stop hook: lint / format / type-check changed Python on turn end.

Fires when Claude finishes a turn. If any Python files changed versus HEAD
(tracked edits or new untracked files, excluding the `.claude/` tooling dir),
it runs the fast checks CLAUDE.md asks for after a reasonable set of changes:

  * `ruff check` on the changed files (honouring the `[tool.ruff]` excludes)
  * `ruff format --check` on the changed files
  * `pyrefly check` (whole project — a change can break dependents' types)

pytest is deliberately NOT run here (it runs before `git commit` instead — see
`before_commit.py`).

If everything passes (or nothing Python changed) the turn ends silently. If a
check fails, the hook blocks the stop and feeds the failures back so they get
fixed before moving on. To avoid trapping a session on an unfixable failure, it
gives up after a few consecutive blocks within the same turn (a fresh,
non-continuation stop resets that budget).

Tools are run from the in-project `.venv/bin/` if present, else via `uv run`.
"""

import contextlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

# Consecutive blocks allowed within one turn before giving up (prevents traps).
_MAX_BLOCKS = 3
# Chars of each failing check's output to surface (tail — failure summary lives there).
_OUTPUT_TAIL = 4000


def _repo_root() -> Path:
    """Project root — `CLAUDE_PROJECT_DIR` when the harness sets it, else cwd."""
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())


def _changed_py_files(root: Path) -> list[str]:
    """Changed-vs-HEAD plus new untracked Python files, minus the `.claude/` dir."""
    files: set[str] = set()
    for cmd in (
        ["git", "diff", "--name-only", "--diff-filter=d", "HEAD", "--", "*.py"],
        ["git", "ls-files", "--others", "--exclude-standard", "--", "*.py"],
    ):
        try:
            result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=30, check=False)  # noqa: S603
        except (OSError, subprocess.SubprocessError):
            continue
        files.update(line for line in result.stdout.splitlines() if line.strip())
    return sorted(f for f in files if not f.startswith(".claude/") and (root / f).is_file())


def _tool(root: Path, name: str) -> list[str]:
    """Prefer the in-project venv binary; fall back to `uv run <name>`."""
    venv_bin = root / ".venv" / "bin" / name
    if venv_bin.is_file() and os.access(venv_bin, os.X_OK):
        return [str(venv_bin)]
    return ["uv", "run", name]


def _run(root: Path, cmd: list[str], timeout: int) -> tuple[int, str]:
    """Run a check; return (exit code, trimmed combined output)."""
    try:
        proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout, check=False)  # noqa: S603
    except subprocess.TimeoutExpired:
        return 1, f"`{' '.join(cmd)}` timed out after {timeout}s."
    except OSError as exc:
        return 1, f"Could not run `{' '.join(cmd)}`: {exc}"
    output = (proc.stdout + proc.stderr).strip()
    if len(output) > _OUTPUT_TAIL:
        output = "…(truncated)…\n" + output[-_OUTPUT_TAIL:]
    return proc.returncode, output


def _marker(root: Path, session_id: str) -> Path:
    """Per-session file tracking consecutive blocks (keyed on the repo and session id)."""
    safe_id = "".join(c for c in f"{root.name}_{session_id}" if c.isalnum() or c in "-_")
    return Path(tempfile.gettempdir()) / f".claude_check_{safe_id}"


def _read_count(marker: Path) -> int:
    try:
        return int(marker.read_text())
    except (OSError, ValueError):
        return 0


def _write_count(marker: Path, count: int) -> None:
    with contextlib.suppress(OSError):  # Best effort — a missing counter just means a fresh budget.
        marker.write_text(str(count))


def main() -> None:
    """Run the fast checks on changed Python and block the stop if any fail."""
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        payload = {}

    root = _repo_root()
    marker = _marker(root, str(payload.get("session_id", "")))

    # A fresh (non-continuation) stop starts a new per-turn block budget.
    if not payload.get("stop_hook_active"):
        _write_count(marker, 0)

    changed = _changed_py_files(root)
    if not changed:
        _write_count(marker, 0)
        return  # Nothing Python changed — end the turn silently.

    ruff = _tool(root, "ruff")
    checks = (
        ("ruff check", [*ruff, "check", "--force-exclude", *changed], 60),
        ("ruff format", [*ruff, "format", "--check", "--force-exclude", *changed], 60),
        ("pyrefly", [*_tool(root, "pyrefly"), "check"], 120),
    )

    failures: list[str] = []
    failed_labels: list[str] = []
    for label, cmd, timeout in checks:
        code, output = _run(root, cmd, timeout)
        if code != 0:
            failed_labels.append(label)
            failures.append(f"### {label} failed\n```\n{output or '(no output)'}\n```")

    if not failures:
        _write_count(marker, 0)
        return  # All green — end the turn silently.

    count = _read_count(marker) + 1
    _write_count(marker, count)
    labels = ", ".join(failed_labels)

    # Give up after too many consecutive blocks so an unfixable failure can't trap us.
    if count > _MAX_BLOCKS:
        json.dump(
            {
                "systemMessage": (
                    f"{root.name} checks still failing after {_MAX_BLOCKS} attempts ({labels}); "
                    "letting the turn end. Run the checks manually to finish fixing them."
                )
            },
            sys.stdout,
        )
        return

    reason = (
        "The post-change checks from CLAUDE.md are failing. Fix these before finishing "
        "(only the fast checks ran — pytest runs before commit):\n\n" + "\n\n".join(failures)
    )
    json.dump(
        {
            "decision": "block",
            "reason": reason,
            "systemMessage": f"{root.name} checks failed ({labels}) — fixing before finishing.",
        },
        sys.stdout,
    )


if __name__ == "__main__":
    main()
