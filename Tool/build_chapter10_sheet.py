from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import html
import re

import markdown
from bs4 import BeautifulSoup, Tag


ROOT = Path(r"D:\Fogust\Workspace\College\AC311\Cheat Sheet")
SRC_TXT = ROOT / "Chapter10" / "Data.txt"
DEDUCTIBLE_MD = ROOT / "Chapter10" / "13.4-deductible-clause.md"
OUT_MD = ROOT / "Chapter10" / "Data.md"
OUT_HTML = ROOT / "chapter-10-notes.html"


PAGE_TITLE = "Chapter 10: Provision"
PAGE_SUBTITLE = "Rebuilt from clean UTF-8 source to repair corrupted text."
PAGE_DESCRIPTION = (
    "AC311 exam sheet for Provision under IAS 37 rebuilt from clean UTF-8 source, "
    "covering liabilities, provisions, contingent items, measurement, and disclosures."
)
EYEBROW = "AC311 Intermediate Accounting"
PILLS = [
    "Provision",
    "IAS 37",
    "UTF-8 rebuild",
    "Deductible clause restored",
]


ASCII_SKIP_PREFIXES = (
    "If you have questions",
    "Let me know",
)


@dataclass
class Section:
    section_id: str
    title: str
    body_html: str


def strip_markdown_emphasis(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def slugify(text: str, index: int) -> str:
    slug = re.sub(r"<[^>]+>", "", text)
    slug = re.sub(r"[^\w\u0E00-\u0E7F]+", "-", slug, flags=re.UNICODE).strip("-").lower()
    return slug or f"section-{index}"


def normalize_source(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\ufeff", "")
    text = re.sub(r"\[cite:\s*\d+\]", "", text)
    text = text.replace("\U0001F4CC", "").replace("\u2705", "").replace("\u274C", "")

    cleaned_lines: list[str] = []
    previous_blank = False

    for raw_line in text.split("\n"):
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            if not previous_blank:
                cleaned_lines.append("")
            previous_blank = True
            continue

        if stripped.startswith(ASCII_SKIP_PREFIXES):
            continue

        cleaned_lines.append(stripped)
        previous_blank = False

    return "\n".join(cleaned_lines).strip() + "\n"


def convert_line(line: str) -> str:
    if match := re.match(r"^###\s+\*\*(.+?)\*\*\s*$", line):
        title = strip_markdown_emphasis(match.group(1))
        return f"## {title}"

    if match := re.match(r"^\*\*(.+?)\*\*\s*$", line):
        title = strip_markdown_emphasis(match.group(1))
        return f"### {title}"

    return line


def is_list_line(line: str) -> bool:
    return bool(re.match(r"^(?:\*|-|\d+\.)\s+", line))


def massage_markdown_lines(lines: list[str]) -> list[str]:
    first_heading = next((i for i, line in enumerate(lines) if line.startswith("## ")), 0)
    lines = lines[first_heading:]

    output: list[str] = []
    prev_nonblank = ""

    for line in lines:
        if line.startswith("## ") and output and output[-1] != "":
            output.append("")

        if is_list_line(line) and prev_nonblank and not is_list_line(prev_nonblank):
            if output and output[-1] != "":
                output.append("")

        output.append(line)

        if line.strip():
            prev_nonblank = line

    return output


def deductible_fragment() -> str:
    raw = DEDUCTIBLE_MD.read_text(encoding="utf-8")
    lines: list[str] = []
    h2_seen = 0
    keep = False

    for line in raw.splitlines():
        if line.startswith("## "):
            h2_seen += 1
            if h2_seen >= 2:
                keep = True
                lines.append("### " + line[3:].strip())
            continue

        if not keep:
            continue

        if line.startswith("### "):
            lines.append("#### " + line[4:].strip())
        else:
            lines.append(line)

    return "\n".join(lines).strip() + "\n"


def insert_deductible(md: str) -> str:
    fragment = deductible_fragment().strip()
    if fragment in md:
        return md

    lines = md.splitlines()
    output: list[str] = []
    inserted = False

    for line in lines:
        output.append(line)
        if not inserted and "Reimbursements" in line:
            output.extend(["", fragment, ""])
            inserted = True

    if not inserted:
        output.extend(["", "## Deductible Clause", "", fragment])

    return "\n".join(output).strip() + "\n"


def build_markdown() -> str:
    source = normalize_source(SRC_TXT.read_text(encoding="utf-8"))
    converted_lines = [convert_line(line) for line in source.splitlines()]
    massaged_lines = massage_markdown_lines(converted_lines)
    md = "# Chapter 10: Provision\n\n" + "\n".join(massaged_lines).strip() + "\n"
    md = insert_deductible(md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


def render_markdown(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def build_sections(article_html: str) -> list[Section]:
    soup = BeautifulSoup(article_html, "html.parser")
    nodes = [child for child in soup.children if isinstance(child, Tag)]
    sections: list[Section] = []
    current_title = "Overview"
    current_nodes: list[str] = []
    index = 1

    def flush() -> None:
        nonlocal current_nodes, current_title, index
        if not current_nodes:
            return
        body_html = "".join(current_nodes).strip()
        if not body_html:
            current_nodes = []
            return
        sections.append(Section(slugify(current_title, index), current_title, body_html))
        current_nodes = []
        index += 1

    for node in nodes:
        if node.name == "h1":
            continue
        if node.name == "h2":
            flush()
            current_title = node.get_text(" ", strip=True)
            continue
        current_nodes.append(str(node))

    flush()
    return sections


def render_nav(sections: list[Section]) -> str:
    return "\n".join(
        f'<a href="#{section.section_id}"><span>{i:02d}</span>{html.escape(section.title)}</a>'
        for i, section in enumerate(sections, start=1)
    )


def render_sections(sections: list[Section]) -> str:
    blocks = []
    for i, section in enumerate(sections, start=1):
        blocks.append(
            f"""
            <section class="sheet-section" id="{section.section_id}">
              <div class="section-kicker">Section {i:02d}</div>
              <h2>{html.escape(section.title)}</h2>
              <div class="section-body">
                {section.body_html}
              </div>
            </section>
            """
        )
    return "\n".join(blocks)


def build_html(md_text: str) -> str:
    article_html = render_markdown(md_text)
    sections = build_sections(article_html)
    nav_html = render_nav(sections)
    sections_html = render_sections(sections)
    pills_html = "".join(f"<li>{html.escape(pill)}</li>" for pill in PILLS)

    return f"""<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AC311 | {PAGE_TITLE}</title>
  <meta name="description" content="{html.escape(PAGE_DESCRIPTION)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #f4ede1;
      --paper: rgba(255, 250, 242, 0.92);
      --paper-strong: #fffaf2;
      --ink: #3b2c21;
      --muted: #6b5d50;
      --line: rgba(119, 96, 74, 0.16);
      --accent: #7b8564;
      --accent-soft: rgba(123, 133, 100, 0.12);
      --shadow: 0 16px 32px rgba(76, 56, 37, 0.05);
      --font-sans: "Google Sans Text", "Google Sans", "Product Sans", "Noto Sans Thai", sans-serif;
      --font-mono: "Google Sans Code", "SFMono-Regular", Consolas, monospace;
      --max: 1180px;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: var(--font-sans);
      background:
        linear-gradient(90deg, transparent 0, transparent 72px, rgba(160, 122, 88, 0.07) 72px, rgba(160, 122, 88, 0.07) 74px, transparent 74px),
        repeating-linear-gradient(180deg, transparent 0, transparent 38px, rgba(120, 99, 78, 0.06) 38px, rgba(120, 99, 78, 0.06) 39px),
        radial-gradient(circle at top left, rgba(255,255,255,0.42), transparent 34%),
        var(--bg);
      line-height: 1.78;
      letter-spacing: -0.01em;
    }}
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      opacity: 0.18;
      background-image: radial-gradient(rgba(90, 67, 47, 0.18) 0.45px, transparent 0.45px);
      background-size: 9px 9px;
      mask-image: linear-gradient(to bottom, rgba(0,0,0,0.3), transparent 35%);
    }}
    a {{ color: inherit; text-decoration: none; }}
    code, pre {{ font-family: var(--font-mono); }}
    .page {{
      width: min(calc(100% - 32px), var(--max));
      margin: 0 auto;
      padding: 28px 0 80px;
    }}
    .masthead {{
      padding: 18px 0 12px;
      border-bottom: 1px solid var(--line);
      margin-bottom: 20px;
    }}
    .eyebrow {{
      margin: 0 0 10px;
      color: var(--muted);
      font-size: 0.82rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      font-weight: 700;
    }}
    .hero {{
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
      gap: 28px;
      align-items: end;
    }}
    .hero h1 {{
      margin: 0;
      font-size: clamp(2.25rem, 5.6vw, 4.4rem);
      line-height: 0.98;
      letter-spacing: -0.05em;
      color: #36261c;
    }}
    .hero p {{
      margin: 14px 0 0;
      max-width: 62ch;
      color: var(--muted);
      font-size: 1rem;
    }}
    .hero-panel {{
      background: linear-gradient(180deg, rgba(255,255,255,0.82), rgba(255,250,242,0.92));
      border: 1px solid var(--line);
      border-radius: 22px;
      padding: 18px 20px;
      box-shadow: var(--shadow);
    }}
    .hero-panel strong {{
      display: block;
      margin-bottom: 10px;
      font-size: 0.9rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #554538;
    }}
    .hero-panel ul {{
      margin: 0;
      padding-left: 18px;
    }}
    .hero-panel li + li {{
      margin-top: 6px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 280px minmax(0, 1fr);
      gap: 24px;
      align-items: start;
    }}
    .sheet-nav {{
      position: sticky;
      top: 18px;
      background: rgba(255, 250, 242, 0.86);
      border: 1px solid var(--line);
      border-radius: 22px;
      padding: 18px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(14px);
    }}
    .sheet-nav h2 {{
      margin: 0 0 12px;
      font-size: 0.92rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    .sheet-nav a {{
      display: flex;
      gap: 10px;
      align-items: baseline;
      padding: 9px 10px;
      border-radius: 12px;
      color: #4d3d30;
      transition: background 0.18s ease;
    }}
    .sheet-nav a:hover {{
      background: var(--accent-soft);
    }}
    .sheet-nav span {{
      min-width: 24px;
      color: var(--accent);
      font-size: 0.82rem;
      font-weight: 700;
    }}
    .content-stack {{
      display: grid;
      gap: 18px;
    }}
    .sheet-section {{
      background: var(--paper);
      border: 1px solid var(--line);
      border-radius: 26px;
      padding: 22px 24px;
      box-shadow: var(--shadow);
      overflow: hidden;
    }}
    .section-kicker {{
      margin-bottom: 8px;
      color: var(--accent);
      font-size: 0.78rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      font-weight: 700;
    }}
    .sheet-section h2 {{
      margin: 0 0 14px;
      font-size: clamp(1.35rem, 2vw, 1.9rem);
      line-height: 1.18;
    }}
    .section-body h3 {{
      margin: 28px 0 10px;
      font-size: 1.12rem;
      line-height: 1.35;
      color: #433328;
    }}
    .section-body p, .section-body ul, .section-body ol, .section-body table, .section-body pre {{
      margin-top: 0;
      margin-bottom: 14px;
    }}
    .section-body ul, .section-body ol {{
      padding-left: 22px;
    }}
    .section-body li + li {{
      margin-top: 6px;
    }}
    .section-body table {{
      width: 100%;
      border-collapse: collapse;
      background: rgba(255,255,255,0.45);
    }}
    .section-body th,
    .section-body td {{
      border: 1px solid var(--line);
      padding: 10px 12px;
      vertical-align: top;
      text-align: left;
    }}
    .section-body pre {{
      padding: 14px 16px;
      background: #2d241e;
      color: #f8ead8;
      border-radius: 16px;
      overflow: auto;
    }}
    .footer-note {{
      margin-top: 22px;
      color: var(--muted);
      font-size: 0.92rem;
      text-align: center;
    }}
    @media (max-width: 980px) {{
      .hero,
      .layout {{
        grid-template-columns: 1fr;
      }}
      .sheet-nav {{
        position: static;
      }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="masthead">
      <div class="eyebrow">{EYEBROW}</div>
      <div class="hero">
        <div>
          <h1>{PAGE_TITLE}</h1>
          <p>{PAGE_SUBTITLE}</p>
        </div>
        <aside class="hero-panel">
          <strong>Quick Frame</strong>
          <ul>{pills_html}</ul>
        </aside>
      </div>
    </header>

    <div class="layout">
      <nav class="sheet-nav" aria-label="Contents">
        <h2>Contents</h2>
        {nav_html}
      </nav>

      <main class="content-stack">
        {sections_html}
      </main>
    </div>

    <p class="footer-note">{html.escape(PAGE_DESCRIPTION)}</p>
  </div>
</body>
</html>
"""


def main() -> None:
    md_text = build_markdown()
    OUT_MD.write_text(md_text, encoding="utf-8")
    html_text = build_html(md_text)
    OUT_HTML.write_text(html_text, encoding="utf-8")
    print(OUT_HTML)


if __name__ == "__main__":
    main()
