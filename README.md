# Microsoft Technical Archive Knowledge Base

MkDocs Material 기반 GitHub Pages Knowledge Base.

## Source boundary

Only the following Notion root and descendants are allowed:

- `Microsoft Technical Archive`
- Page ID: `36bdbd59-1ead-80a0-be5d-d0cc9d468183`

`Project Archive` and customer project pages are denied.

## Local preview

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

## GitHub Pages

Create the public repository `fetilonia.github.io`, upload all files, and select **GitHub Actions** as the Pages source.

## Asset parity

Notion attachment URLs are temporary signed URLs. Export the allowed Notion page tree and run:

```powershell
python tools/import_notion_export.py <ExportDirectory> docs
python tools/validate_assets.py
```

The importer preserves binary files and records SHA-256 hashes.
