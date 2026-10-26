"""Validate SEO source metadata; use --live to inspect the deployed HTML."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from check_translations import metadata

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://mamarafiki.cz"
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.lang = None
        self.meta = {}
        self.links = []
        self.schemas = []
        self.json_buffer = None
        self.titles = 0
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "title":
            self.titles += 1
        if tag == "meta":
            self.meta[a.get("name", a.get("property", ""))] = a.get("content", "")
        if tag == "link":
            self.links.append(a)
        if tag == "script" and a.get("type") == "application/ld+json":
            self.json_buffer = ""
    def handle_data(self, data):
        if self.json_buffer is not None:
            self.json_buffer += data
    def handle_endtag(self, tag):
        if tag == "script" and self.json_buffer is not None:
            self.schemas.append(json.loads(self.json_buffer))
            self.json_buffer = None

def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mamarafiki-SEO-Check/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")

def source_checks():
    count = 0
    for lang in ("cs", "en"):
        for path in (ROOT / lang).iterdir():
            if path.suffix not in (".md", ".html"):
                continue
            text = path.read_text(encoding="utf-8")
            meta = metadata(text)
            description = meta.get("description", "")
            require(50 <= len(description) <= 200, f"{path.name}: missing or unsuitable description")
            require(meta.get("locale") == {"cs": "cs_CZ", "en": "en_GB"}[lang], f"{path}: locale")
            kind = "WebSite" if meta.get("translation_key") == "home" else "CollectionPage" if path.stem == "laktacni_poradenstvi" else "BlogPosting"
            require(f"seo:\n  type: {kind}\n" in text, f"{path}: schema type")
            if "<img " in text:
                require("\nimage:\n" in text, f"{path}: missing article image metadata")
            count += 1
    for name in ("index.md", "cs/index.md", "en/index.md", "_layouts/default.html"):
        text = (ROOT / name).read_text(encoding="utf-8")
        require(text.count("{% seo %}") == 1, f"{name}: need exactly one SEO include")
        require("{% include search_metadata.html %}" in text, f"{name}: shared search metadata")
    root = (ROOT / "index.md").read_text(encoding="utf-8")
    require("canonical_url: https://mamarafiki.cz/cs/" in root, "Root canonical must point to /cs/")
    require("sitemap: false" in root, "Root duplicate must be excluded from sitemap")
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    require("author:\n  name: Josefína Drbálková\n" in config, "Missing author")
    require("- jekyll-seo-tag" in config, "SEO plugin must be declared")
    require("https://mamarafiki.cz/sitemap.xml" in (ROOT / "robots.txt").read_text(), "Missing sitemap discovery")
    require('content="noindex,nofollow"' in (ROOT / "office.html").read_text(encoding="utf-8"), "Office noindex must remain")
    return count

def live_checks(expected_count):
    sitemap = ET.fromstring(get(BASE + "/sitemap.xml"))
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
    entries = sitemap.findall("sm:url", ns)
    require(len(entries) == expected_count, "Sitemap must contain all canonical language pages")
    urls = [entry.findtext("sm:loc", namespaces=ns) for entry in entries]
    require(len(urls) == len(set(urls)), "Duplicate sitemap URLs")
    require(BASE + "/" not in urls and not any("office" in url for url in urls), "Internal/duplicate page in sitemap")
    for entry, url in zip(entries, urls):
        page = Page(get(url))
        prefix = url + ": "
        require(page.titles == 1, prefix + "duplicate/missing title")
        require(bool(page.meta.get("description")), prefix + "missing description")
        require(page.meta.get("author") == "Josefína Drbálková", prefix + "author")
        require("noindex" not in page.meta.get("robots", ""), prefix + "unexpected noindex")
        canonicals = [a["href"] for a in page.links if a.get("rel") == "canonical"]
        require(canonicals == [url], prefix + "canonical")
        alternates = {a.get("hreflang"): a.get("href") for a in page.links if a.get("rel") == "alternate"}
        sitemap_alternates = {a.get("hreflang"): a.get("href") for a in entry.findall("x:link", ns)}
        require(alternates == sitemap_alternates, prefix + "HTML/sitemap alternates differ")
        require(set(alternates) == {"cs", "en", "x-default"}, prefix + "missing alternates")
        require(alternates.get(page.lang) == url, prefix + "language/self alternate mismatch")
        require(all(target in urls for target in alternates.values()), prefix + "alternate outside sitemap")
        require(page.meta.get("og:url") == url, prefix + "Open Graph canonical mismatch")
        require(page.meta.get("og:description") == page.meta.get("description"), prefix + "Open Graph description mismatch")
        require(bool(page.schemas), prefix + "missing JSON-LD")
        for schema in page.schemas:
            if schema.get("@type") == "BlogPosting":
                require(schema.get("author", {}).get("name") == "Josefína Drbálková", prefix + "article author missing")
    root = Page(get(BASE + "/"))
    require([a.get("href") for a in root.links if a.get("rel") == "canonical"] == [BASE + "/cs/"], "Root canonical")
    require("noindex" in Page(get(BASE + "/office.html")).meta.get("robots", ""), "Office noindex")
    require("Sitemap: " + BASE + "/sitemap.xml" in get(BASE + "/robots.txt"), "robots sitemap")

if __name__ == "__main__":
    count = source_checks()
    if "--live" in sys.argv:
        live_checks(count)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: SEO metadata for {count} canonical pages" + (" and live HTML/sitemap/robots" if "--live" in sys.argv else "") + ".")
