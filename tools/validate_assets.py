#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

root = Path(__file__).resolve().parents[1]
manifests = list((root / "docs" / "assets").rglob("manifest.json"))
errors = []

for manifest_path in manifests:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    for asset in data.get("assets", []):
        p = manifest_path.parent.parent / asset["local_path"]
        if not p.exists():
            errors.append(f"Missing: {p}")
        elif sha256(p) != asset["sha256"]:
            errors.append(f"Hash mismatch: {p}")

if errors:
    print("\n".join(errors))
    raise SystemExit(1)

print(f"Validated {len(manifests)} manifest(s)")
