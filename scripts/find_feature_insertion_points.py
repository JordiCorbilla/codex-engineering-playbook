from __future__ import annotations

import argparse
from pathlib import Path

IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    "bin",
    "obj",
}

PRIORITY_PARTS = (
    "controller",
    "service",
    "repository",
    "route",
    "api",
    "component",
    "hook",
    "client",
    "model",
)


def visible(path: Path) -> bool:
    return not any(part in IGNORED_DIRS for part in path.parts)


def score(path: Path, keyword: str) -> int:
    lowered = str(path).lower()
    value = 0
    if keyword in path.stem.lower():
        value += 5
    if keyword in lowered:
        value += 3
    value += sum(2 for part in PRIORITY_PARTS if part in lowered)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Find likely feature insertion points.")
    parser.add_argument("keyword", help="Feature keyword, such as order or customer")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--limit", type=int, default=20, help="Maximum results")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    keyword = args.keyword.lower()

    candidates = []
    for path in root.rglob("*"):
        if not visible(path):
            continue
        if path.is_dir():
            continue
        path_score = score(path.relative_to(root), keyword)
        if path_score > 0:
            candidates.append((path_score, path.relative_to(root)))

    for _, relative_path in sorted(candidates, key=lambda item: (-item[0], str(item[1])))[: args.limit]:
        print(str(relative_path).replace("\\", "/"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
