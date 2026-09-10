"""Validate bilingual source coverage, CommonMark emphasis, and built links."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
PAGES = ("index", "preparation", "part1", "part2", "summary")
ERRORS = []


def check_source(path):
    source = path.read_text(encoding="utf-8")
    # CommonMark does not parse MkDocs link class attributes as markup.
    prose_source = re.sub(r"(?<=\))\{(?:\s+\.[\w-]+)+\s*\}", "", source)
    tokens = MarkdownIt("commonmark").parse(prose_source)
    for token in tokens:
        if token.type != "inline":
            continue
        for child in token.children or []:
            if child.type == "text" and "**" in child.content:
                ERRORS.append(f"Unrendered emphasis in {path.relative_to(ROOT)}: {child.content}")
    if "/ja/" in path.as_posix() and path.name != "README.md":
        japanese = r"\u3041-\u3096\u30a1-\u30fa\u3400-\u9fff"
        for token in tokens:
            if token.type != "inline":
                continue
            # Inline code is opaque, but its boundary still needs prose spacing.
            prose = "".join(
                "X" if child.type == "code_inline" else
                child.content if child.type == "text" else
                " " if child.type in ("softbreak", "hardbreak") else ""
                for child in token.children or []
            )
            checks = {
                "Half-width prose parentheses": r"[()]",
                "Full-width colon": "：",
                "Missing Japanese/Latin space": rf"[{japanese}][A-Za-z0-9]|[A-Za-z0-9][{japanese}]",
                "Missing space after colon": rf"(?<=[{japanese}0-9]):(?=\S)",
                "Missing arrow spacing": r"\S→|→\S",
            }
            for label, pattern in checks.items():
                if re.search(pattern, prose):
                    ERRORS.append(f"{label} in {path.relative_to(ROOT)}: {prose}")


def check_site():
    site = ROOT / "site"
    if not (site / "index.html").is_file():
        ERRORS.append("Build the site with mkdocs build --strict before validation")
        return
    for path in site.rglob("*.html"):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        article = soup.select_one(".md-content__inner")
        if not article:
            continue
        # Every lesson except the summary must render one styled next link.
        relative = path.relative_to(site).as_posix()
        next_pages = {f"{prefix}{page}" for prefix in ("", "ja/")
                      for page in ("index.html", "preparation/index.html",
                                   "part1/index.html", "part2/index.html")}
        if relative in next_pages and len(article.select("a.workshop-next[href]")) != 1:
            ERRORS.append(f"Missing styled next button in {path.relative_to(ROOT)}")
        for node in article.find_all(string=True):
            if "**" in node and not node.find_parent(["pre", "code", "script", "style"]):
                ERRORS.append(f"Visible emphasis delimiter in {path.relative_to(ROOT)}")
        for link in article.select("a[href], img[src]"):
            url = urlsplit(link.get("href", link.get("src", "")))
            if url.scheme or url.netloc or url.path.startswith("/"):
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                ERRORS.append(f"Missing site target in {path.relative_to(ROOT)}: {url.geturl()}")
                continue
            if url.fragment and target.suffix == ".html":
                target_soup = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
                if not target_soup.find(id=unquote(url.fragment)):
                    ERRORS.append(f"Missing anchor in {path.relative_to(ROOT)}: {url.geturl()}")


for page in PAGES:
    for prefix in ("docs", "docs/ja"):
        path = ROOT / prefix / f"{page}.md"
        if not path.is_file():
            ERRORS.append(f"Missing language counterpart: {path}")
for name in ("README.md", "worksheet.md"):
    for locale in ("en", "ja"):
        if not (ROOT / "setup/participant" / locale / name).is_file():
            ERRORS.append(f"Missing participant counterpart: {locale}/{name}")
for base in (ROOT / "docs", ROOT / "setup"):
    for path in base.rglob("*.md"):
        check_source(path)
check_source(ROOT / "README.md")
check_site()
if ERRORS:
    print("\n".join(ERRORS), file=sys.stderr)
    sys.exit(1)
print("Validated language pairs, CommonMark emphasis, Japanese notation, and built article links.")
