from __future__ import annotations

import argparse
from collections import Counter
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

ENTRYPOINT_MARKERS = {
    "Program.cs",
    "Startup.cs",
    "main.py",
    "app.py",
    "manage.py",
    "vite.config.ts",
    "package.json",
    "tsconfig.json",
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize repository structure.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = list(iter_files(root))
    suffixes = Counter(path.suffix or "<no-ext>" for path in files)
    entrypoints = sorted(
        str(path.relative_to(root)).replace("\\", "/")
        for path in files
        if path.name in ENTRYPOINT_MARKERS
    )

    print(f"Root: {root}")
    print(f"Files: {len(files)}")
    print("Top extensions:")
    for suffix, count in suffixes.most_common(10):
        print(f"  {suffix}: {count}")

    print("Entrypoints:")
    for entrypoint in entrypoints:
        print(f"  {entrypoint}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
