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

TEST_MARKERS = (
    "test",
    "spec",
)


def is_visible(path: Path) -> bool:
    return not any(part in IGNORED_DIRS for part in path.parts)


def is_test_path(path: Path) -> bool:
    lowered = path.name.lower()
    parent = path.parent.name.lower()
    return any(marker in lowered for marker in TEST_MARKERS) or parent in {"tests", "test"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover likely test files.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    results = []

    for path in root.rglob("*"):
        if not path.is_file() or not is_visible(path):
            continue
        if is_test_path(path):
            results.append(path.relative_to(root))

    for result in sorted(results):
        print(str(result).replace("\\", "/"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
