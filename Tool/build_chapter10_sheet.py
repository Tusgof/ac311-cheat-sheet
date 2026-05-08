from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import html
import re

import markdown
from bs4 import BeautifulSoup, Tag


ROOT = Path(r"D:\Fogust\Workspace\College\AC311\Cheat Sheet")
SRC_MD = ROOT / "Chapter10" / "Data.md"
DEDUCTIBLE_MD = ROOT / "Chapter10" / "13.4-deductible-clause.md"
OUT_HTML = ROOT / "chapter-10-notes.html"


PAGE_TITLE = "Chapter 10: Provision"
PAGE_SUBTITLE = "อ่านตามลำดับ: ฐานคิดของหนี้สิน -> เกณฑ์รับรู้ -> การวัดมูลค่า -> รายการที่อาจเกิดขึ้น -> การเปิดเผยข้อมูล"
PAGE_DESCRIPTION = (
    "ชีททบทวน Provision ตาม IAS 37 สำหรับ AC311 ครอบคลุมตรรกะของหนี้สิน "
    "เกณฑ์รับรู้ การวัดมูลค่า รายการที่อาจเกิดขึ้น และการเปิดเผยข้อมูล"
)
EYEBROW = "AC311 Intermediate Accounting"
PILLS = ["IAS 37", "เกณฑ์รับรู้ -> การวัดมูลค่า", "รายการที่อาจเกิดขึ้น -> การเปิดเผยข้อมูล"]
QUICK_FRAME = [
    ("หนี้สิน", "present obligation + past event + outflow"),
    ("Provision", "probable + reliable estimate"),
    ("การวัดมูลค่า", "best estimate + discount if long-term"),
    ("รายการอาจเกิดขึ้น", "liability disclose / asset wait until virtually certain"),
]


THAI_SKIP_PREFIXES = (
    "หากคุณมีข้อสงสัย",
    "หากคุณสงสัย",
    "แจ้งผมได้เลย",
    "เคลียร์ไหม",
    "คุณมีประเด็นไหน",
    "จัดให้ตามคำขอ",
    "ขอแสดงความยินดี",
    "ลองวิเคราะห์และเขียนคำตอบ",
    "ลองวิเคราะห์และพิมพ์คำตอบ",
    "ผมรออ่าน",
    "เดี๋ยวผม",
    "พร้อมที่จะให้ผม",
    "ผมขอจัดระเบียบเนื้อหา",
    "ผมขอจัดระเบียบเนื้อหาส่วนนี้",
    "ผมขอจัดระเบียบเนื้อหาช่วงสุดท้ายนี้",
    "ลุยกันต่อเลยครับ",
    "มาถึงด่านสุดท้าย",
    "พอเห็นลอจิกเบื้องหลังแบบนี้แล้ว",
    "คุณมาถูกทางแล้ว",
    "ถือว่าคุณมีฐานความรู้",
    "ถ้าคุณเก็บตก",
)
THAI_SKIP_CONTAINS = (
    "ถือว่าสอบผ่าน",
    "ยอดเยี่ยมมากครับ",
    "เป๊ะมาก",
    "เป็นคำถามที่ดีมาก",
    "เป็นคำถามที่เจาะลึก",
    "คุณมีความเข้าใจ",
    "ตอนนี้คุณมีความเข้าใจ",
    "พอเห็นภาพ",
    "เห็นภาพความแตกต่าง",
    "มาดูบทสรุป",
    "ลองทบทวนดูว่าเคลียร์ไหม",
    "พร้อมลุยข้อสอบได้สบายเลยครับ",
    "ขอชมเลยว่า",
    "ผมกล้าการันตีเลยว่า",
    "ส่วนนี้จะเป็นเนื้อหาที่เน้นความเข้าใจเชิงคอนเซปต์",
    "เพื่อให้คุณเห็นภาพรวมของหลักการและเข้าใจวิธีคำนวณครับ",
    "ลองพิมพ์คำตอบของคุณ",
    "วิเคราะห์คำตอบได้ดีมากครับ",
    "รับทราบครับ ขออภัย",
    "เพื่อให้คุณได้ฝึกทบทวน",
    "ยินดีด้วยครับ! เราเดินทางมาถึงบทสรุป",
)

PRACTICE_TITLE_MARKERS = (
    "โจทย์ข้อที่",
    "คำสั่ง:",
)

PRACTICE_TEXT_MARKERS = (
    "โจทย์อัตนัย",
    "เพื่อให้คุณได้ฝึก",
    "ทดสอบความเข้าใจ",
    "ก่อนที่เราจะปิดจบ",
    "คุณอยากลองทำโจทย์",
    "จัดโจทย์อัตนัย",
    "โจทย์ 3 ข้อที่ออกแบบมา",
    "ถือว่าคุณจับแก่น",
    "ทั้งสองแบบนี้จบที่เดียวกัน",
    "ส่วนประกอบในสไลด์หน้า 27-28 มีเพียงเท่านี้ครับ",
)


@dataclass
class Section:
    section_id: str
    title: str
    body_html: str
    group_id: str
    theme: str


@dataclass(frozen=True)
class GroupSpec:
    group_id: str
    nav_label: str
    title: str
    description: str


GROUP_SPECS = [
    GroupSpec(
        "foundations",
        "01 ฐานคิด",
        "ฐานคิดของหนี้สิน",
        "เริ่มจากนิยามหนี้สิน present obligation และ past obligating event เพื่อแยกก่อนว่าเรื่องใดเป็นหนี้สินจริงและเรื่องใดยังไม่ถึงจุดรับรู้รายการ",
    ),
    GroupSpec(
        "recognition-timing",
        "02 รับรู้",
        "Recognition และจังหวะเวลา",
        "ต่อด้วยเกณฑ์รับรู้ provision, probable, valid expectation และกรณีศึกษาที่ทำให้เห็นเส้นแบ่งระหว่างตั้งหนี้สินกับเปิดเผยข้อมูล",
    ),
    GroupSpec(
        "measurement-special",
        "03 วัดมูลค่า",
        "Measurement และกรณีพิเศษ",
        "รวม best estimate, expected value, present value, decommissioning, onerous contract และ reimbursement เพื่อปิดฝั่งการวัดมูลค่าให้ครบเป็นก้อนเดียว",
    ),
    GroupSpec(
        "contingencies",
        "04 อาจเกิดขึ้น",
        "Contingent Liabilities และ Contingent Assets",
        "แยกสถานะรายการที่ยังไม่รับรู้ในงบ และดูว่าความน่าจะเป็นกับความเชื่อถือได้ของตัวเลขเปลี่ยนผลทางบัญชีอย่างไร",
    ),
    GroupSpec(
        "disclosure-wrap",
        "05 เปิดเผย",
        "Disclosure และแผนผังข้อสอบ",
        "ปิดบทด้วย disclosure, decision tree และ probability matrix เพื่อใช้ทวนภาพรวมก่อนสอบได้ในหน้าเดียว",
    ),
]


def strip_markdown_emphasis(text: str) -> str:
    return re.sub(r"\*\*(.*?)\*\*", r"\1", text).strip()


def slugify(text: str, index: int) -> str:
    slug = re.sub(r"<[^>]+>", "", text)
    slug = re.sub(r"[^\w\u0E00-\u0E7F]+", "-", slug, flags=re.UNICODE).strip("-").lower()
    return slug or f"section-{index}"


def is_conversational_line(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if re.match(r"^#{2,6}\s+โจทย์ข้อที่", stripped):
        return True
    if stripped.startswith("**คำสั่ง:**"):
        return True
    if stripped.startswith(THAI_SKIP_PREFIXES):
        return True
    return any(marker in stripped for marker in THAI_SKIP_CONTAINS)


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

        if is_conversational_line(stripped):
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
    if "Deductible clause" in md or "ค่าเสียหายส่วนแรก" in md:
        return md

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
    md = SRC_MD.read_text(encoding="utf-8")
    if not md.lstrip().startswith("#"):
        md = "# Chapter 10: Provision\n\n" + md.strip() + "\n"
    md = insert_deductible(md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


def render_markdown(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def section_theme(title: str) -> str:
    if any(token in title for token in ["Disclosure", "Decision Tree", "Probability Matrix", "เมทริกซ์", "เปิดเผยข้อมูล"]):
        return "theme-disclosure"
    if any(token in title for token in ["ข้อ ", "แบบที่", "สรุปภาพรวม", "ความย้อนแย้ง", "วิวัฒนาการ"]):
        return "theme-review"
    return "theme-accounting"


def classify_group(title: str) -> str:
    if any(token in title for token in [
        "ภาพรวมของหนี้สิน",
        "ตัวอย่างวิเคราะห์นิยามหนี้สิน",
        "หนี้สินคืออะไร",
        "ภาระผูกพันในปัจจุบัน",
        "เหตุการณ์ในอดีต",
        "สรุปความเข้าใจผ่านแบบทดสอบ",
        "เส้นแบ่งของ",
        "สัญญาที่กลายเป็นภาระ",
        "เงื่อนเวลาและทางเลือกที่สมเหตุสมผล",
    ]):
        return "foundations"

    if any(token in title for token in [
        "ประมาณการหนี้สิน",
        "ตัวอย่างการรับรู้ Provision",
        "เกณฑ์การรับรู้รายการ",
        "Probable",
        "โอกาสแพ้คดี",
        "วิเคราะห์เกณฑ์การรับรู้รายการ",
        "แยกแยะความแตกต่างระหว่าง Provision",
        "กรณีศึกษาการรับรู้รายการ Provision",
        "TAS#10",
        "การวิเคราะห์เงื่อนเวลาในการรับรู้ Provision",
        "การผสานกันของ",
        "กับดักเรื่องเงื่อนเวลา",
        "การเปลี่ยนแปลงของความน่าจะเป็น",
    ]):
        return "recognition-timing"

    if any(token in title for token in [
        "การวัดมูลค่า Provision",
        "ภาระรื้อถอน",
        "ประเด็นเฉพาะของ Provision",
        "กฎเหล็กของการวัดมูลค่า",
        "เทคนิคการเลือกตัวเลข",
        "แกะรอยโจทย์คำนวณ",
        "Expected Value",
        "Single Obligation",
        "Time Value of Money",
        "ไขข้อข้องใจ",
        "ค่ารื้อถอน",
        "Capital",
        "ผลขาดทุนจากการดำเนินงานในอนาคต",
        "ปรับโครงสร้างธุรกิจ",
        "Onerous Contracts",
        "Reimbursements",
        "ยอดรื้อถอน",
        "ค่าเสียหายส่วนแรก",
    ]):
        return "measurement-special"

    if any(token in title for token in [
        "หนี้สินที่อาจเกิดขึ้น",
        "คดีอาหารเป็นพิษ",
        "Not Probable",
        "Possible Obligation",
        "Contingent Liability",
        "Contingent Asset",
        "สินทรัพย์ที่อาจเกิดขึ้น",
        "ความย้อนแย้งของความน่าจะเป็น",
        "วิวัฒนาการสู่การเป็นสินทรัพย์ที่แท้จริง",
        "ขั้วตรงข้ามของความไม่แน่นอน",
    ]):
        return "contingencies"

    return "disclosure-wrap"


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
        sections.append(
            Section(
                section_id=slugify(current_title, index),
                title=current_title,
                body_html=body_html,
                group_id=classify_group(current_title),
                theme=section_theme(current_title),
            )
        )
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


def clean_short_title(title: str) -> str:
    title = re.sub(r"^ส่วนที่\s*\d+:\s*", "", title).strip()
    title = re.sub(r"^ข้อ\s*\d+:\s*", "", title).strip()
    title = re.sub(r"^แบบที่\s*\d+:\s*", "", title).strip()
    return title


def prune_noise(fragment: BeautifulSoup) -> None:
    for tag in fragment.find_all(["p", "li"]):
        text = tag.get_text(" ", strip=True)
        if not text:
            tag.decompose()
            continue
        if tag.name == "p" and is_conversational_line(text):
            tag.decompose()
            continue
        if text.startswith("คำสั่ง:") or any(marker in text for marker in PRACTICE_TEXT_MARKERS):
            tag.decompose()

    for tag in fragment.find_all(["ul", "ol"]):
        if not tag.find_all("li", recursive=False):
            tag.decompose()

    for tag in fragment.find_all("hr"):
        if not tag.find_previous_sibling() or not tag.find_next_sibling():
            tag.decompose()


def wrap_structural_nodes(fragment: BeautifulSoup) -> None:
    for table in fragment.find_all("table"):
        parent = table.parent
        if parent and parent.name == "div" and "table-wrap" in parent.get("class", []):
            continue
        wrapper = fragment.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrapper)

    for pre in fragment.find_all("pre"):
        parent = pre.parent
        if parent and parent.name == "div" and "ledger-block" in parent.get("class", []):
            continue
        wrapper = fragment.new_tag("div", attrs={"class": "ledger-block"})
        pre.wrap(wrapper)


def tone_for(title: str) -> str:
    lowered = title.lower()
    if any(token in title for token in ["กับดัก", "หลุมพราง", "จุดหลอก", "ความย้อนแย้ง"]):
        return "trap"
    if any(token in title for token in ["กฎเหล็ก", "สิ่งที่ต้องรู้", "สำคัญ", "Decision Tree", "เมทริกซ์"]):
        return "alert"
    if any(token in title for token in ["ตัวอย่าง", "กรณีศึกษา", "ข้อ ", "แบบที่"]):
        return "example"
    if any(token in title for token in ["สรุป", "ภาพรวม", "Lifecycle", "Probability Matrix"]):
        return "summary"
    if any(token in lowered for token in ["why", "เหตุผล", "ทำไม", "หลักคิด", "logic"]):
        return "note"
    return "default"


def tone_label(tone: str) -> str:
    return {
        "trap": "TRAP",
        "alert": "RULE",
        "example": "CASE",
        "summary": "WRAP",
        "note": "NOTE",
        "default": "TOPIC",
    }[tone]


def render_subsection(title: str, nodes: list[Tag]) -> str:
    if any(marker in title for marker in PRACTICE_TITLE_MARKERS):
        return ""
    tone = tone_for(title)
    body = "".join(str(node) for node in nodes).strip()
    if not body:
        return ""
    return (
        f'<article class="subsection {tone}">'
        f'<div class="subsection-head"><span class="subsection-label">{tone_label(tone)}</span>'
        f"<h3>{html.escape(title)}</h3></div>"
        f'<div class="subsection-body prose">{body}</div>'
        f"</article>"
    )


def render_section(section: Section, index: int) -> str:
    fragment = BeautifulSoup(section.body_html, "html.parser")
    prune_noise(fragment)
    wrap_structural_nodes(fragment)

    children = [child for child in fragment.children if isinstance(child, Tag)]
    intro_nodes: list[Tag] = []
    subsections: list[tuple[str, list[Tag]]] = []
    current_subtitle = ""
    current_nodes: list[Tag] = []

    for node in children:
        if node.name == "h3":
            if current_subtitle:
                subsections.append((current_subtitle, current_nodes))
            current_subtitle = node.get_text(" ", strip=True)
            current_nodes = []
            continue

        if current_subtitle:
            current_nodes.append(node)
        else:
            intro_nodes.append(node)

    if current_subtitle:
        subsections.append((current_subtitle, current_nodes))

    intro_html = "".join(str(node) for node in intro_nodes).strip()
    subsection_html = "".join(render_subsection(title, nodes) for title, nodes in subsections if nodes)

    if not intro_html and not subsection_html:
        return ""

    body_parts = []
    if intro_html:
        body_parts.append(f'<div class="section-intro prose">{intro_html}</div>')
    if subsection_html:
        body_parts.append(subsection_html)

    body = "".join(body_parts).strip()
    short_title = clean_short_title(section.title)

    return f"""
    <section class="sheet-section {section.theme}" id="{section.section_id}" data-title="{html.escape(short_title)}">
      <div class="section-rule"></div>
      <header class="section-head">
        <p class="section-kicker">ตอนที่ {index:02d}</p>
        <h2>{html.escape(short_title)}</h2>
      </header>
      {body}
    </section>
    """


def render_group(group: GroupSpec, sections: list[Section], index: int) -> str:
    kept_sections: list[tuple[Section, str]] = []
    for idx, section in enumerate(sections, start=1):
        rendered = render_section(section, idx)
        if rendered.strip():
            kept_sections.append((section, rendered))

    if not kept_sections:
        return ""

    group_nav = "".join(
        f'<a class="group-link" href="#{section.section_id}">{html.escape(clean_short_title(section.title))}</a>'
        for section, _ in kept_sections
    )
    section_html = "\n".join(rendered for _, rendered in kept_sections)

    return f"""
    <section class="sheet-group" id="{group.group_id}" data-group-title="{html.escape(group.title)}">
      <div class="group-head">
        <div class="group-meta">
          <p class="group-kicker">ชุดที่ {index:02d}</p>
          <p class="group-kicker">{len(kept_sections)} หัวข้อ</p>
        </div>
        <h2>{html.escape(group.title)}</h2>
        <p class="group-description">{html.escape(group.description)}</p>
        <div class="group-nav">
          {group_nav}
        </div>
      </div>
      <div class="group-body">
        {section_html}
      </div>
    </section>
    """


def build_html(md_text: str) -> str:
    article_html = render_markdown(md_text)
    sections = build_sections(article_html)
    grouped_sections: dict[str, list[Section]] = {spec.group_id: [] for spec in GROUP_SPECS}
    for section in sections:
        grouped_sections[section.group_id].append(section)

    mini_nav = "".join(
        f'<a href="#{spec.group_id}" class="mini-link" data-target="{spec.group_id}" title="{html.escape(spec.description)}">{html.escape(spec.nav_label)}</a>'
        for spec in GROUP_SPECS
        if grouped_sections[spec.group_id]
    )
    quick_frame = "".join(
        f'<div class="formula-item"><span>{html.escape(label)}</span><strong>{html.escape(value)}</strong></div>'
        for label, value in QUICK_FRAME
    )
    groups_html = "\n".join(
        render_group(spec, grouped_sections[spec.group_id], idx)
        for idx, spec in enumerate(GROUP_SPECS, start=1)
        if grouped_sections[spec.group_id]
    )
    pills_html = "".join(f"<span>{html.escape(pill)}</span>" for pill in PILLS)

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
      --bg:#f4efe6;
      --paper:#fffaf1;
      --paper-soft:#fbf5ea;
      --ink:#2f231a;
      --ink-strong:#21170f;
      --muted:#6f6254;
      --line:rgba(120,99,78,0.16);
      --line-strong:rgba(120,99,78,0.3);
      --accent:#7c8160;
      --accent-soft:rgba(124,137,96,0.12);
      --shadow:0 14px 28px rgba(76,56,37,0.045);
      --font-sans:"Google Sans Text","Google Sans","Product Sans","Noto Sans Thai",sans-serif;
      --font-mono:"Google Sans Code","SFMono-Regular",Consolas,monospace;
      --max:1160px;
    }}
    * {{ box-sizing:border-box; }}
    html {{
      scroll-behavior:smooth;
      width:100%;
      max-width:100%;
      overflow-x:hidden;
    }}
    body {{
      margin:0;
      width:100%;
      max-width:100%;
      overflow-x:hidden;
      color:var(--ink);
      font-family:var(--font-sans);
      background:
        linear-gradient(90deg, transparent 0, transparent 72px, rgba(160,122,88,0.07) 72px, rgba(160,122,88,0.07) 74px, transparent 74px),
        repeating-linear-gradient(180deg, transparent 0, transparent 38px, rgba(120,99,78,0.06) 38px, rgba(120,99,78,0.06) 39px),
        radial-gradient(circle at top left, rgba(255,255,255,0.42), transparent 34%),
        var(--bg);
      line-height:1.78;
      letter-spacing:-0.01em;
    }}
    body::before {{
      content:"";
      position:fixed;
      inset:0;
      pointer-events:none;
      opacity:0.18;
      background-image:radial-gradient(rgba(90,67,47,0.18) 0.45px, transparent 0.45px);
      background-size:9px 9px;
      mask-image:linear-gradient(to bottom, rgba(0,0,0,0.3), transparent 35%);
    }}
    a {{ color:inherit; text-decoration:none; }}
    code, pre {{ font-family:var(--font-mono); }}
    .page {{
      width:min(calc(100% - 32px), var(--max));
      max-width:100%;
      margin:0 auto;
      padding:28px 0 80px;
    }}
    .masthead {{
      padding:18px 0 16px;
      border-bottom:1px solid var(--line);
      margin-bottom:8px;
    }}
    .eyebrow {{
      margin:0 0 10px;
      color:var(--muted);
      font-size:0.82rem;
      letter-spacing:0.16em;
      text-transform:uppercase;
      font-weight:700;
    }}
    .hero {{
      display:grid;
      grid-template-columns:minmax(0, 1.35fr) minmax(280px, 0.65fr);
      gap:28px;
      align-items:end;
      min-width:0;
    }}
    .hero h1 {{
      margin:0;
      font-size:clamp(2.25rem, 5.6vw, 4.45rem);
      line-height:0.98;
      letter-spacing:-0.05em;
      color:#36261c;
    }}
    .hero p {{
      margin:12px 0 0;
      max-width:62ch;
      color:#4a3a2d;
      font-size:1.02rem;
      line-height:1.72;
    }}
    .subject-line {{
      display:flex;
      flex-wrap:wrap;
      gap:10px;
      margin-top:16px;
      color:var(--muted);
      font-size:0.84rem;
    }}
    .subject-line span {{
      padding:7px 11px;
      border:1px solid var(--line);
      border-radius:999px;
      background:rgba(255,255,255,0.38);
    }}
    .formula-strip {{
      padding:16px 18px;
      border:1px solid var(--line);
      border-radius:22px;
      background:linear-gradient(180deg, rgba(255,250,241,0.86), rgba(250,244,233,0.74));
      box-shadow:0 10px 20px rgba(76,56,37,0.03);
      min-width:0;
    }}
    .formula-strip h2 {{
      margin:0 0 10px;
      font-size:0.92rem;
      letter-spacing:0.08em;
      text-transform:uppercase;
      color:#554538;
    }}
    .formula-item {{
      display:grid;
      grid-template-columns:96px minmax(0,1fr);
      gap:10px;
      padding:8px 0;
      border-top:1px dashed var(--line);
      min-width:0;
    }}
    .formula-item:first-of-type {{ border-top:0; padding-top:0; }}
    .formula-item span {{
      color:var(--muted);
      font-size:0.82rem;
      text-transform:uppercase;
      letter-spacing:0.08em;
      font-weight:700;
    }}
    .formula-item strong {{
      color:var(--ink);
      font-size:0.94rem;
      line-height:1.45;
    }}
    .mini-nav-shell {{
      position:sticky;
      top:0;
      z-index:30;
      max-width:100%;
      overflow:hidden;
      padding:10px 0 18px;
      background:linear-gradient(180deg, rgba(245,239,228,0.96), rgba(245,239,228,0.78), rgba(245,239,228,0));
      backdrop-filter:blur(8px);
    }}
    .mini-nav {{
      display:flex;
      gap:10px;
      max-width:100%;
      overflow:auto;
      padding:10px 4px 10px 2px;
      scrollbar-width:none;
      -webkit-overflow-scrolling:touch;
      overscroll-behavior-x:contain;
    }}
    .mini-nav::-webkit-scrollbar {{ display:none; }}
    .mini-link {{
      white-space:nowrap;
      padding:10px 14px;
      border-radius:999px;
      border:1px solid var(--line);
      color:var(--muted);
      background:rgba(255,250,241,0.78);
      transition:180ms ease;
      font-size:0.95rem;
    }}
    .mini-link:hover,
    .mini-link:focus-visible {{
      border-color:var(--line-strong);
      color:var(--ink);
      transform:translateY(-1px);
    }}
    .mini-link.is-active {{
      background:#efe4cf;
      border-color:rgba(124,137,96,0.4);
      color:#2f271f;
    }}
    .content {{
      display:grid;
      gap:22px;
      min-width:0;
      max-width:100%;
    }}
    .sheet-group {{
      display:grid;
      gap:16px;
      padding-top:4px;
      min-width:0;
      max-width:100%;
    }}
    .group-head {{
      padding:17px 20px 15px;
      border:1px solid var(--line);
      border-radius:24px;
      background:linear-gradient(180deg, rgba(255,250,241,0.86), rgba(250,244,233,0.7));
      box-shadow:0 10px 20px rgba(76,56,37,0.03);
      position:relative;
      min-width:0;
      max-width:100%;
    }}
    .group-head::after {{
      content:"";
      position:absolute;
      left:20px;
      right:20px;
      bottom:0;
      height:1px;
      background:linear-gradient(90deg, rgba(123,133,100,0.16), rgba(123,133,100,0));
    }}
    .group-meta {{
      display:flex;
      flex-wrap:wrap;
      justify-content:space-between;
      gap:8px 16px;
      align-items:baseline;
    }}
    .group-kicker {{
      margin:0;
      color:var(--muted);
      text-transform:uppercase;
      letter-spacing:0.16em;
      font-size:0.72rem;
      font-weight:700;
    }}
    .group-head h2 {{
      margin:0;
      font-size:clamp(1.55rem, 2.2vw, 2.2rem);
      line-height:1.08;
      letter-spacing:-0.04em;
      color:#2f2219;
    }}
    .group-description {{
      margin:10px 0 0;
      max-width:68ch;
      color:var(--muted);
      font-size:0.97rem;
      line-height:1.68;
    }}
    .group-nav {{
      display:grid;
      grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));
      gap:8px;
      margin-top:12px;
      padding-top:2px;
      min-width:0;
      max-width:100%;
    }}
    .group-link {{
      padding:9px 11px;
      border-radius:14px;
      border:1px solid var(--line);
      background:rgba(255,250,241,0.6);
      color:var(--muted);
      font-size:0.86rem;
      line-height:1.35;
      transition:180ms ease;
    }}
    .group-link:hover,
    .group-link:focus-visible {{
      color:var(--ink);
      border-color:var(--line-strong);
      background:rgba(255,250,241,0.88);
    }}
    .group-link.is-current {{
      color:#2f271f;
      background:rgba(123,133,100,0.12);
      border-color:rgba(123,133,100,0.26);
    }}
    .group-body {{
      display:grid;
      gap:18px;
      min-width:0;
      max-width:100%;
    }}
    .sheet-section {{
      position:relative;
      padding:26px clamp(18px, 2vw, 28px) 28px 26px;
      border:1px solid var(--line);
      border-radius:24px;
      background:linear-gradient(180deg, rgba(255,250,241,0.92), rgba(255,248,236,0.8));
      box-shadow:var(--shadow);
      overflow:clip;
      min-width:0;
      max-width:100%;
    }}
    .sheet-section.theme-accounting {{
      background:linear-gradient(180deg, rgba(255,250,241,0.92), rgba(248,241,230,0.84));
    }}
    .sheet-section.theme-disclosure {{
      background:linear-gradient(180deg, rgba(255,250,241,0.9), rgba(244,240,230,0.8));
    }}
    .sheet-section.theme-review {{
      background:linear-gradient(180deg, rgba(255,250,241,0.9), rgba(245,244,236,0.84));
    }}
    .sheet-section::before {{
      content:"";
      position:absolute;
      inset:0;
      pointer-events:none;
      background:linear-gradient(180deg, rgba(255,255,255,0.45), transparent 24%);
    }}
    .section-rule {{
      position:absolute;
      left:0;
      top:0;
      bottom:0;
      width:10px;
      background:linear-gradient(180deg, rgba(124,137,96,0.16), rgba(124,137,96,0.02));
    }}
    .section-head {{
      position:relative;
      padding-left:8px;
      margin-bottom:14px;
    }}
    .section-kicker {{
      margin:0 0 7px;
      color:var(--muted);
      text-transform:uppercase;
      letter-spacing:0.16em;
      font-size:0.72rem;
      font-weight:700;
    }}
    .section-head h2 {{
      margin:0;
      font-size:clamp(1.4rem, 2vw, 2rem);
      line-height:1.15;
      letter-spacing:-0.03em;
      overflow-wrap:anywhere;
    }}
    .section-intro {{
      margin-bottom:12px;
    }}
    .section-intro > p:first-child {{
      font-size:1.02rem;
      color:#4a392d;
      line-height:1.74;
    }}
    .prose p {{
      margin:0 0 11px;
    }}
    .prose ul,
    .prose ol {{
      margin:0 0 12px 0;
      padding-left:1.05rem;
    }}
    .prose li {{
      margin-bottom:7px;
      padding-left:2px;
      line-height:1.7;
    }}
    .prose h4 {{
      margin:18px 0 8px;
      font-size:0.98rem;
      line-height:1.4;
      color:#49382c;
    }}
    .prose strong {{
      color:#2c2018;
    }}
    .subsection {{
      margin-top:16px;
      padding:17px;
      border-top:1px solid var(--line);
      background:rgba(255,252,246,0.5);
      min-width:0;
      max-width:100%;
    }}
    .subsection-head {{
      display:flex;
      align-items:baseline;
      flex-wrap:wrap;
      gap:9px 10px;
      margin-bottom:11px;
    }}
    .subsection-label {{
      color:var(--muted);
      letter-spacing:0.14em;
      text-transform:uppercase;
      font-size:0.7rem;
      font-weight:800;
    }}
    .subsection h3 {{
      margin:0;
      font-size:1.08rem;
      line-height:1.35;
      overflow-wrap:anywhere;
    }}
    .subsection.trap {{
      background:linear-gradient(180deg, rgba(154,93,67,0.08), rgba(255,252,246,0.52));
      border-left:3px solid rgba(154,93,67,0.46);
      padding-left:16px;
    }}
    .subsection.alert {{
      background:linear-gradient(180deg, rgba(124,137,96,0.12), rgba(255,252,246,0.52));
      border-left:3px solid rgba(124,137,96,0.48);
      padding-left:16px;
    }}
    .subsection.summary {{
      background:linear-gradient(180deg, rgba(124,137,96,0.08), rgba(255,252,246,0.52));
    }}
    .subsection.example {{
      background:linear-gradient(180deg, rgba(98,86,73,0.08), rgba(255,252,246,0.52));
    }}
    .subsection.note {{
      background:linear-gradient(180deg, rgba(197,172,126,0.12), rgba(255,252,246,0.52));
    }}
    .table-wrap {{
      overflow:auto;
      max-width:100%;
      margin:12px 0 16px;
      border:1px solid var(--line);
      border-radius:16px;
      background:rgba(255,255,255,0.52);
      position:relative;
      -webkit-overflow-scrolling:touch;
      overscroll-behavior-x:contain;
    }}
    .table-wrap::after {{
      content:"";
      position:sticky;
      right:0;
      top:0;
      float:right;
      width:18px;
      height:100%;
      pointer-events:none;
      background:linear-gradient(90deg, rgba(255,255,255,0), rgba(244,237,225,0.92));
    }}
    table {{
      width:100%;
      border-collapse:collapse;
      min-width:640px;
      font-size:0.94rem;
      line-height:1.58;
      font-variant-numeric:tabular-nums;
    }}
    th, td {{
      padding:12px 14px;
      vertical-align:top;
      border-bottom:1px solid rgba(120,99,78,0.12);
      text-align:left;
    }}
    th {{
      background:rgba(124,137,96,0.08);
      font-weight:700;
      position:sticky;
      top:0;
      z-index:2;
      backdrop-filter:blur(2px);
    }}
    tbody tr:nth-child(even) td {{
      background:rgba(255,252,246,0.42);
    }}
    tr:hover td {{
      background:rgba(124,137,96,0.06);
    }}
    .ledger-block {{
      margin:12px 0 16px;
      padding:15px 16px;
      background:#f7f0e6;
      border:1px solid var(--line);
      border-radius:18px;
      overflow:auto;
      max-width:100%;
      -webkit-overflow-scrolling:touch;
      overscroll-behavior-x:contain;
    }}
    .ledger-block code {{
      font-family:var(--font-mono);
      font-size:0.95rem;
      line-height:1.7;
      white-space:pre;
      display:block;
      color:#2f241d;
    }}
    blockquote {{
      margin:14px 0;
      padding:12px 16px;
      border-left:3px solid rgba(124,137,96,0.35);
      background:rgba(255,255,255,0.34);
      color:var(--muted);
    }}
    .sheet-section:target {{
      border-color:rgba(123,133,100,0.34);
      box-shadow:0 0 0 1px rgba(123,133,100,0.1), 0 14px 28px rgba(76,56,37,0.045);
    }}
    .footer-note {{
      color:var(--muted);
      font-size:0.95rem;
      padding:20px 0 0;
      text-align:center;
    }}
    @media (max-width: 980px) {{
      .hero {{
        grid-template-columns:1fr;
      }}
      .formula-strip {{
        order:2;
      }}
      .group-nav {{
        grid-template-columns:repeat(2, minmax(0,1fr));
      }}
    }}
    @media (max-width: 720px) {{
      .page {{
        width:min(calc(100% - 24px), var(--max));
        padding:20px 0 56px;
      }}
      .hero h1 {{
        font-size:clamp(2rem, 11vw, 3.2rem);
      }}
      .group-nav {{
        grid-template-columns:1fr;
      }}
      .formula-item {{
        grid-template-columns:1fr;
        gap:2px;
      }}
      .section-head h2 {{
        font-size:1.28rem;
      }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior:auto; }}
      *, *::before, *::after {{ transition:none !important; animation:none !important; }}
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
          <div class="subject-line">{pills_html}</div>
        </div>
        <aside class="formula-strip" aria-label="กรอบจำเร็ว">
          <h2>กรอบจำเร็ว</h2>
          {quick_frame}
        </aside>
      </div>
    </header>

    <div class="mini-nav-shell">
      <nav class="mini-nav" aria-label="สารบัญย่อ">
        {mini_nav}
      </nav>
    </div>

    <main class="content">
      {groups_html}
    </main>

    <p class="footer-note">{html.escape(PAGE_DESCRIPTION)}</p>
  </div>

  <script>
    const groups = [...document.querySelectorAll('.sheet-group')];
    const sections = [...document.querySelectorAll('.sheet-section')];
    const navLinks = [...document.querySelectorAll('.mini-link')];
    const groupLinks = [...document.querySelectorAll('.group-link')];
    const navMap = Object.fromEntries(navLinks.map(link => [link.dataset.target, link]));
    const sectionMap = Object.fromEntries(groupLinks.map(link => [link.getAttribute('href').slice(1), link]));

    const navObserver = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        const link = navMap[entry.target.id];
        if (!link || !entry.isIntersecting) return;
        navLinks.forEach(item => item.classList.remove('is-active'));
        link.classList.add('is-active');
      }});
    }}, {{ rootMargin: '-25% 0px -60% 0px', threshold: 0 }});
    groups.forEach(group => navObserver.observe(group));

    const sectionObserver = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        const link = sectionMap[entry.target.id];
        if (!link || !entry.isIntersecting) return;
        groupLinks.forEach(item => item.classList.remove('is-current'));
        link.classList.add('is-current');
      }});
    }}, {{ threshold: 0.18 }});
    sections.forEach(section => sectionObserver.observe(section));
  </script>
</body>
</html>
"""


def main() -> None:
    md_text = build_markdown()
    html_text = build_html(md_text)
    OUT_HTML.write_text(html_text, encoding="utf-8")
    print(OUT_HTML)


if __name__ == "__main__":
    main()
