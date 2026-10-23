#!/usr/bin/env python3
# Copyright 2026 KODER contributors
# SPDX-License-Identifier: Apache-2.0
"""Check this skill repository locally using only the Python standard library."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "LICENSE", "NOTICE", "VERSION", "CHANGELOG.md", "RELEASE.md",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md",
    "docs/getting-started.md", "docs/integration.md", "docs/memory-model.md",
    "docs/validation.md", "docs/faq.md",
    "skills/koder-shared-memory/SKILL.md",
    "skills/koder-shared-memory/agents/openai.yaml",
    "scripts/check_repository.py", "scripts/package_skill.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def headings(text):
    anchors = set()
    counts = {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        title = re.sub(r"[`*_]", "", title).lower()
        anchor = re.sub(r"[^\w\s-]", "", title).replace(" ", "-")
        index = counts.get(anchor, 0)
        counts[anchor] = index + 1
        anchors.add(anchor + (f"-{index}" if index else ""))
    return anchors


def check(root=ROOT):
    root = root.resolve()
    for relative in REQUIRED:
        require((root / relative).is_file(), f"Missing required file: {relative}")

    files = sorted(
        item for item in root.rglob("*")
        if not any(part in {".git", "dist", "__pycache__"} for part in item.relative_to(root).parts)
        and (item.is_file() or item.is_symlink())
    )
    contents = {}
    for item in files:
        relative = item.relative_to(root).as_posix()
        require(not item.is_symlink(), f"Symlinks cannot enter the publication: {relative}")
        text = item.read_text(encoding="utf-8")
        require("\x00" not in text, f"Binary content is not expected: {relative}")
        require(item.suffix == ".md" or not re.search(r"[\u3400-\u9fff]", text), f"Non-English CJK content outside documentation: {relative}")
        require(not re.search(r"/(?:Users|home)/[A-Za-z0-9_.-]+/", text), f"Personal absolute path: {relative}")
        require(not re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)", text), f"Possible credential: {relative}")
        if item.suffix in {".md", ".yaml"}:
            require(not re.search(r"\b(?:TODO|TBD|FIXME)\b", text), f"Unfinished placeholder: {relative}")
        contents[item] = text

    skill = contents[root / "skills/koder-shared-memory/SKILL.md"]
    match = re.match(r"\A---\n(.*?)\n---\n(.+)\Z", skill, re.DOTALL)
    require(match is not None, "Skill needs frontmatter and a body")
    front, body = match.groups()
    require(re.search(r"^name: koder-shared-memory$", front, re.MULTILINE), "Unexpected skill name")
    require(re.search(r"^description: \S.+$", front, re.MULTILINE), "Missing single-line skill description")
    require(re.search(r"^license: Apache-2.0$", front, re.MULTILINE), "Skill license differs from this distribution")
    license_text = contents[root / "LICENSE"]
    require("Apache License" in license_text and "Version 2.0, January 2004" in license_text
            and "END OF TERMS AND CONDITIONS" in license_text,
            "LICENSE must contain the complete Apache-2.0 license")
    version = contents[root / "VERSION"].strip()
    require(re.fullmatch(r"\d+\.\d+\.\d+", version), "VERSION must contain a semantic version")
    require(f'  version: "{version}"' in front, "Skill and distribution versions differ")
    require(bool(body.strip()), "Empty skill body")
    require("allow_implicit_invocation: true" in contents[root / "skills/koder-shared-memory/agents/openai.yaml"], "Implicit invocation metadata is missing")

    links = 0
    for item, text in contents.items():
        if item.suffix != ".md":
            continue
        for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
            link = urlsplit(target)
            if link.scheme or link.netloc:
                continue
            destination = (item.parent / unquote(link.path)).resolve() if link.path else item
            require(destination.is_relative_to(root), f"Link leaves the repository: {target}")
            require(destination.is_file(), f"Broken local link in {item.relative_to(root)}: {target}")
            if link.fragment:
                destination_text = contents.get(destination, destination.read_text(encoding="utf-8"))
                require(unquote(link.fragment) in headings(destination_text), f"Broken heading link: {target}")
            links += 1

    return {"status": "PASS", "version": version, "files": len(files), "local_links": links,
            "scope": "Structural checks only; no model, platform, or cross-device behavior verified."}


if __name__ == "__main__":
    try:
        print(json.dumps(check(), indent=2))
    except (ValueError, OSError, UnicodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
