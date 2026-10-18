#!/usr/bin/env python3
# Copyright 2026 KODER contributors
# SPDX-License-Identifier: Apache-2.0
"""Build and verify the portable skill archive without external dependencies."""

import hashlib
import json
import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
from check_repository import check


ROOT = Path(__file__).resolve().parents[1]


def main():
    validation = check(ROOT)
    sources = {
        "koder-shared-memory/SKILL.md": ROOT / "skills/koder-shared-memory/SKILL.md",
        "koder-shared-memory/agents/openai.yaml": ROOT / "skills/koder-shared-memory/agents/openai.yaml",
        "koder-shared-memory/LICENSE": ROOT / "LICENSE",
        "koder-shared-memory/NOTICE": ROOT / "NOTICE",
    }
    payloads = {name: source.read_bytes() for name, source in sources.items()}
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    package = output / "koder-shared-memory.skill.zip"
    with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, payload in sorted(payloads.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, payload)
    with zipfile.ZipFile(package) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(payloads):
            raise ValueError("Archive integrity or file inventory mismatch")
        for name, payload in payloads.items():
            if archive.read(name) != payload:
                raise ValueError(f"Archive round-trip mismatch: {name}")
    report = {
        "version": validation["version"], "package": package.name,
        "sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
        "files": [{"path": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}
                  for name, payload in sorted(payloads.items())],
        "scope": "Portable skill archive; no runtime or connector is included.",
    }
    (output / "manifest.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, UnicodeError, zipfile.BadZipFile) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
