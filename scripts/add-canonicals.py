#!/usr/bin/env python3
"""
Add <link rel="canonical"> to every HTML file at the repo root that is missing one.

Canonical URL is derived from the filename:
  index.html                -> https://skipschool.ai/
  05-ai-curriculum-builder.html -> https://skipschool.ai/05-ai-curriculum-builder

Inserts the tag on a new line immediately after the first <meta name="description">.
If no meta description is present, inserts after <title>. Skips files that already
have a canonical tag.

Safe to re-run — idempotent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BASE = "https://skipschool.ai"
REPO_ROOT = Path(__file__).resolve().parent.parent


def canonical_for(filename: str) -> str:
    if filename == "index.html":
        return f"{BASE}/"
    slug = filename[:-len(".html")]
    return f"{BASE}/{slug}"


CANONICAL_RE = re.compile(r'<link[^>]+rel=["\']canonical["\']', re.IGNORECASE)
META_DESC_RE = re.compile(r'(<meta\s+name=["\']description["\'][^>]*>)', re.IGNORECASE)
TITLE_RE = re.compile(r'(</title>)', re.IGNORECASE)


def process(path: Path) -> str:
    html = path.read_text(encoding="utf-8")

    if CANONICAL_RE.search(html):
        return "skip (already has canonical)"

    canonical_tag = f'\n    <link rel="canonical" href="{canonical_for(path.name)}">'

    # Prefer insertion right after <meta name="description"> for consistency
    # with existing pages that follow that pattern.
    new_html, n = META_DESC_RE.subn(
        lambda m: m.group(1) + canonical_tag, html, count=1
    )
    if n == 0:
        new_html, n = TITLE_RE.subn(
            lambda m: m.group(1) + canonical_tag, html, count=1
        )
    if n == 0:
        return "skip (no <meta description> or <title> anchor found)"

    path.write_text(new_html, encoding="utf-8")
    return f"added -> {canonical_for(path.name)}"


def main() -> int:
    files = sorted(REPO_ROOT.glob("*.html"))
    if not files:
        print("No HTML files found at repo root", file=sys.stderr)
        return 1
    print(f"Scanning {len(files)} HTML files at {REPO_ROOT}")
    added = skipped = 0
    for f in files:
        result = process(f)
        print(f"  {f.name}: {result}")
        if result.startswith("added"):
            added += 1
        else:
            skipped += 1
    print(f"\nDone. Added canonicals to {added} files; skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
