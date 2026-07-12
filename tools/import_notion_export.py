#!/usr/bin/env python3
"""
Import a Notion HTML/Markdown export into MkDocs while preserving attached
images/files byte-for-byte and recording SHA-256 hashes.

Usage:
    python tools/import_notion_export.py <notion_export_dir> <docs_output_dir>
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path
from urllib.parse import unquote

ASSET_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".pdf", ".docx", ".xlsx", ".pptx", ".zip", ".txt",
    ".csv", ".json", ".xml", ".ps1", ".md"
}

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def copy_assets(source: Path, destination: Path) -> list[dict]:
    manifest = []
    for path in source.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in ASSET_EXTENSIONS:
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        manifest.append({
            "source_path": str(relative).replace("\\", "/"),
            "local_path": str(target.relative_to(destination.parent)).replace("\\", "/"),
            "sha256": sha256(target),
            "size_bytes": target.stat().st_size,
        })
    return manifest

def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    export_dir = Path(sys.argv[1]).resolve()
    docs_dir = Path(sys.argv[2]).resolve()
    if not export_dir.is_dir():
        raise FileNotFoundError(export_dir)

    asset_root = docs_dir / "assets" / "notion-export"
    asset_root.mkdir(parents=True, exist_ok=True)
    manifest = copy_assets(export_dir, asset_root)

    manifest_path = asset_root / "manifest.json"
    manifest_path.write_text(
        json.dumps({"assets": manifest}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Copied {len(manifest)} assets")
    print(f"Manifest: {manifest_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
