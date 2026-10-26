"""Check bilingual page pairs and internal navigation without third-party packages."""
from pathlib import Path
from collections import defaultdict
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def metadata(text):
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not match:
        return {}
    return {
        key: value.strip().strip(chr(34)).strip(chr(39))
        for key, value in re.findall(r"^([a-z_]+):\s*(.*?)\s*$", match[1], re.M)
    }

def check(root):
    errors = []
    pages = {}
    for lang in ("cs", "en"):
        for path in (root / lang).rglob("*"):
            if path.suffix not in (".html", ".md"):
                continue
            name = path.relative_to(root).as_posix()
            text = path.read_text(encoding="utf-8")
            meta = metadata(text)
            pages[name] = (meta, text)
            if meta.get("lang") != lang:
                errors.append(f"{name}: incorrect or missing lang")
            if not meta.get("translation_key"):
                errors.append(f"{name}: missing translation_key")
    groups = defaultdict(dict)
    urls = {}
    for name, (meta, text) in pages.items():
        lang, key = meta.get("lang"), meta.get("translation_key")
        if lang in groups[key]:
            errors.append(f"{name}: duplicate {lang} translation for {key}")
        groups[key][lang] = name
        url = meta.get("permalink", "/" + str(Path(name).with_suffix("")) + "/")
        if url in urls:
            errors.append(f"{name}: duplicate URL {url}")
        urls[url] = name
    for key, pair in groups.items():
        if set(pair) != {"cs", "en"}:
            errors.append(f"{key}: must have exactly one cs and one en page")
            continue
        cs, en = (pages[pair[lang]][0] for lang in ("cs", "en"))
        if cs.get("date") != en.get("date"):
            errors.append(f"{key}: publication dates differ")

    # Root is an intentional Czech homepage alias, not a second translation.
    root_text = (root / "index.md").read_text(encoding="utf-8")
    root_meta = metadata(root_text)
    if root_meta.get("lang") != "cs" or root_meta.get("translation_key") != "home":
        errors.append("index.md: root must be the Czech home alias")
    pages["index.md"] = (root_meta, root_text)
    urls["/"] = "index.md"
    linked = defaultdict(set)
    for name, (meta, text) in pages.items():
        lang = meta.get("lang")
        for target in re.findall(r"{%\s*link\s+([^\s%]+)\s*%}", text):
            if not (root / target).is_file():
                errors.append(f"{name}: missing link target {target}")
            elif target in pages:
                linked[name].add(target)
                if pages[target][0].get("lang") != lang:
                    errors.append(f"{name}: content link crosses language: {target}")
        literals = re.findall(r'href=["\x27](/[^"\x27]*)["\x27]', text)
        relative = re.findall(r"""href="{{\s*['"](/[^'"]*)['"]\s*\|\s*relative_url\s*}}""", text)
        for target in literals + relative:
            target = target.split("#")[0].split("?")[0]
            if target in urls:
                linked[name].add(urls[target])
                if pages[urls[target]][0].get("lang") != lang:
                    errors.append(f"{name}: content link crosses language: {target}")
            elif target.startswith(("/cs/", "/en/")):
                errors.append(f"{name}: unresolved local page URL {target}")
    for name, (meta, _) in pages.items():
        if meta.get("translation_key") == "home":
            continue
        homes = ("index.md", "cs/index.md") if meta.get("lang") == "cs" else ("en/index.md",)
        for home in homes:
            if name not in linked[home]:
                errors.append(f"{home}: missing listing for {name}")
    for home in ("index.md", "cs/index.md", "en/index.md"):
        text = pages[home][1]
        if "{% include language_switcher.html homepage=true %}" not in text:
            errors.append(f"{home}: shared language switcher missing")
        if "{% include alternate_languages.html %}" not in text:
            errors.append(f"{home}: hreflang metadata missing")
    layout = (root / "_layouts/default.html").read_text(encoding="utf-8")
    if 'page.lang' not in layout.split("<head>")[0]:
        errors.append("default layout: HTML language must follow page.lang")
    if "{% include language_switcher.html %}" not in layout.split("<body>")[-1]:
        errors.append("default layout: shared language switcher must be in body")
    return errors, len(groups)

if __name__ == "__main__":
    errors, count = check(ROOT)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {count} Czech/English page pairs, homepage listings and internal links.")
