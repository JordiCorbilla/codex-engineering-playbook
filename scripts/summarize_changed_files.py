from __future__ import annotations

import argparse
import subprocess
from collections import defaultdict
from pathlib import Path


def git_output(args: list[str], cwd: Path) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def bucket_for(path: str) -> str:
    normalized = path.replace("\\", "/")
    if normalized.startswith(".agents/skills/"):
        return "skills"
    if normalized.startswith("conventions/"):
        return "conventions"
    if normalized.startswith("templates/"):
        return "templates"
    if normalized.startswith("scripts/"):
        return "scripts"
    if normalized.startswith("examples/"):
        return "examples"
    if normalized.startswith("blog/"):
        return "blog"
    return "root"


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize changed files by area.")
    parser.add_argument("--base", help="Optional base revision for git diff --name-only")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    command = ["diff", "--name-only", args.base] if args.base else ["status", "--short"]
    changed = git_output(command, root)

    buckets: dict[str, list[str]] = defaultdict(list)
    for line in changed:
        path = line[3:] if not args.base else line
        buckets[bucket_for(path)].append(path)

    for bucket in sorted(buckets):
        print(f"{bucket}:")
        for path in sorted(buckets[bucket]):
            print(f"  {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
