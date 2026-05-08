from pathlib import Path
import re

import markdown
from bs4 import BeautifulSoup, Tag


SRC = Path(r"D:\Fogust\Workspace\College\AC311\08 Investment Property - Exam Sheet.md")
OUT = Path(r"D:\Fogust\Workspace\College\AC311\08 Investment Property - Exam Sheet.html")


SUBTITLE = (
    "\u0e0a\u0e35\u0e17\u0e2d\u0e48\u0e32\u0e19\u0e2a\u0e2d\u0e1a\u0e41\u0e1a\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27 "
    "\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e17\u0e1a\u0e17\u0e27\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32\u0e2b\u0e49\u0e2d\u0e07\u0e2a\u0e2d\u0e1a"
)
DESCRIPTION = (
    "\u0e0a\u0e35\u0e17\u0e2d\u0e48\u0e32\u0e19\u0e2a\u0e2d\u0e1a\u0e27\u0e34\u0e0a\u0e32 AC311 \u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07 Investment Property "
    "\u0e41\u0e1a\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27 \u0e1e\u0e23\u0e49\u0e2d\u0e21 Dr./Cr. \u0e41\u0e25\u0e30\u0e15\u0e32\u0e23\u0e32\u0e07\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a"
)
EYEBROW = "AC311 Intermediate Accounting"
SUBJECT_PILLS = [
    "Single-page exam sheet",
    "\u0e04\u0e23\u0e1a\u0e40\u0e19\u0e37\u0e49\u0e2d\u0e2b\u0e32 + \u0e2a\u0e41\u0e01\u0e19\u0e40\u0e23\u0e47\u0e27",
    "Dr./Cr. \u0e1e\u0e23\u0e49\u0e2d\u0e21\u0e17\u0e27\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e2d\u0e1a",
]
QUICK_FRAME_TITLE = "Quick Frame"
NAV_ARIA = "\u0e2a\u0e32\u0e23\u0e1a\u0e31\u0e0d\u0e22\u0e48\u0e2d"
QUICK_REVIEW_TITLE = "\u0e40\u0e0a\u0e47\u0e01\u0e25\u0e34\u0e2a\u0e15\u0e4c\u0e01\u0e48\u0e2d\u0e19\u0e40\u0e02\u0e49\u0e32\u0e2b\u0e49\u0e2d\u0e07\u0e2a\u0e2d\u0e1a"
QUICK_REVIEW_TEXT = (
    "\u0e2a\u0e41\u0e01\u0e19\u0e40\u0e09\u0e1e\u0e32\u0e30\u0e2b\u0e31\u0e27\u0e02\u0e49\u0e2d\u0e19\u0e35\u0e49\u0e23\u0e2d\u0e1a\u0e2a\u0e38\u0e14\u0e17\u0e49\u0e32\u0e22 "
    "\u0e40\u0e1e\u0e37\u0e48\u0e2d\u0e40\u0e0a\u0e47\u0e01\u0e27\u0e48\u0e32\u0e41\u0e19\u0e27\u0e04\u0e34\u0e14\u0e2b\u0e25\u0e31\u0e01\u0e22\u0e31\u0e07\u0e44\u0e21\u0e48\u0e2b\u0e25\u0e38\u0e14\u0e08\u0e32\u0e01\u0e2b\u0e31\u0e27"
)
FOOTER_NOTE = (
    "\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27\u0e19\u0e35\u0e49\u0e43\u0e0a\u0e49\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e08\u0e32\u0e01\u0e44\u0e1f\u0e25\u0e4c\u0e2a\u0e23\u0e38\u0e1b\u0e17\u0e35\u0e48\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49\u0e2d\u0e31\u0e1b\u0e42\u0e2b\u0e25\u0e14\u0e40\u0e1b\u0e47\u0e19\u0e10\u0e32\u0e19\u0e2b\u0e25\u0e31\u0e01\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14 "
    "\u0e41\u0e25\u0e30\u0e08\u0e31\u0e14\u0e43\u0e2b\u0e21\u0e48\u0e43\u0e2b\u0e49\u0e2d\u0e48\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e0a\u0e35\u0e17\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e2d\u0e1a\u0e43\u0e19\u0e23\u0e39\u0e1b\u0e41\u0e1a\u0e1a\u0e40\u0e27\u0e47\u0e1a"
)

QUICK_FORMULAE = [
    ("\u0e27\u0e31\u0e19\u0e41\u0e23\u0e01", "\u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49\u0e14\u0e49\u0e27\u0e22 Cost"),
    ("\u0e2b\u0e25\u0e31\u0e07\u0e08\u0e32\u0e01\u0e19\u0e31\u0e49\u0e19", "\u0e40\u0e25\u0e37\u0e2d\u0e01 Cost \u0e2b\u0e23\u0e37\u0e2d Fair Value \u0e41\u0e25\u0e30\u0e43\u0e0a\u0e49\u0e17\u0e31\u0e49\u0e07\u0e01\u0e25\u0e38\u0e48\u0e21"),
    ("\u0e42\u0e2d\u0e19", "\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35 change in use + evidence"),
    ("\u0e08\u0e33\u0e2b\u0e19\u0e48\u0e32\u0e22", "proceeds - carrying amount -> P&L"),
]

CHECK_ITEMS = [
    "\u0e08\u0e33\u0e44\u0e14\u0e49\u0e27\u0e48\u0e32 <code>\u0e27\u0e31\u0e19\u0e41\u0e23\u0e01 = Cost</code> \u0e40\u0e2a\u0e21\u0e2d",
    "\u0e41\u0e22\u0e01 <code>Investment Property</code>, <code>PPE</code>, <code>Inventory</code> \u0e44\u0e14\u0e49\u0e0a\u0e31\u0e14",
    "\u0e23\u0e39\u0e49\u0e15\u0e48\u0e32\u0e07\u0e01\u0e31\u0e19\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07 <code>Replacement</code> \u0e01\u0e31\u0e1a <code>Day-to-day servicing</code>",
    "\u0e44\u0e21\u0e48\u0e25\u0e37\u0e21\u0e27\u0e48\u0e32 <code>Fair Value Model</code> \u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e48\u0e32\u0e07\u0e40\u0e02\u0e49\u0e32 <code>P&amp;L</code>",
    "\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e01\u0e32\u0e23\u0e42\u0e2d\u0e19\u0e15\u0e49\u0e2d\u0e07\u0e21\u0e35 <code>change in use + evidence</code>",
    "\u0e23\u0e39\u0e49\u0e27\u0e48\u0e32\u0e01\u0e23\u0e13\u0e35 <code>PPE -&gt; IP (fair value)</code> \u0e15\u0e49\u0e2d\u0e07\u0e1c\u0e48\u0e32\u0e19\u0e01\u0e15\u0e34\u0e01\u0e32 PPE \u0e01\u0e48\u0e2d\u0e19",
    "\u0e08\u0e33\u0e2a\u0e39\u0e15\u0e23\u0e08\u0e33\u0e2b\u0e19\u0e48\u0e32\u0e22\u0e44\u0e14\u0e49: <code>proceeds - carrying amount</code>",
    "\u0e08\u0e33 disclosure \u0e2b\u0e25\u0e31\u0e01: <code>rental income</code>, <code>direct operating expenses</code>, <code>fair value</code>",
]

GROUP_SPECS = [
    {
        "id": "foundations",
        "title": "\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e41\u0e22\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17",
        "description": "\u0e40\u0e23\u0e34\u0e48\u0e21\u0e08\u0e32\u0e01\u0e19\u0e34\u0e22\u0e32\u0e21 \u0e02\u0e2d\u0e1a\u0e40\u0e02\u0e15 \u0e41\u0e25\u0e30\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e17\u0e35\u0e48\u0e21\u0e31\u0e01\u0e43\u0e0a\u0e49\u0e41\u0e22\u0e01\u0e27\u0e48\u0e32\u0e40\u0e1b\u0e47\u0e19\u0e2b\u0e23\u0e37\u0e2d\u0e44\u0e21\u0e48\u0e40\u0e1b\u0e47\u0e19 Investment Property",
        "numbers": [1, 2, 5, 6, 7, 3, 4, 8],
    },
    {
        "id": "recognition-cost",
        "title": "Recognition \u0e41\u0e25\u0e30\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19",
        "description": "\u0e15\u0e48\u0e2d\u0e14\u0e49\u0e27\u0e22\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23 \u0e01\u0e32\u0e23\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e41\u0e23\u0e01 \u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e41\u0e22\u0e01 replacement \u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01 day-to-day servicing",
        "numbers": [9, 10, 11, 12, 13],
    },
    {
        "id": "measurement-models",
        "title": "\u0e01\u0e32\u0e23\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e41\u0e25\u0e30\u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22",
        "description": "\u0e08\u0e31\u0e14 Cost model \u0e41\u0e25\u0e30 Fair value model \u0e44\u0e27\u0e49\u0e14\u0e49\u0e27\u0e22\u0e01\u0e31\u0e19 \u0e23\u0e27\u0e21\u0e17\u0e31\u0e49\u0e07\u0e1c\u0e39\u0e49\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e23\u0e32\u0e04\u0e32\u0e41\u0e25\u0e30\u0e40\u0e07\u0e37\u0e48\u0e2d\u0e19\u0e44\u0e02\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22",
        "numbers": [14, 15, 16, 19, 17, 18],
    },
    {
        "id": "transfers",
        "title": "Transfers \u0e41\u0e25\u0e30\u0e01\u0e23\u0e13\u0e35\u0e42\u0e2d\u0e19\u0e0b\u0e31\u0e1a\u0e0b\u0e49\u0e2d\u0e19",
        "description": "\u0e23\u0e27\u0e21 change in use, evidence, \u0e01\u0e32\u0e23\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e42\u0e2d\u0e19 \u0e41\u0e25\u0e30\u0e01\u0e23\u0e13\u0e35 PPE -> IP \u0e17\u0e35\u0e48\u0e2d\u0e2d\u0e01\u0e2a\u0e2d\u0e1a\u0e1a\u0e48\u0e2d\u0e22",
        "numbers": [20, 21, 22, 23, 24, 25, 26, 27],
    },
    {
        "id": "ending-and-disclosure",
        "title": "\u0e1b\u0e25\u0e32\u0e22\u0e17\u0e32\u0e07\u0e02\u0e2d\u0e07\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23",
        "description": "\u0e14\u0e39\u0e40\u0e23\u0e37\u0e48\u0e2d\u0e07 compensation, disposal, \u0e41\u0e25\u0e30 disclosure \u0e43\u0e2b\u0e49\u0e08\u0e1a\u0e40\u0e1b\u0e47\u0e19\u0e01\u0e49\u0e2d\u0e19\u0e40\u0e14\u0e35\u0e22\u0e27",
        "numbers": [28, 29, 30, 31, 32, 33, 34],
    },
    {
        "id": "exam-wrap-up",
        "title": "\u0e27\u0e07\u0e08\u0e23\u0e0a\u0e35\u0e27\u0e34\u0e15 Investment Property (IP)",
        "description": "\u0e2a\u0e23\u0e38\u0e1b phase \u0e17\u0e31\u0e49\u0e07\u0e27\u0e07\u0e08\u0e23\u0e15\u0e31\u0e49\u0e07\u0e41\u0e15\u0e48\u0e04\u0e31\u0e14\u0e01\u0e23\u0e2d\u0e07 \u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01 \u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32 \u0e42\u0e2d\u0e19 \u0e08\u0e33\u0e2b\u0e19\u0e48\u0e32\u0e22 \u0e08\u0e19\u0e16\u0e36\u0e07 disclosure \u0e43\u0e0a\u0e49\u0e17\u0e27\u0e19\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e2d\u0e1a\u0e44\u0e14\u0e49\u0e43\u0e19\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e14\u0e35\u0e22\u0e27",
        "numbers": [],
    },
]

GROUP_NAV_LABELS = {
    "foundations": "01 Basics",
    "recognition-cost": "02 Recognition",
    "measurement-models": "03 Models",
    "transfers": "04 Transfers",
    "ending-and-disclosure": "05 Closing",
    "exam-wrap-up": "06 Lifecycle",
}

MODULE_6_REPLACEMENT_HTML = """
<section class="sheet-section theme-review" id="ip-lifecycle-summary" data-title="วงจรชีวิต Investment Property (IP)">
  <div class="section-rule"></div>
  <header class="section-head">
    <p class="section-kicker">Part {part_number:02d}</p>
    <h2>วงจรชีวิต Investment Property (IP) สรุปจบในหน้าเดียว</h2>
  </header>
  <div class="section-intro prose">
    <p>ใช้ทวนทั้งบทแบบมองเป็นลำดับตั้งแต่คัดกรองรายการ จนถึงการจำหน่ายและการเปิดเผยข้อมูล โดยคง logic หลักที่มักออกสอบไว้ครบในหน้าเดียว</p>
  </div>

  <article class="subsection summary">
    <div class="subsection-head"><span class="subsection-label">PHASE 1</span><h3>คัดกรองจุดยืน (ใช่ หรือ ไม่ใช่ IP?)</h3></div>
    <div class="subsection-body prose">
      <ul>
        <li><strong>ใช่ IP:</strong> ถือไว้เพื่อรับค่าเช่า หรือ รอราคาขึ้น เช่น อพาร์ตเมนต์ หรือที่ดินว่างเปล่า</li>
        <li><strong>ไม่ใช่ IP:</strong> ใช้งานเอง หรือมีบริการเสริมเยอะ จัดเป็น <code>PPE</code> เช่น โรงแรม หรือออฟฟิศบริษัท</li>
        <li><strong>ไม่ใช่ IP:</strong> มีไว้เพื่อขายตามปกติธุรกิจ จัดเป็น <code>Inventory</code> เช่น หมู่บ้านจัดสรร</li>
        <li><strong>ไม่ใช่ IP:</strong> ถ้าปล่อยเช่าแบบโอนความเสี่ยงไปแล้ว เป็น <code>Finance Lease</code> และตัดตึกออกจากงบ</li>
      </ul>
    </div>
  </article>

  <article class="subsection alert">
    <div class="subsection-head"><span class="subsection-label">PHASE 2</span><h3>วันแรกที่เข้าบ้าน (Initial Recognition)</h3></div>
    <div class="subsection-body prose">
      <p><strong>กฎเหล็ก:</strong> วันแรกต้องบันทึกด้วย <code>ราคาทุน (Cost)</code> เสมอ</p>
    </div>
  </article>

  <article class="subsection note">
    <div class="subsection-head"><span class="subsection-label">PHASE 3</span><h3>การดูแลระหว่างทาง (Subsequent Costs)</h3></div>
    <div class="subsection-body prose">
      <ul>
        <li><strong>เปลี่ยนชิ้นใหญ่ (Replacement):</strong> บวกทุนใหม่เข้าไป แล้วตัดมูลค่าบัญชีของเก่าทิ้ง</li>
        <li><strong>ซ่อมแซมรายวัน (Day-to-day servicing):</strong> รับรู้เป็น <code>ค่าใช้จ่าย (Expense)</code> ของงวด ห้ามบวกเข้าตึก</li>
      </ul>
    </div>
  </article>

  <article class="subsection example">
    <div class="subsection-head"><span class="subsection-label">PHASE 4</span><h3>ประเมินค่าสิ้นปี (Subsequent Measurement)</h3></div>
    <div class="subsection-body prose">
      <p>ต้องเลือกใช้วิธีใดวิธีหนึ่ง และบังคับใช้กับ <strong>IP ทุกชิ้นทั้งกลุ่ม</strong></p>
      <ul>
        <li><strong>สาย Cost Model:</strong> คิดค่าเสื่อมราคาปกติ แต่ยังต้องหา <code>Fair Value</code> มาเปิดเผยในหมายเหตุประกอบงบเสมอ</li>
        <li><strong>สาย Fair Value Model:</strong> ห้ามคิดค่าเสื่อมราคาเด็ดขาด และส่วนต่างราคาตลาดที่ขึ้นหรือลงให้รับรู้เข้า <code>P&amp;L</code> ทันที</li>
      </ul>
    </div>
  </article>

  <article class="subsection trap">
    <div class="subsection-head"><span class="subsection-label">PHASE 5</span><h3>เปลี่ยนใจย้ายหมวด (Transfers)</h3></div>
    <div class="subsection-body prose">
      <p><strong>กฎการโอน:</strong> จะโอนได้ต้องมี <code>การเปลี่ยนการใช้งานจริง + มีหลักฐาน</code> เท่านั้น แค่ผู้บริหารคิดเปลี่ยนใจเองยังโอนไม่ได้</p>
      <blockquote>จุดสลบปราบเซียน: โอน <code>PPE</code> เปลี่ยนเป็น <code>IP (Fair Value)</code></blockquote>
      <ul>
        <li><strong>ก่อนโอน:</strong> ต้องตีราคาแบบทิ้งทวนด้วยกฎของ <code>PPE</code> ก่อน ถ้าราคาขึ้นให้เอากำไรไปไว้ใน <code>OCI / Revaluation surplus</code></li>
        <li><strong>หลังโอน:</strong> เมื่อกลายเป็น <code>IP</code> แล้ว ราคาที่ขึ้นหรือลงหลังจากนั้นจึงค่อยวิ่งเข้า <code>P&amp;L</code></li>
      </ul>
    </div>
  </article>

  <article class="subsection default">
    <div class="subsection-head"><span class="subsection-label">PHASE 6</span><h3>ขายทิ้ง / พังทลาย (Disposals)</h3></div>
    <div class="subsection-body prose">
      <p><strong>สูตรคำนวณ:</strong> <code>เงินที่ได้สุทธิ (Proceeds) - มูลค่าบัญชี (Carrying amount) = กำไร/ขาดทุน</code></p>
      <p>ส่วนต่างนี้ให้รับรู้เข้า <code>P&amp;L</code> ทันที</p>
    </div>
  </article>

  <article class="subsection note">
    <div class="subsection-head"><span class="subsection-label">PHASE 7</span><h3>เล่าให้นักลงทุนฟัง (Disclosure)</h3></div>
    <div class="subsection-body prose">
      <ul>
        <li>ต้องเปิดเผยนโยบายที่ใช้ว่าเป็น <code>Cost</code> หรือ <code>Fair Value</code> และบอกมูลค่ายุติธรรม</li>
        <li>ต้องแยก <code>Rental income</code> และ <code>Direct operating expenses</code> ให้ชัด</li>
        <li>ต้องแยกค่าใช้จ่ายของ <strong>ตึกที่มีคนเช่า</strong> ออกจาก <strong>ตึกที่ว่างเปล่า</strong> ด้วย</li>
      </ul>
    </div>
  </article>

  <article class="subsection alert">
    <div class="subsection-head"><span class="subsection-label">EXAM TRICK</span><h3>ทริคในห้องสอบ</h3></div>
    <div class="subsection-body prose">
      <p>ถ้าเจอโจทย์หลอก ให้ท่องไว้เสมอว่า <strong>Fair Value ของบทนี้ห้ามคิดค่าเสื่อม และกำไร/ขาดทุนวิ่งเข้า <code>P&amp;L</code> ล้วน ๆ</strong> ยกเว้นตอนโอนมาจาก <code>PPE</code></p>
    </div>
  </article>
</section>
"""


def slugify(text: str, fallback_index: int) -> str:
    slug = re.sub(r"<[^>]+>", "", text)
    slug = re.sub(r"[^\w\u0E00-\u0E7F]+", "-", slug, flags=re.UNICODE).strip("-").lower()
    return slug or f"section-{fallback_index}"


def tone_for(title: str) -> str:
    if any(k in title for k in ["\u0e08\u0e38\u0e14\u0e2a\u0e31\u0e1a\u0e2a\u0e19", "\u0e2b\u0e25\u0e38\u0e21\u0e1e\u0e23\u0e32\u0e07", "\u0e2b\u0e49\u0e32\u0e21\u0e17\u0e33", "\u0e02\u0e49\u0e2d\u0e04\u0e27\u0e23\u0e23\u0e30\u0e27\u0e31\u0e07", "\u0e02\u0e49\u0e2d\u0e40\u0e15\u0e37\u0e2d\u0e19"]):
        return "trap"
    if any(k in title for k in ["\u0e2b\u0e25\u0e31\u0e01\u0e08\u0e33", "\u0e08\u0e33\u0e07\u0e48\u0e32\u0e22", "\u0e2a\u0e23\u0e38\u0e1b", "\u0e2a\u0e39\u0e15\u0e23\u0e08\u0e33", "quick review", "checklist"]):
        return "summary"
    if any(k in title for k in ["\u0e01\u0e0e\u0e40\u0e2b\u0e25\u0e47\u0e01", "\u0e02\u0e49\u0e2d\u0e2a\u0e2d\u0e1a\u0e0a\u0e2d\u0e1a\u0e16\u0e32\u0e21"]):
        return "alert"
    if any(k in title for k in ["\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e2d\u0e2d\u0e01\u0e2a\u0e2d\u0e1a", "\u0e02\u0e49\u0e2d\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21"]):
        return "example"
    if any(k in title for k in ["\u0e2b\u0e25\u0e31\u0e01\u0e04\u0e34\u0e14", "\u0e41\u0e19\u0e27\u0e04\u0e34\u0e14", "\u0e40\u0e2b\u0e15\u0e38\u0e1c\u0e25", "\u0e1c\u0e39\u0e49\u0e1b\u0e23\u0e30\u0e40\u0e21\u0e34\u0e19\u0e23\u0e32\u0e04\u0e32"]):
        return "note"
    if re.search(r"^16\.", title):
        return "entry"
    return "default"


def short_nav(title: str) -> str:
    clean = re.sub(r"^\d+\)\s*", "", title).strip()
    mapping = [
        ("\u0e04\u0e33\u0e19\u0e34\u0e22\u0e32\u0e21\u0e41\u0e25\u0e30\u0e2b\u0e25\u0e31\u0e01\u0e41\u0e22\u0e01\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17", "\u0e04\u0e33\u0e19\u0e34\u0e22\u0e32\u0e21"),
        ("\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e40\u0e2a\u0e23\u0e34\u0e21", "\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23\u0e40\u0e2a\u0e23\u0e34\u0e21"),
        ("\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", "Recognition"),
        ("\u0e01\u0e32\u0e23\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e40\u0e23\u0e34\u0e48\u0e21\u0e41\u0e23\u0e01", "Initial Cost"),
        ("\u0e15\u0e49\u0e19\u0e17\u0e38\u0e19\u0e20\u0e32\u0e22\u0e2b\u0e25\u0e31\u0e07\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49", "Subsequent"),
        ("\u0e01\u0e32\u0e23\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e20\u0e32\u0e22\u0e2b\u0e25\u0e31\u0e07\u0e01\u0e32\u0e23\u0e23\u0e31\u0e1a\u0e23\u0e39\u0e49", "After Recognition"),
        ("Cost Model", "Cost Model"),
        ("Fair Value Model", "Fair Value"),
        ("\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e19\u0e42\u0e22\u0e1a\u0e32\u0e22\u0e1a\u0e31\u0e0d\u0e0a\u0e35", "Policy"),
        ("\u0e01\u0e32\u0e23\u0e42\u0e2d\u0e19\u0e40\u0e1b\u0e25\u0e35\u0e48\u0e22\u0e19\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17", "Transfers"),
        ("\u0e27\u0e34\u0e18\u0e35\u0e27\u0e31\u0e14\u0e21\u0e39\u0e25\u0e04\u0e48\u0e32\u0e40\u0e21\u0e37\u0e48\u0e2d\u0e21\u0e35\u0e01\u0e32\u0e23\u0e42\u0e2d\u0e19", "Transfer Value"),
        ("\u0e01\u0e32\u0e23\u0e15\u0e31\u0e14\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23 / \u0e08\u0e33\u0e2b\u0e19\u0e48\u0e32\u0e22", "Disposals"),
        ("\u0e01\u0e32\u0e23\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e1c\u0e22\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25", "Disclosure"),
        ("\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e2a\u0e31\u0e49\u0e19\u0e46", "Compare"),
        ("\u0e40\u0e1b\u0e23\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e35\u0e22\u0e1a Cost Model", "Models"),
        ("\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07 Dr./Cr.", "Dr./Cr."),
        ("\u0e08\u0e38\u0e14\u0e2a\u0e31\u0e1a\u0e2a\u0e19", "\u0e08\u0e38\u0e14\u0e2a\u0e31\u0e1a\u0e2a\u0e19"),
        ("\u0e2a\u0e39\u0e15\u0e23\u0e08\u0e33\u0e2a\u0e31\u0e49\u0e19\u0e21\u0e32\u0e01\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e2d\u0e1a", "\u0e01\u0e48\u0e2d\u0e19\u0e2a\u0e2d\u0e1a"),
    ]
    for key, label in mapping:
        if key in clean:
            return label
    return clean[:18]


def section_number(title: str) -> int | None:
    match = re.match(r"^(\d+)\)", title.strip())
    return int(match.group(1)) if match else None


def section_theme_class(title: str) -> str:
    lowered = title.lower()
    if any(key in title for key in ["Disclosure", "\u0e40\u0e1b\u0e34\u0e14\u0e40\u0e1c\u0e22"]):
        return "theme-disclosure"
    if any(key in title for key in ["\u0e15\u0e31\u0e14\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23", "\u0e08\u0e33\u0e2b\u0e19\u0e48\u0e32\u0e22", "Compensation"]):
        return "theme-ending"
    if any(key in title for key in ["\u0e08\u0e38\u0e14\u0e2a\u0e31\u0e1a\u0e2a\u0e19", "\u0e2a\u0e39\u0e15\u0e23\u0e08\u0e33", "\u0e1b\u0e34\u0e14\u0e17\u0e49\u0e32\u0e22"]):
        return "theme-review"
    if any(key in title for key in ["\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e1a\u0e31\u0e0d\u0e0a\u0e35", "fair value model", "cost model"]) or "dr./cr." in lowered:
        return "theme-accounting"
    return "theme-default"


def clean_section_title(title: str) -> str:
    return re.sub(r"^\d+\)\s*", "", title).strip()


def wrap_tables(fragment: BeautifulSoup) -> None:
    for table in fragment.find_all("table"):
        wrapper = fragment.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrapper)


def mark_code_blocks(fragment: BeautifulSoup) -> None:
    for pre in fragment.find_all("pre"):
        classes = pre.get("class", [])
        if "ledger-block" not in classes:
            classes.append("ledger-block")
        pre["class"] = classes


def build_sections(soup_root: Tag):
    children = [c for c in soup_root.children if isinstance(c, Tag)]
    page_title = "Investment Property"
    if children and children[0].name == "h1":
        page_title = children[0].get_text(" ", strip=True).replace("AC311 Exam Sheet: ", "").replace("AC311 ", "", 1).strip()
        children = children[1:]

    sections = []
    current = None
    for node in children:
        if node.name == "h2":
            current = {"title": node.get_text(" ", strip=True), "nodes": []}
            sections.append(current)
        else:
            if current is None:
                current = {"title": "\u0e20\u0e32\u0e1e\u0e23\u0e27\u0e21", "nodes": []}
                sections.append(current)
            current["nodes"].append(node)

    if len(sections) > 1 and "\u0e0a\u0e35\u0e17\u0e2d\u0e48\u0e32\u0e19\u0e2a\u0e2d\u0e1a" in sections[0]["title"]:
        sections[1]["nodes"] = sections[0]["nodes"] + sections[1]["nodes"]
        sections = sections[1:]
    return page_title, sections


def render_single_section(sec, index, display_index=None):
    sec_id = slugify(sec["title"], index)
    section_theme = section_theme_class(sec["title"])
    part_number = display_index if display_index is not None else index
    display_title = clean_section_title(sec["title"])

    intro_nodes = []
    subsections = []
    current_sub = None

    for node in sec["nodes"]:
        if node.name == "h3":
            current_sub = {"title": node.get_text(" ", strip=True), "nodes": []}
            subsections.append(current_sub)
        else:
            if current_sub is None:
                intro_nodes.append(node)
            else:
                current_sub["nodes"].append(node)

    sec_html = [
        f'<section class="sheet-section {section_theme}" id="{sec_id}" data-title="{sec["title"]}">',
        '<div class="section-rule"></div>',
        f'<header class="section-head"><p class="section-kicker">Part {part_number:02d}</p><h2>{display_title}</h2></header>',
    ]

    if intro_nodes:
        frag = BeautifulSoup("", "html.parser")
        for node in intro_nodes:
            frag.append(node)
        wrap_tables(frag)
        mark_code_blocks(frag)
        sec_html.append(f'<div class="section-intro prose">{frag.decode_contents()}</div>')

    for sub in subsections:
        tone = tone_for(sub["title"])
        frag = BeautifulSoup("", "html.parser")
        for node in sub["nodes"]:
            frag.append(node)
        wrap_tables(frag)
        mark_code_blocks(frag)
        content = frag.decode_contents()
        if tone == "entry":
            sec_html.append(
                '<details class="subsection is-entry entry" open>'
                f'<summary><span class="subsection-label">Dr./Cr.</span><h3>{sub["title"]}</h3></summary>'
                f'<div class="subsection-body prose">{content}</div>'
                "</details>"
            )
        else:
            sec_html.append(
                f'<article class="subsection {tone}">'
                f'<div class="subsection-head"><span class="subsection-label">{tone.upper()}</span><h3>{sub["title"]}</h3></div>'
                f'<div class="subsection-body prose">{content}</div>'
                "</article>"
            )

    sec_html.append("</section>")
    return "\n".join(sec_html), (sec_id, short_nav(sec["title"]), sec["title"])


def render_sections(sections):
    grouped_sections = []
    indexed = []

    for index, sec in enumerate(sections, 1):
        number = section_number(sec["title"])
        indexed.append(
            {
                "index": index,
                "number": number,
                "section": sec,
            }
        )

    for group_index, spec in enumerate(GROUP_SPECS, 1):
        members = [item for item in indexed if item["number"] in spec["numbers"]]
        if members:
            order_map = {num: pos for pos, num in enumerate(spec["numbers"])}
            members.sort(key=lambda item: order_map.get(item["number"], 999))
        if not members and spec["id"] != "exam-wrap-up":
            continue
        grouped_sections.append(
            {
                "id": spec["id"],
                "title": spec["title"],
                "description": spec["description"],
                "group_index": group_index,
                "members": members,
            }
        )

    html_parts = []
    nav_links = []
    running_display_index = 1

    for group in grouped_sections:
        nav_links.append((group["id"], GROUP_NAV_LABELS.get(group["id"], group["title"]), group["description"]))
        local_links = []
        rendered_members = []
        member_count = len(group["members"])

        if group["id"] == "exam-wrap-up":
            rendered_members.append(MODULE_6_REPLACEMENT_HTML.format(part_number=running_display_index))
            local_links.append(("ip-lifecycle-summary", "\u0e27\u0e07\u0e08\u0e23 IP", "\u0e27\u0e07\u0e08\u0e23\u0e0a\u0e35\u0e27\u0e34\u0e15 Investment Property (IP)"))
            member_count = 1
            running_display_index += 1
        else:
            for item in group["members"]:
                section_html, link = render_single_section(item["section"], item["index"], running_display_index)
                rendered_members.append(section_html)
                local_links.append(link)
                running_display_index += 1

        local_nav = "".join(
            f'<a href="#{sid}" class="group-link" title="{full}">{label}</a>'
            for sid, label, full in local_links
        )

        html_parts.append(
            "\n".join(
                [
                    f'<section class="sheet-group" id="{group["id"]}" data-group-title="{group["title"]}">',
                    '<div class="group-head">',
                    '<div class="group-meta">',
                    f'<p class="group-kicker">Module {group["group_index"]:02d}</p>',
                    f'<p class="group-kicker">{member_count} sections</p>',
                    "</div>",
                    f'<h2>{group["title"]}</h2>',
                    f'<p class="group-description">{group["description"]}</p>',
                    f'<nav class="group-nav" aria-label="{group["title"]}">{local_nav}</nav>',
                    "</div>",
                    '<div class="group-body">',
                    *rendered_members,
                    "</div>",
                    "</section>",
                ]
            )
        )

    return "\n".join(html_parts), nav_links


def build_html() -> str:
    md_text = SRC.read_text(encoding="utf-8")
    html_fragment = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists", "nl2br"])
    base = BeautifulSoup(f'<div id="md-root">{html_fragment}</div>', "html.parser")
    page_title, sections = build_sections(base.find(id="md-root"))
    body_html, nav_links = render_sections(sections)

    nav_html = "".join(
        f'<a href="#{sid}" class="mini-link" data-target="{sid}" title="{full}">{label}</a>'
        for sid, label, full in nav_links
    )
    formula_html = "".join(
        f'<div class="formula-item"><span>{left}</span><strong>{right}</strong></div>'
        for left, right in QUICK_FORMULAE
    )
    pills_html = "".join(f"<span>{item}</span>" for item in SUBJECT_PILLS)
    check_html = "".join(f'<div class="check-item">{item}</div>' for item in CHECK_ITEMS)

    return f"""<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AC311 | {page_title}</title>
  <meta name="description" content="{DESCRIPTION}">
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
      --line-strong: rgba(119, 96, 74, 0.3);
      --accent: #7b8564;
      --accent-soft: rgba(123, 133, 100, 0.12);
      --shadow: 0 16px 32px rgba(76, 56, 37, 0.05);
      --font-sans: "Google Sans Text", "Google Sans", "Product Sans", "Noto Sans Thai", sans-serif;
      --font-mono: "Google Sans Code", "SFMono-Regular", Consolas, monospace;
      --max: 1160px;
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
    :target {{
      scroll-margin-top: 92px;
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
    .page {{ width: min(calc(100% - 32px), var(--max)); margin: 0 auto; padding: 28px 0 80px; }}
    .masthead {{
      padding: 18px 0 8px;
      border-bottom: 1px solid var(--line);
      margin-bottom: 12px;
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
      grid-template-columns: minmax(0, 1.35fr) minmax(280px, 0.65fr);
      gap: 28px;
      align-items: end;
      padding: 18px 0 16px;
    }}
    .hero h1 {{
      margin: 0;
      font-size: clamp(2.25rem, 5.6vw, 4.45rem);
      line-height: 0.98;
      letter-spacing: -0.05em;
      color: #36261c;
    }}
    .hero p {{ margin: 12px 0 0; max-width: 62ch; color: var(--muted); font-size: 1rem; }}
    .subject-line {{ display:flex; gap:12px; flex-wrap:wrap; margin-top:18px; color: var(--muted); font-size:0.95rem; }}
    .subject-line span {{ padding: 7px 11px; border: 1px solid var(--line); border-radius: 999px; background: rgba(255,255,255,0.28); }}
    .formula-strip {{
      display:grid; gap:12px;
      padding: 18px;
      background: linear-gradient(180deg, rgba(255,250,241,0.88), rgba(252,246,236,0.72));
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: var(--shadow);
    }}
    .formula-strip h2 {{ margin:0; font-size:0.98rem; color: var(--muted); letter-spacing:0.06em; text-transform:uppercase; }}
    .formula-item {{ display:grid; gap:4px; padding-bottom:10px; border-bottom:1px dashed var(--line); }}
    .formula-item:last-child {{ border-bottom:none; padding-bottom:0; }}
    .formula-item span {{ color: var(--muted); font-size:0.9rem; }}
    .formula-item strong {{ font-size:1rem; line-height:1.45; }}
    .mini-nav-shell {{ position: sticky; top: 0; z-index: 30; padding: 10px 0 18px; background: linear-gradient(180deg, rgba(245,239,228,0.96), rgba(245,239,228,0.78), rgba(245,239,228,0)); backdrop-filter: blur(8px); }}
    .mini-nav {{
      display:flex; gap:10px; overflow:auto; padding: 10px 4px 10px 2px; scrollbar-width:none;
    }}
    .mini-nav::-webkit-scrollbar {{ display:none; }}
    .mini-link {{
      white-space:nowrap; padding: 10px 14px; border-radius: 999px; border: 1px solid var(--line);
      color: var(--muted); background: rgba(255,250,241,0.78); transition: 180ms ease;
      font-size: 0.95rem;
    }}
    .mini-link:hover, .mini-link:focus-visible {{ border-color: var(--line-strong); color: var(--ink); transform: translateY(-1px); }}
    .mini-link.is-active {{ background: #efe4cf; border-color: rgba(124,137,96,0.4); color: #2f271f; }}
    .content {{ display:grid; gap: 22px; }}
    .sheet-group {{
      display: grid;
      gap: 16px;
      padding-top: 4px;
    }}
    .group-head {{
      padding: 17px 20px 15px;
      border: 1px solid var(--line);
      border-radius: 24px;
      background: linear-gradient(180deg, rgba(255,250,241,0.86), rgba(250,244,233,0.7));
      box-shadow: 0 10px 20px rgba(76, 56, 37, 0.03);
      position: relative;
    }}
    .group-head::after {{
      content: "";
      position: absolute;
      left: 20px;
      right: 20px;
      bottom: 0;
      height: 1px;
      background: linear-gradient(90deg, rgba(123,133,100,0.16), rgba(123,133,100,0));
    }}
    .group-meta {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 8px 16px;
      align-items: baseline;
    }}
    .group-kicker {{
      margin: 0;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.16em;
      font-size: 0.72rem;
      font-weight: 700;
    }}
    .group-head h2 {{
      margin: 0;
      font-size: clamp(1.55rem, 2.2vw, 2.2rem);
      line-height: 1.08;
      letter-spacing: -0.04em;
      color: #2f2219;
    }}
    .group-description {{
      margin: 10px 0 0;
      max-width: 68ch;
      color: var(--muted);
      font-size: 0.97rem;
      line-height: 1.68;
    }}
    .group-nav {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 8px;
      margin-top: 12px;
      padding-top: 2px;
    }}
    .group-link {{
      padding: 9px 11px;
      border-radius: 14px;
      border: 1px solid var(--line);
      background: rgba(255,250,241,0.6);
      color: var(--muted);
      font-size: 0.86rem;
      line-height: 1.35;
      transition: 180ms ease;
    }}
    .group-link:hover, .group-link:focus-visible {{
      color: var(--ink);
      border-color: var(--line-strong);
      background: rgba(255,250,241,0.88);
    }}
    .group-link.is-current {{
      color: #2f271f;
      background: rgba(123, 133, 100, 0.12);
      border-color: rgba(123, 133, 100, 0.26);
    }}
    .group-body {{
      display: grid;
      gap: 18px;
    }}
    .sheet-section {{
      position: relative; padding: 26px clamp(18px, 2vw, 28px) 28px 26px; border: 1px solid var(--line);
      border-radius: 24px; background: linear-gradient(180deg, rgba(255,250,241,0.92), rgba(255,248,236,0.8));
      box-shadow: 0 14px 28px rgba(76, 56, 37, 0.045); overflow: clip;
    }}
    .sheet-section.theme-accounting {{
      background: linear-gradient(180deg, rgba(255,250,241,0.92), rgba(248,241,230,0.84));
    }}
    .sheet-section.theme-disclosure {{
      background: linear-gradient(180deg, rgba(255,250,241,0.9), rgba(244,240,230,0.8));
    }}
    .sheet-section.theme-review {{
      background: linear-gradient(180deg, rgba(255,250,241,0.9), rgba(245,244,236,0.84));
    }}
    .sheet-section::before {{
      content: ""; position:absolute; inset:0; pointer-events:none;
      background: linear-gradient(180deg, rgba(255,255,255,0.45), transparent 24%);
    }}
    .section-rule {{ position:absolute; left:0; top:0; bottom:0; width:10px; background: linear-gradient(180deg, rgba(124,137,96,0.16), rgba(124,137,96,0.02)); }}
    .section-head {{ position:relative; padding-left: 8px; margin-bottom: 14px; }}
    .section-kicker {{ margin:0 0 7px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.16em; font-size: 0.72rem; font-weight: 700; }}
    .section-head h2 {{ margin:0; font-size: clamp(1.4rem, 2vw, 2rem); line-height:1.15; letter-spacing: -0.03em; }}
    .section-head + .section-intro > p:first-child {{
      font-size: 1.02rem;
      color: #4a392d;
      line-height: 1.74;
    }}
    .section-intro {{ margin-bottom: 12px; }}
    .prose p {{ margin: 0 0 11px; }}
    .prose ul, .prose ol {{ margin: 0 0 12px 0; padding-left: 1.05rem; }}
    .prose li {{ margin-bottom: 7px; padding-left: 2px; line-height: 1.7; }}
    .prose td, .prose th, .prose p, .prose li {{
      overflow-wrap: anywhere;
      word-break: normal;
    }}
    .prose h4 {{
      margin: 18px 0 10px;
      font-size: 0.98rem;
      line-height: 1.4;
      color: #4a392d;
      font-weight: 800;
      letter-spacing: -0.01em;
    }}
    .prose code {{
      font-family: var(--font-sans); font-size: 0.95em; font-weight: 700; color: #4f3a2b;
      padding: 0.14rem 0.42rem; border-radius: 8px; background: rgba(124, 137, 96, 0.08); border: 1px solid rgba(124, 137, 96, 0.18);
      transition: background-color 400ms ease, border-color 400ms ease, color 400ms ease, box-shadow 400ms ease;
    }}
    .sheet-section.in-view .prose code {{ background: rgba(124, 137, 96, 0.16); border-color: rgba(124, 137, 96, 0.28); box-shadow: inset 0 -0.55em 0 rgba(124,137,96,0.12); }}
    .prose strong {{ color:#2f231b; }}
    .subsection, details.subsection {{
      margin-top: 16px; padding: 17px; border-top: 1px solid var(--line);
      background: rgba(255,252,246,0.5);
    }}
    .subsection-head {{ display:flex; align-items:baseline; flex-wrap:wrap; gap: 9px 10px; margin-bottom: 11px; }}
    .subsection-label {{ color: var(--muted); letter-spacing:0.14em; text-transform:uppercase; font-size:0.7rem; font-weight:800; }}
    .subsection h3, details.subsection summary h3 {{ margin:0; font-size:1.08rem; line-height:1.35; }}
    .subsection.trap {{ background: linear-gradient(180deg, rgba(154,93,67,0.08), rgba(255,252,246,0.52)); border-left: 3px solid rgba(154,93,67,0.46); padding-left: 16px; }}
    .subsection.alert {{ background: linear-gradient(180deg, rgba(124,137,96,0.12), rgba(255,252,246,0.52)); border-left: 3px solid rgba(124,137,96,0.48); padding-left: 16px; }}
    .subsection.summary {{ background: linear-gradient(180deg, rgba(124,137,96,0.08), rgba(255,252,246,0.52)); }}
    .subsection.example {{ background: linear-gradient(180deg, rgba(98,86,73,0.08), rgba(255,252,246,0.52)); }}
    .subsection.note {{ background: linear-gradient(180deg, rgba(197,172,126,0.12), rgba(255,252,246,0.52)); }}
    details.subsection {{ border-radius: 16px; border: 1px dashed var(--line); padding: 0; overflow: hidden; }}
    details.subsection summary {{ list-style:none; cursor:pointer; display:flex; gap:12px; align-items:baseline; padding: 17px 18px; background: rgba(255,252,246,0.84); }}
    details.subsection summary::-webkit-details-marker {{ display:none; }}
    details.subsection[open] summary {{ border-bottom: 1px dashed var(--line); }}
    details.subsection .subsection-body {{ padding: 17px 18px 18px; }}
    .table-wrap {{ overflow:auto; margin: 12px 0 16px; border: 1px solid var(--line); border-radius: 16px; background: rgba(255,255,255,0.52); position: relative; }}
    .table-wrap::after {{
      content: "";
      position: sticky;
      right: 0;
      top: 0;
      float: right;
      width: 18px;
      height: 100%;
      pointer-events: none;
      background: linear-gradient(90deg, rgba(255,255,255,0), rgba(244,237,225,0.92));
    }}
    table {{ width:100%; border-collapse:collapse; min-width: 640px; font-size: 0.94rem; line-height: 1.58; font-variant-numeric: tabular-nums; }}
    th, td {{ padding: 12px 14px; vertical-align: top; border-bottom: 1px solid rgba(120,99,78,0.12); }}
    th {{ text-align:left; background: rgba(124,137,96,0.08); font-weight: 700; position: sticky; top: 0; z-index: 2; backdrop-filter: blur(2px); }}
    tbody tr:nth-child(even) td {{ background: rgba(255,252,246,0.42); }}
    tr:hover td {{ background: rgba(124,137,96,0.06); }}
    .ledger-block {{
      margin: 12px 0 16px; padding: 15px 16px; background: #f7f0e6; border: 1px solid var(--line);
      border-radius: 18px; overflow:auto;
    }}
    .ledger-block code {{ font-family: var(--font-mono); font-size: 0.95rem; line-height: 1.7; white-space: pre; display:block; color:#2f241d; }}
    .quick-review {{ padding: 22px 24px; border:1px solid var(--line); border-radius: 24px; background: linear-gradient(180deg, rgba(124,137,96,0.08), rgba(255,250,241,0.82)); }}
    .quick-review h2 {{ margin:0 0 8px; font-size: 1.45rem; }}
    .check-grid {{ display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 10px 18px; }}
    .check-item {{ padding: 10px 12px; border-bottom: 1px dashed var(--line); line-height: 1.62; }}
    blockquote {{ margin: 14px 0; padding: 12px 16px; border-left: 3px solid rgba(124,137,96,0.35); background: rgba(255,255,255,0.34); color: var(--muted); }}
    .footer-note {{ color: var(--muted); font-size: 0.95rem; padding: 20px 0 0; }}
    .sheet-section:target {{
      border-color: rgba(123, 133, 100, 0.34);
      box-shadow: 0 0 0 1px rgba(123, 133, 100, 0.1), 0 14px 28px rgba(76, 56, 37, 0.045);
    }}
    details.subsection summary::after {{
      content: "+";
      margin-left: auto;
      color: var(--muted);
      font-size: 0.95rem;
      line-height: 1;
    }}
    details.subsection[open] summary::after {{
      content: "-";
    }}
    .sheet-group, .sheet-section, .group-head, .quick-review, .formula-strip {{
      scroll-margin-top: 96px;
    }}
    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior: auto; }}
      * {{ transition-duration: 0ms !important; animation-duration: 0ms !important; }}
    }}
    @media (max-width: 900px) {{
      .page {{ width: min(calc(100% - 18px), var(--max)); padding-top: 12px; }}
      .hero {{ grid-template-columns: 1fr; gap:18px; }}
      .group-head {{ padding: 15px 15px 13px; border-radius: 20px; }}
      .group-description {{ margin-top: 8px; font-size: 0.94rem; }}
      .group-nav {{ grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); }}
      .sheet-section {{ padding: 21px 15px 22px 18px; border-radius: 22px; }}
      .section-rule {{ width: 8px; }}
      .check-grid {{ grid-template-columns: 1fr; }}
      table {{ min-width: 560px; font-size:0.91rem; }}
      th, td {{ padding: 11px 12px; }}
      .table-wrap {{ margin: 11px -2px 15px; border-radius: 14px; }}
    }}
    @media (max-width: 560px) {{
      body {{ line-height: 1.66; }}
      .hero h1 {{ font-size: 2.15rem; }}
      .hero p {{ font-size: 0.96rem; }}
      .content {{ gap: 18px; }}
      .mini-nav {{ gap: 8px; padding: 8px 2px 8px 0; }}
      .mini-link {{ padding: 8px 11px; font-size: 0.88rem; }}
      .mini-nav-shell {{ padding: 8px 0 14px; }}
      .group-head {{ padding: 14px 14px 12px; border-radius: 18px; }}
      .group-nav {{
        display: flex;
        flex-wrap: nowrap;
        overflow: auto;
        gap: 7px;
        margin-top: 10px;
        padding-bottom: 2px;
        scrollbar-width: none;
      }}
      .group-nav::-webkit-scrollbar {{ display: none; }}
      .group-link {{ font-size: 0.8rem; padding: 7px 10px; border-radius: 999px; white-space: nowrap; }}
      .sheet-section {{ padding: 19px 13px 20px 16px; border-radius: 20px; }}
      .section-head {{ padding-left: 6px; margin-bottom: 12px; }}
      .section-kicker {{ font-size: 0.69rem; }}
      .section-head h2 {{ font-size: 1.25rem; }}
      .section-head + .section-intro > p:first-child {{ font-size: 0.98rem; line-height: 1.68; }}
      .section-intro {{ margin-bottom: 10px; }}
      .prose p {{ margin-bottom: 10px; }}
      .prose ul, .prose ol {{ padding-left: 0.95rem; margin-bottom: 11px; }}
      .prose li {{ margin-bottom: 6px; }}
      .subsection, details.subsection {{ margin-top: 14px; padding: 15px 14px; }}
      details.subsection summary {{ padding: 15px 14px; gap: 10px; }}
      details.subsection .subsection-body {{ padding: 15px 14px 16px; }}
      .table-wrap {{ border-radius: 12px; margin: 10px -2px 14px; }}
      table {{ min-width: 520px; font-size: 0.87rem; line-height: 1.5; }}
      th, td {{ padding: 10px 11px; }}
      .ledger-block {{ padding: 12px 13px; border-radius: 12px; }}
      .ledger-block code {{ font-size: 0.9rem; line-height: 1.62; }}
      .quick-review {{ padding: 18px 16px; border-radius: 20px; }}
      .quick-review h2 {{ font-size: 1.2rem; }}
      .check-item {{ padding: 9px 10px; }}
    }}
  </style>
</head>
<body>
  <div class="page">
    <header class="masthead">
      <p class="eyebrow">{EYEBROW}</p>
      <div class="hero">
        <div>
          <h1>{page_title}</h1>
          <p>{SUBTITLE}</p>
          <div class="subject-line">{pills_html}</div>
        </div>
        <aside class="formula-strip" aria-label="quick formulae">
          <h2>{QUICK_FRAME_TITLE}</h2>
          {formula_html}
        </aside>
      </div>
    </header>

    <div class="mini-nav-shell">
      <nav class="mini-nav" aria-label="{NAV_ARIA}">
        {nav_html}
      </nav>
    </div>

    <main class="content">
      {body_html}
    </main>

    <p class="footer-note">{FOOTER_NOTE}</p>
  </div>

  <script>
    const sections = [...document.querySelectorAll('.sheet-section')];
    const groups = [...document.querySelectorAll('.sheet-group')];
    const navLinks = [...document.querySelectorAll('.mini-link')];
    const groupLinks = [...document.querySelectorAll('.group-link')];
    const byId = Object.fromEntries(navLinks.map(link => [link.dataset.target, link]));
    const groupById = Object.fromEntries(groupLinks.map(link => [link.getAttribute('href').slice(1), link]));

    const sectionObserver = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        entry.target.classList.toggle('in-view', entry.isIntersecting);
        const localLink = groupById[entry.target.id];
        if (localLink && entry.isIntersecting) {{
          groupLinks.forEach(item => item.classList.remove('is-current'));
          localLink.classList.add('is-current');
        }}
      }});
    }}, {{ threshold: 0.18 }});
    sections.forEach(section => sectionObserver.observe(section));

    const navObserver = new IntersectionObserver((entries) => {{
      entries.forEach((entry) => {{
        const link = byId[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {{
          navLinks.forEach(item => item.classList.remove('is-active'));
          link.classList.add('is-active');
        }}
      }});
    }}, {{ rootMargin: '-25% 0px -60% 0px', threshold: 0 }});
    groups.forEach(group => navObserver.observe(group));

    navLinks.forEach(link => {{
      link.addEventListener('click', () => {{
        navLinks.forEach(item => item.classList.remove('is-active'));
        link.classList.add('is-active');
      }});
    }});
  </script>
</body>
</html>
"""


def main():
    html = build_html()
    OUT.write_text(html, encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
