#!/usr/bin/env python3
"""
Skip School SEO Audit
=====================
Crawls https://skipschool.ai (or another base URL) starting from the sitemap,
falling back to a recursive crawl from the homepage if the sitemap is missing.

For each page, it records:
  - URL (final after redirects) and HTTP status
  - Title
  - All <link rel="canonical"> hrefs
  - All <meta name="description"> contents
  - All internal <a href> links
  - All <img src> references
  - Total page size in bytes

Then it checks every internal link and image for HTTP status (HEAD with GET
fallback), detects duplicate URLs (trailing-slash vs non-trailing-slash),
flags pages over 2 MB, and writes a structured JSON snapshot to
scripts/seo-audit-data.json plus a human-readable Markdown report at
scripts/seo-audit-report.md.

Usage:
  python3 scripts/seo-audit.py [--base https://skipschool.ai]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse, urldefrag

import requests
from bs4 import BeautifulSoup

USER_AGENT = "TJ-SEO-Audit/1.0"
REQUEST_DELAY = 0.5  # seconds between requests (politeness)
TIMEOUT = 20
PAGE_SIZE_LIMIT = 2 * 1024 * 1024  # 2 MB


def normalize_url(url: str, base: str) -> str:
    """Resolve relative URLs and strip fragments. Lower-case scheme/host."""
    if not url:
        return ""
    url, _ = urldefrag(urljoin(base, url.strip()))
    parsed = urlparse(url)
    scheme = parsed.scheme.lower() or "https"
    netloc = parsed.netloc.lower()
    return urlunparse((scheme, netloc, parsed.path, parsed.params, parsed.query, ""))


def is_internal(url: str, host: str) -> bool:
    parsed = urlparse(url)
    return parsed.netloc == "" or parsed.netloc.lower() == host.lower()


def fetch_sitemap_urls(base_url: str, session: requests.Session) -> list[str]:
    """Pull all <loc> entries from /sitemap.xml; recursively expand sitemap indexes."""
    sitemap_url = urljoin(base_url, "/sitemap.xml")
    print(f"[sitemap] fetching {sitemap_url}")
    try:
        r = session.get(sitemap_url, timeout=TIMEOUT)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"[sitemap] FAILED: {e}")
        return []

    soup = BeautifulSoup(r.text, "xml")
    urls: list[str] = []

    # Sitemap index?
    for sm in soup.find_all("sitemap"):
        loc = sm.find("loc")
        if loc and loc.text:
            time.sleep(REQUEST_DELAY)
            try:
                rr = session.get(loc.text.strip(), timeout=TIMEOUT)
                rr.raise_for_status()
                inner = BeautifulSoup(rr.text, "xml")
                for u in inner.find_all("url"):
                    l = u.find("loc")
                    if l and l.text:
                        urls.append(l.text.strip())
            except requests.RequestException as e:
                print(f"[sitemap] inner sitemap failed: {e}")

    # Plain sitemap
    for u in soup.find_all("url"):
        l = u.find("loc")
        if l and l.text:
            urls.append(l.text.strip())

    print(f"[sitemap] discovered {len(urls)} URLs")
    return urls


def crawl_fallback(base_url: str, session: requests.Session, limit: int = 200) -> list[str]:
    """Breadth-first crawl from the homepage if no sitemap is present."""
    host = urlparse(base_url).netloc
    seen: set[str] = set()
    queue: list[str] = [base_url]
    while queue and len(seen) < limit:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            time.sleep(REQUEST_DELAY)
            r = session.get(url, timeout=TIMEOUT)
            if r.status_code != 200 or "text/html" not in r.headers.get("content-type", ""):
                continue
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.find_all("a", href=True):
                nxt = normalize_url(a["href"], url)
                if is_internal(nxt, host) and nxt not in seen:
                    queue.append(nxt)
        except requests.RequestException:
            continue
    return sorted(seen)


def audit_page(url: str, session: requests.Session) -> dict:
    """Fetch a single page and extract SEO-relevant metadata."""
    record: dict = {
        "url": url,
        "final_url": None,
        "status": None,
        "size_bytes": 0,
        "title": None,
        "canonicals": [],
        "meta_descriptions": [],
        "internal_links": [],
        "external_links": [],
        "images": [],
        "error": None,
    }
    try:
        r = session.get(url, timeout=TIMEOUT, allow_redirects=True)
        record["status"] = r.status_code
        record["final_url"] = r.url
        record["size_bytes"] = len(r.content)
        if r.status_code != 200 or "text/html" not in r.headers.get("content-type", "").lower():
            return record
        soup = BeautifulSoup(r.text, "html.parser")
        if soup.title and soup.title.string:
            record["title"] = soup.title.string.strip()
        for link in soup.find_all("link", rel=lambda v: v and "canonical" in v):
            href = link.get("href")
            if href:
                record["canonicals"].append(href.strip())
        for m in soup.find_all("meta", attrs={"name": "description"}):
            content = m.get("content")
            if content is not None:
                record["meta_descriptions"].append(content.strip())
        host = urlparse(r.url).netloc
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                continue
            resolved = normalize_url(href, r.url)
            if not resolved:
                continue
            if is_internal(resolved, host):
                record["internal_links"].append(resolved)
            else:
                record["external_links"].append(resolved)
        for img in soup.find_all("img"):
            src = img.get("src") or img.get("data-src")
            if not src:
                continue
            resolved = normalize_url(src, r.url)
            if resolved:
                record["images"].append(resolved)
    except requests.RequestException as e:
        record["error"] = str(e)
    return record


def head_or_get(url: str, session: requests.Session) -> int | None:
    """Return HTTP status; HEAD first, GET fallback for servers that 405 on HEAD."""
    try:
        r = session.head(url, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code in (405, 403):
            r = session.get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)
        return r.status_code
    except requests.RequestException:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Skip School SEO audit")
    parser.add_argument("--base", default="https://skipschool.ai", help="Base URL")
    parser.add_argument("--limit", type=int, default=0, help="Limit pages crawled (0 = no limit)")
    parser.add_argument("--out-json", default="scripts/seo-audit-data.json")
    parser.add_argument("--out-md", default="scripts/seo-audit-report.md")
    args = parser.parse_args()

    base = args.base.rstrip("/")
    host = urlparse(base).netloc

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    # 1. Discover URLs
    urls = fetch_sitemap_urls(base, session)
    if not urls:
        print("[discovery] no sitemap URLs; falling back to recursive crawl")
        urls = crawl_fallback(base, session)

    # Normalize + dedupe
    seen: set[str] = set()
    deduped: list[str] = []
    for u in urls:
        n = normalize_url(u, base)
        if n and is_internal(n, host) and n not in seen:
            seen.add(n)
            deduped.append(n)
    urls = deduped
    if args.limit and args.limit > 0:
        urls = urls[: args.limit]
    print(f"[crawl] auditing {len(urls)} pages")

    # 2. Audit each page
    pages: list[dict] = []
    for i, url in enumerate(urls, 1):
        print(f"  [{i}/{len(urls)}] {url}")
        record = audit_page(url, session)
        pages.append(record)
        time.sleep(REQUEST_DELAY)

    # 3. Resolve link/image statuses (only check unique URLs once)
    print("[checks] resolving internal-link statuses")
    link_targets: set[str] = set()
    image_targets: set[str] = set()
    for p in pages:
        for l in p["internal_links"]:
            link_targets.add(l)
        for img in p["images"]:
            image_targets.add(img)

    link_status: dict[str, int | None] = {}
    image_status: dict[str, int | None] = {}

    for i, t in enumerate(sorted(link_targets), 1):
        if i % 25 == 0:
            print(f"  [links {i}/{len(link_targets)}]")
        link_status[t] = head_or_get(t, session)
        time.sleep(REQUEST_DELAY)

    print("[checks] resolving image statuses")
    for i, t in enumerate(sorted(image_targets), 1):
        if i % 25 == 0:
            print(f"  [images {i}/{len(image_targets)}]")
        image_status[t] = head_or_get(t, session)
        time.sleep(REQUEST_DELAY)

    # 4. Build issues
    issues = build_issues(pages, link_status, image_status, host)

    # 5. Write JSON snapshot
    snapshot = {
        "base": base,
        "page_count": len(pages),
        "pages": pages,
        "link_status": link_status,
        "image_status": image_status,
        "issues_summary": {k: len(v) for k, v in issues.items()},
    }
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(snapshot, indent=2))
    print(f"[done] wrote {args.out_json}")

    # 6. Write Markdown report
    report = render_report(base, pages, link_status, image_status, issues)
    Path(args.out_md).write_text(report)
    print(f"[done] wrote {args.out_md}")

    # 7. Print summary
    print("\n=== SUMMARY ===")
    for k, v in issues.items():
        print(f"  {k}: {len(v)}")
    return 0


def build_issues(
    pages: list[dict],
    link_status: dict[str, int | None],
    image_status: dict[str, int | None],
    host: str,
) -> dict[str, list]:
    issues: dict[str, list] = {
        "missing_canonical": [],
        "multiple_canonicals": [],
        "wrong_canonical": [],
        "missing_meta_description": [],
        "multiple_meta_descriptions": [],
        "broken_internal_links": [],
        "broken_images": [],
        "oversized_pages": [],
        "trailing_slash_duplicates": [],
        "non_html_or_failed": [],
    }

    # Trailing-slash duplicates: build a map of normalized path -> [urls]
    path_map: dict[str, list[str]] = defaultdict(list)

    for p in pages:
        url = p["url"]
        status = p["status"]
        if status is None or status >= 400:
            issues["non_html_or_failed"].append({"url": url, "status": status, "error": p["error"]})
            continue

        # Canonical checks
        canonicals = p["canonicals"]
        if len(canonicals) == 0:
            issues["missing_canonical"].append({"url": url})
        elif len(canonicals) > 1:
            issues["multiple_canonicals"].append({"url": url, "canonicals": canonicals})
        else:
            c = normalize_url(canonicals[0], url)
            # Wrong canonical = canonical does not point to self (after stripping trailing slash)
            if c.rstrip("/") != url.rstrip("/"):
                issues["wrong_canonical"].append({"url": url, "canonical": canonicals[0]})

        # Meta description
        descs = p["meta_descriptions"]
        if len(descs) == 0:
            issues["missing_meta_description"].append({"url": url})
        elif len(descs) > 1:
            issues["multiple_meta_descriptions"].append({"url": url, "count": len(descs)})

        # Page size
        if p["size_bytes"] > PAGE_SIZE_LIMIT:
            issues["oversized_pages"].append({"url": url, "size_bytes": p["size_bytes"]})

        # Build trailing-slash dedup map
        parsed = urlparse(url)
        normalized_path = parsed.path.rstrip("/") or "/"
        key = (parsed.netloc, normalized_path)
        path_map[key].append(url)

    # Broken internal links: source -> target
    for p in pages:
        for target in p["internal_links"]:
            st = link_status.get(target)
            if st is not None and 400 <= st < 600:
                issues["broken_internal_links"].append(
                    {"source": p["url"], "target": target, "status": st}
                )

    # Broken images
    for p in pages:
        for target in p["images"]:
            st = image_status.get(target)
            if st is not None and 400 <= st < 600:
                issues["broken_images"].append(
                    {"source": p["url"], "image": target, "status": st}
                )

    # Trailing slash duplicates
    for key, members in path_map.items():
        if len(set(members)) > 1:
            issues["trailing_slash_duplicates"].append({"variants": sorted(set(members))})

    return issues


def render_report(
    base: str,
    pages: list[dict],
    link_status: dict[str, int | None],
    image_status: dict[str, int | None],
    issues: dict[str, list],
) -> str:
    lines: list[str] = []
    lines.append(f"# Skip School SEO Audit Report")
    lines.append("")
    lines.append(f"- Base: {base}")
    lines.append(f"- Pages crawled: {len(pages)}")
    lines.append(f"- Internal link targets checked: {len(link_status)}")
    lines.append(f"- Image targets checked: {len(image_status)}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Issue | Count |")
    lines.append("|---|---|")
    for k, v in issues.items():
        lines.append(f"| {k} | {len(v)} |")
    lines.append("")

    def section(title: str, items: list, render):
        lines.append(f"## {title} ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_None_")
            lines.append("")
            return
        for item in items:
            lines.append(render(item))
        lines.append("")

    section(
        "Pages missing canonical",
        issues["missing_canonical"],
        lambda i: f"- {i['url']}",
    )
    section(
        "Pages with multiple canonicals",
        issues["multiple_canonicals"],
        lambda i: f"- {i['url']} → {i['canonicals']}",
    )
    section(
        "Pages with wrong canonical (does not match self)",
        issues["wrong_canonical"],
        lambda i: f"- {i['url']} → canonical: {i['canonical']}",
    )
    section(
        "Pages missing meta description",
        issues["missing_meta_description"],
        lambda i: f"- {i['url']}",
    )
    section(
        "Pages with multiple meta descriptions",
        issues["multiple_meta_descriptions"],
        lambda i: f"- {i['url']} (count: {i['count']})",
    )
    section(
        "Broken internal links (source → target [status])",
        issues["broken_internal_links"],
        lambda i: f"- {i['source']} → {i['target']} [{i['status']}]",
    )
    section(
        "Broken images (source → image [status])",
        issues["broken_images"],
        lambda i: f"- {i['source']} → {i['image']} [{i['status']}]",
    )
    section(
        "Pages over 2 MB",
        issues["oversized_pages"],
        lambda i: f"- {i['url']} ({i['size_bytes'] / 1024 / 1024:.2f} MB)",
    )
    section(
        "Trailing-slash duplicates",
        issues["trailing_slash_duplicates"],
        lambda i: f"- {' ↔ '.join(i['variants'])}",
    )
    section(
        "Pages that returned non-200 / non-HTML",
        issues["non_html_or_failed"],
        lambda i: f"- {i['url']} [status: {i['status']}, error: {i['error']}]",
    )

    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
