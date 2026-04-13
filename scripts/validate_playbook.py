from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "conventions/architecture.md",
    "conventions/csharp.md",
    "conventions/python.md",
    "conventions/react-typescript.md",
    ".agents/skills/csharp-backend-feature/SKILL.md",
    ".agents/skills/csharp-backend-review/SKILL.md",
    ".agents/skills/python-backend-feature/SKILL.md",
    ".agents/skills/python-backend-review/SKILL.md",
    ".agents/skills/react-typescript-feature/SKILL.md",
    ".agents/skills/frontend-ux-polish/SKILL.md",
    ".agents/skills/api-contract-review/SKILL.md",
    ".agents/skills/layered-architecture-recon/SKILL.md",
    "examples/csharp-api",
    "examples/python-api",
    "examples/react-app",
]

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def validate_paths(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            errors.append(f"Missing required path: {relative}")
    return errors


def validate_markdown_links(root: Path) -> list[str]:
    errors = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for _, target in LINK_PATTERN.findall(text):
            if target.startswith("http://") or target.startswith("https://") or target.startswith("#"):
                continue
            target_path = (path.parent / target).resolve()
            if not target_path.exists():
                relative_source = path.relative_to(root).as_posix()
                errors.append(f"Broken link in {relative_source}: {target}")
    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = []
    errors.extend(validate_paths(root))
    errors.extend(validate_markdown_links(root))

    if errors:
        for error in errors:
            print(error)
        return 1

    print("Playbook structure and markdown links validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
