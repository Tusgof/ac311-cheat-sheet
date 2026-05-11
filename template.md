# AC311 Cheat Sheet Template

Template นี้ถอดรูปแบบจาก `chapter-06-notes.html` ให้ใช้สร้างชีทบทใหม่โดยเปลี่ยนเฉพาะเนื้อหา ตัวเลข ตัวอย่าง และคำอธิบายตามบทนั้น ๆ เท่านั้น โครงหน้า น้ำเสียง ลำดับการอ่าน ตาราง กล่องสูตร ข้อสอบย่อย และเฉลยควรคงสไตล์เดียวกับบท 6 ให้มากที่สุด

## Source Integrity ก่อนใช้ Template

Template นี้เป็นคู่มือเรื่อง `รูปแบบการจัดหน้าและ UX` ไม่ใช่คำสั่งให้สร้างเนื้อหาเพิ่มแบบบท 6 เสมอไป เวลาแปลง source เป็นชีท ต้องยึดเนื้อหาที่ผู้ใช้ให้มาก่อนเสมอ

- ห้ามแต่ง Mini Test, Mock Exam, Answer Key, ตัวเลข, case, หรือรายการบัญชีเพิ่มเอง เว้นแต่ผู้ใช้สั่งให้สร้างโจทย์/แบบฝึกหัด/เฉลย หรือ source มีส่วนนั้นอยู่แล้ว
- ถ้า source เป็นชีทเนื้อหาล้วน ให้ทำเป็นชีทเนื้อหาล้วน โดยใช้ component ของ template เช่น hero, quick frame, roadmap, formula, callout, table, highlight, ledger block
- ถ้า source มีโจทย์หรือเฉลยอยู่แล้ว ให้จัดรูปแบบโจทย์/เฉลยนั้นด้วย `test-box` และ `answer-box` ได้ แต่ต้องไม่เปลี่ยนสาระหรือเพิ่มข้อใหม่โดยไม่บอก
- ถ้าจะเพิ่ม context เพื่อช่วยอ่าน ต้องเป็น context สั้น ๆ และต้องไม่ทำให้เหมือนเป็นข้อมูลจาก source
- Chapter 6 เป็นตัวอย่าง style เต็มรูปแบบ เพราะบทนั้นมี mini test/mock exam/answer key ในตัว ไม่ได้แปลว่าทุกบทต้องมีเหมือนกัน

## เป้าหมายของชีท

ชีทต้องเป็นเอกสารอ่านสอบที่พานักศึกษาไล่คิดทีละขั้น ไม่ใช่สรุปสั้นแบบ bullet dump

- อ่านแล้วรู้ว่าเรื่องนี้ต้องเริ่มคิดจากอะไร
- เห็นเงื่อนไข กฎ สูตร และกับดักสอบแยกชัดเจน
- มีตัวอย่างคำนวณพร้อมรายการบัญชี
- มี Mini Test / Mock Exam / Answer Key เฉพาะเมื่อ source มีให้ หรือผู้ใช้สั่งให้สร้าง
- ใช้ภาษาไทยเป็นหลัก และคง technical terms ภาษาอังกฤษที่สำคัญ เช่น `carrying amount`, `fair value`, `OCI`, `P/L`, `depreciation`, `revaluation surplus`

## ไฟล์ที่ควรสร้าง

สำหรับบทใหม่ให้ใช้โครงชื่อไฟล์นี้

```text
chapter-XX-notes.html
chapter-XX-mock-exam.html        ถ้ามีหน้าโจทย์แยก
chapter-XX-solution.html         ถ้ามีหน้าเฉลยแยก
ChapterXX/source-notes.md        ถ้าเก็บต้นฉบับ markdown
ChapterXX/mock-exam.md           ถ้ามีข้อสอบจำลอง
ChapterXX/mock-exam-solution.md  ถ้ามีเฉลยข้อสอบจำลอง
```

หน้า library `index.html` ควรมี 3 ปุ่มต่อบท

```text
เนื้อหา -> chapter-XX-notes.html
ข้อสอบจำลอง -> chapter-XX-mock-exam.html
เฉลย -> chapter-XX-solution.html
```

## บุคลิกของหน้า

สไตล์ภาพรวมต้องเหมือนบท 6

- พื้นหลังครีมอ่อนพร้อมเส้น grid บาง ๆ
- หน้าเอกสารตรงกลางเหมือน paper sheet
- สีหลักเป็นน้ำตาลเข้ม ครีม ทองหม่น และเขียวเทาอ่อน
- ตัวอักษรหัวข้อใหญ่ หนัก อ่านง่าย
- หลีกเลี่ยง layout แบบ marketing page
- ความรู้สึกต้องเป็น lecture note สำหรับอ่านสอบ ไม่ใช่ landing page
- กล่องข้อมูลต้องมีหน้าที่ชัดเจน เช่น สูตร, guardrail, exam watch, note, example, test, answer โดย test/answer ใช้เฉพาะเมื่อมีเนื้อหาประเภทนั้น
- ตารางต้องโปร่ง อ่านเป็นแถวได้ง่าย และรองรับ mobile ด้วย horizontal scroll
- รายการบัญชีต้องอยู่ใน dark code block และรักษาบรรทัดให้ตรง

## โครงสร้างหน้าแนะนำ

โครงสร้างพื้นฐานของชีทควรเรียงแบบนี้

1. Header / Hero
2. Quick Frame 4 ช่อง
3. สารบัญ sticky
4. Segment ตาม logic ของ source
5. กล่องสูตร ตาราง callout และ ledger block ตามเนื้อหาที่มีจริง
6. Mini Test / Mock Exam / Answer Key เฉพาะเมื่อ source มีให้หรือผู้ใช้สั่งให้สร้าง
7. Footer note

ถ้าบทนั้นมีเนื้อหาน้อยหรือมากกว่า 4 ช่วง ให้ยังรักษาจังหวะแบบบท 6 คือแบ่งตาม logic การทำข้อสอบ ไม่แบ่งตามหัวข้อหนังสือแบบแข็ง ๆ

## Page Skeleton

ใช้ skeleton นี้เป็นฐานของ `chapter-XX-notes.html`

หมายเหตุ: ส่วน `mini-test`, `mock-exam`, และ `answer-key` ใน skeleton ด้านล่างเป็นตัวอย่าง component เท่านั้น ให้ลบออกถ้า source ไม่มีโจทย์หรือผู้ใช้ไม่ได้สั่งให้สร้างแบบฝึกหัด/เฉลย

```html
<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chapter XX: [Chapter Title] | AC311</title>
  <style>
    :root {
      --paper: #fffaf2;
      --paper-strong: #f7ead6;
      --ink: #2c2118;
      --muted: #6f604f;
      --accent: #a36b2d;
      --accent-strong: #7d4612;
      --line: rgba(119, 82, 45, 0.22);
      --green: #eaf1de;
      --green-line: #c3cfaa;
      --code-bg: #2a251d;
      --content: 1180px;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      color: var(--ink);
      font-family: "Inter", "Noto Sans Thai", "Segoe UI", sans-serif;
      line-height: 1.7;
      background:
        linear-gradient(rgba(122, 89, 52, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(122, 89, 52, 0.05) 1px, transparent 1px),
        #f6efe3;
      background-size: 32px 32px;
    }

    .page {
      width: min(var(--content), calc(100% - 32px));
      margin: 28px auto;
      padding: 46px 56px 64px;
      background: rgba(255, 250, 242, 0.94);
      border: 1px solid rgba(113, 82, 46, 0.18);
      box-shadow: 0 24px 60px rgba(57, 41, 24, 0.12);
      position: relative;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 13px;
      border-radius: 999px;
      background: var(--paper-strong);
      color: var(--accent-strong);
      font-weight: 800;
      font-size: 13px;
      letter-spacing: 0;
      text-transform: uppercase;
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 360px;
      gap: 32px;
      align-items: end;
      padding: 28px 0 30px;
      border-bottom: 2px solid var(--line);
    }

    h1 {
      margin: 0;
      font-size: 58px;
      line-height: 1.05;
      letter-spacing: 0;
    }

    h2 {
      margin: 0 0 18px;
      font-size: 34px;
      line-height: 1.25;
      letter-spacing: 0;
    }

    h3 {
      margin: 0 0 10px;
      font-size: 22px;
      line-height: 1.35;
    }

    p {
      margin: 0 0 16px;
      font-size: 18px;
    }

    .lead {
      margin-top: 20px;
      color: var(--muted);
      max-width: 780px;
      font-size: 20px;
    }

    .subject-line {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
    }

    .chip {
      display: inline-flex;
      align-items: center;
      padding: 6px 12px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.58);
      color: #4c3c2d;
      font-size: 14px;
      font-weight: 700;
    }

    .formula-strip,
    .roadmap,
    .formula,
    .panel,
    .callout,
    .test-box,
    .answer-box {
      border-radius: 8px;
      border: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.72);
    }

    .formula-strip {
      padding: 18px;
      display: grid;
      gap: 12px;
    }

    .formula-item {
      padding-bottom: 12px;
      border-bottom: 1px dashed var(--line);
    }

    .formula-item:last-child {
      border-bottom: 0;
      padding-bottom: 0;
    }

    .formula-item strong {
      display: block;
      color: var(--accent-strong);
    }

    .toc {
      position: sticky;
      top: 0;
      z-index: 5;
      margin: 30px -18px 46px;
      padding: 16px 18px;
      border: 1px solid var(--line);
      background: rgba(255, 250, 242, 0.94);
      backdrop-filter: blur(10px);
    }

    .toc ol {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .toc a {
      display: inline-flex;
      padding: 8px 12px;
      border: 1px solid var(--line);
      border-radius: 999px;
      color: var(--ink);
      text-decoration: none;
      font-weight: 700;
      background: #fffaf2;
    }

    section {
      padding: 42px 0;
      border-bottom: 1px solid var(--line);
    }

    .segment-label,
    .test-label,
    .answer-label {
      display: inline-block;
      margin-bottom: 14px;
      color: var(--accent-strong);
      font-size: 13px;
      font-weight: 900;
      letter-spacing: 0;
      text-transform: uppercase;
    }

    .roadmap,
    .formula,
    .callout,
    .test-box,
    .answer-box {
      padding: 22px;
      margin: 22px 0;
    }

    .formula {
      border-left: 6px solid var(--accent);
      background: #fff3de;
    }

    .callout {
      background: var(--green);
      border-color: var(--green-line);
    }

    .grid-two {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 18px;
      margin: 22px 0;
    }

    .panel {
      padding: 20px;
    }

    table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 22px 0;
      overflow: hidden;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fffdfa;
    }

    th,
    td {
      padding: 13px 15px;
      vertical-align: top;
      border-bottom: 1px solid var(--line);
      text-align: left;
      font-size: 16px;
    }

    th {
      background: #f4e3cb;
      color: var(--accent-strong);
      font-weight: 900;
    }

    tr:last-child td {
      border-bottom: 0;
    }

    code {
      padding: 2px 6px;
      border-radius: 5px;
      background: rgba(116, 78, 38, 0.09);
      font-family: "Cascadia Mono", "Consolas", monospace;
      font-size: 0.95em;
    }

    pre {
      margin: 22px 0;
      padding: 22px 26px;
      overflow-x: auto;
      border-radius: 8px;
      border-left: 6px solid #c79145;
      background: var(--code-bg);
      color: #fffaf0;
      font-family: "Cascadia Mono", "Consolas", monospace;
      font-size: 16px;
      line-height: 1.7;
      white-space: pre;
    }

    pre code {
      padding: 0;
      background: transparent;
      color: inherit;
      white-space: pre;
      word-break: normal;
      overflow-wrap: normal;
    }

    .test-box {
      background: #f4f8ec;
      border-color: var(--green-line);
    }

    .answer-box {
      background: #fff7eb;
      border-left: 6px solid var(--accent);
    }

    .back {
      margin-top: 24px;
    }

    .back a {
      color: var(--accent-strong);
      font-weight: 800;
      text-decoration: none;
    }

    .footer-note {
      padding-top: 28px;
      color: var(--muted);
      font-size: 15px;
    }

    @media (max-width: 900px) {
      .page {
        width: min(100% - 18px, var(--content));
        padding: 28px 18px 44px;
      }

      .hero,
      .grid-two {
        grid-template-columns: 1fr;
      }

      h1 {
        font-size: 42px;
      }

      h2 {
        font-size: 28px;
      }

      table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
      }

      th,
      td {
        min-width: 160px;
      }
    }
  </style>
</head>
<body>
  <main class="page">
    <header id="top">
      <span class="eyebrow">AC311 Intermediate Accounting 1</span>
      <div class="hero">
        <div>
          <h1>Chapter XX: [ชื่อบทภาษาอังกฤษ]</h1>
          <p class="lead">อ่านตามลำดับ: [concept 1] -> [concept 2] -> [concept 3] -> [exam application]</p>
          <div class="subject-line">
            <span class="chip">[Standard เช่น TAS 16]</span>
            <span class="chip">[Main Topic]</span>
            <span class="chip">Dr./Cr.</span>
          </div>
        </div>

        <aside class="formula-strip" aria-label="Quick frame">
          <div class="formula-item">
            <strong>[Frame 1]</strong>
            [ประโยคสั้นที่เป็นแกนคิด]
          </div>
          <div class="formula-item">
            <strong>[Frame 2]</strong>
            [สูตรหรือ rule สำคัญ]
          </div>
          <div class="formula-item">
            <strong>[Frame 3]</strong>
            [กับดักที่ต้องจำ]
          </div>
          <div class="formula-item">
            <strong>[Frame 4]</strong>
            [ปลายทางของการทำข้อสอบ]
          </div>
        </aside>
      </div>
    </header>

    <nav class="toc" aria-labelledby="toc-title">
      <h2 id="toc-title">สารบัญ</h2>
      <ol>
        <li><a href="#segment-1">Segment 1</a></li>
        <li><a href="#mini-test-1">Mini Test 1</a></li>
        <li><a href="#segment-2">Segment 2</a></li>
        <li><a href="#mini-test-2">Mini Test 2</a></li>
        <li><a href="#segment-3">Segment 3</a></li>
        <li><a href="#mini-test-3">Mini Test 3</a></li>
        <li><a href="#segment-4">Segment 4</a></li>
        <li><a href="#mini-test-4">Mini Test 4</a></li>
        <li><a href="#mock-exam">Mock Exam</a></li>
        <li><a href="#answer-key">Answer Key</a></li>
      </ol>
    </nav>

    <section id="segment-1">
      <span class="segment-label">Current Segment</span>
      <h2>Segment 1: [English Concept], [Thai Keyword]</h2>

      <div class="roadmap">
        <strong>In This Segment</strong>
        <p>อ่านตามลำดับนี้: [step 1] -> [step 2] -> [step 3] -> [output ที่ต้องทำได้]</p>
      </div>

      <p>[ย่อหน้าเปิด segment อธิบายว่าทำไมเรื่องนี้สำคัญในการทำข้อสอบ]</p>

      <div class="formula">
        <strong>Core rule:</strong>
        [กฎหลัก 1-2 ประโยค]
      </div>

      <div class="grid-two">
        <div class="panel">
          <h3>[หัวข้อย่อย A]</h3>
          <p>[คำอธิบาย]</p>
        </div>
        <div class="panel">
          <h3>[หัวข้อย่อย B]</h3>
          <p>[คำอธิบาย]</p>
        </div>
      </div>

      <div class="callout">
        <h3>Exam Watch</h3>
        <p>[กับดักหรือจุดที่ข้อสอบชอบถาม]</p>
      </div>

      <div class="back"><a href="#top">กลับไปด้านบน</a></div>
    </section>

    <section id="mini-test-1" class="test-box">
      <span class="test-label">Mini Test 1</span>
      <h2>Mini Test 1: [ชื่อโจทย์สั้น ๆ]</h2>
      <p>[โจทย์สถานการณ์ 1 ย่อหน้า]</p>
      <ol>
        <li>[คำถามข้อ 1]</li>
        <li>[คำถามข้อ 2]</li>
        <li>[คำถามข้อ 3]</li>
      </ol>
    </section>

    <section id="mock-exam" class="test-box">
      <span class="test-label">Mock Exam</span>
      <h2>Mock Exam: [ชื่อรวมท้ายบท]</h2>
      <div class="roadmap">
        <strong>Exam Scope</strong>
        <p>[บอกว่าโจทย์รวมนี้ทดสอบอะไรบ้าง]</p>
      </div>
      <p>[โจทย์รวมแบบ exam case]</p>
    </section>

    <section id="answer-key">
      <span class="answer-label">Answer Key</span>
      <h2>Answer Key</h2>

      <article class="answer-box">
        <h3>Mini Test 1</h3>
        <p>[อธิบายวิธีคิดก่อนตอบ]</p>
      </article>

      <article class="answer-box">
        <h3>Mock Exam</h3>
        <p>[เฉลยละเอียด]</p>
      </article>
    </section>

    <p class="footer-note">Prepared for AC311 Intermediate Accounting 1. Use this sheet as an exam-reading path, not as a substitute for the full standard.</p>
  </main>
</body>
</html>
```

## วิธีเขียน Header / Hero

Hero ต้องทำหน้าที่บอกภาพรวมของบทภายใน 5 วินาที

รูปแบบหัวข้อ

```text
Chapter XX: [English Chapter Name]
```

ตัวอย่างจากบท 6

```text
Chapter 6: PPE Subsequent Measurement
```

`lead` ต้องเป็น roadmap สั้น ๆ

```text
อ่านตามลำดับ: [policy choice] -> [measurement rule] -> [journal entry] -> [exam disposal / ending balance]
```

Quick Frame ต้องมี 4 ช่องเสมอ แต่ละช่องมีหัวหนาและคำอธิบายสั้นมาก

```html
<aside class="formula-strip" aria-label="Quick frame">
  <div class="formula-item">
    <strong>วัดต่อหลังรับรู้</strong>
    เลือก Cost model หรือ Revaluation model
  </div>
  <div class="formula-item">
    <strong>Revaluation</strong>
    กำไรขึ้น OCI, ขาดทุนลง P/L ตามกฎ
  </div>
  <div class="formula-item">
    <strong>Depreciation</strong>
    คิดจาก carrying amount หลัง revalue
  </div>
  <div class="formula-item">
    <strong>Disposal</strong>
    proceeds - carrying amount = gain/loss
  </div>
</aside>
```

สำหรับบทใหม่ให้เปลี่ยนเฉพาะหัวข้อและประโยคใน 4 ช่อง โดยยังให้ครอบคลุมวงจรคิดตั้งแต่เริ่มโจทย์จนถึงคำตอบ

## วิธีแบ่ง Segment

Segment ไม่ควรเป็นการคัดสารบัญหนังสือ แต่ควรเป็นลำดับการคิดตอนทำข้อสอบ

รูปแบบที่แนะนำ

```text
Segment 1: Definition / Recognition / Initial Rule
Segment 2: Measurement / Calculation / Main Accounting Treatment
Segment 3: Special Cases / Adjustments / Alternative Methods
Segment 4: Later Events / Disposal / Disclosure / Exam Integration
```

แต่ละ Segment ต้องมีองค์ประกอบเหล่านี้

- `segment-label`
- `h2`
- `roadmap`
- ย่อหน้าเปิดว่าทำไม segment นี้สำคัญ
- `formula` สำหรับกฎหลักหรือสูตรจำ
- ตารางหรือ panel อย่างน้อย 1 ชุด ถ้าช่วยให้เห็นภาพ
- `callout` สำหรับกับดักสอบ
- ตัวอย่างคำนวณหรือรายการบัญชีถ้าเป็นบทที่มีตัวเลข
- ปุ่มกลับด้านบน

## Roadmap Block

Roadmap ใช้ก่อนเริ่ม segment เพื่อบังคับลำดับการอ่าน

```html
<div class="roadmap">
  <strong>In This Segment</strong>
  <p>อ่านตามลำดับนี้: ระบุ asset class -> เลือก policy -> วัดมูลค่าหลังรับรู้ -> แปลเป็น journal entry</p>
</div>
```

หลักการเขียน

- ใช้ลูกศร `->`
- เขียน 3-5 ขั้น
- ขั้นสุดท้ายควรเป็น output ที่ทำข้อสอบได้ เช่น `ลง journal entry`, `คำนวณ carrying amount`, `หา impairment loss`

## Formula Block

ใช้สำหรับกฎที่ต้องจำหรือสูตรหลัก

```html
<div class="formula">
  <strong>Core rule:</strong>
  ถ้าใช้ revaluation model ต้อง revalue ทั้ง asset class และต้องทำด้วย sufficient regularity
</div>
```

รูปแบบข้อความที่ใช้ได้

```text
Core rule:
Memory hook:
Exam formula:
Recognition rule:
Measurement rule:
Decision rule:
```

สูตรควรเขียนสั้นและมีชื่อบัญชีชัดเจน

```html
<div class="formula">
  <strong>Exam formula:</strong>
  Revaluation gain/loss = fair value - carrying amount before revaluation
</div>
```

## Grid-Two และ Panel

ใช้เมื่อต้องเทียบ 2 แนวคิด หรือแยกสองฝั่งของ logic

```html
<div class="grid-two">
  <div class="panel">
    <h3>Cost Model</h3>
    <p>ถือสินทรัพย์ด้วย cost less accumulated depreciation and impairment loss</p>
  </div>
  <div class="panel">
    <h3>Revaluation Model</h3>
    <p>ถือสินทรัพย์ด้วย fair value at revaluation date less subsequent depreciation and impairment</p>
  </div>
</div>
```

ใช้ panel สำหรับ

- เปรียบเทียบ model A / model B
- แยก accounting treatment ฝั่ง debit / credit
- แยก before / after
- แยก normal case / exception

## Callout Block

Callout ใช้เตือนเรื่องที่พลาดง่าย ไม่ใช้แทนเนื้อหาหลัก

```html
<div class="callout">
  <h3>Trap: Revalue แค่รายการเดียวไม่ได้เสมอ</h3>
  <p>ถ้าเลือก revaluation model ต้อง revalue ทั้ง asset class เพื่อหลีกเลี่ยง selective revaluation</p>
</div>
```

หัวข้อ callout ที่ควรใช้

```text
Exam Watch
Policy Guardrails
Trap: [สิ่งที่พลาด]
Decision Flow
Check Yourself
Common Mistake
```

## ตาราง

ตารางต้องอ่านง่ายและใช้เมื่อต้องเทียบหรือไล่ตัวเลขหลายช่วง ห้ามใช้ตารางถ้าเป็นแค่ bullet ธรรมดา

### ตารางเปรียบเทียบ Concept

```html
<table>
  <thead>
    <tr>
      <th>ประเด็น</th>
      <th>[Concept A]</th>
      <th>[Concept B]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ฐานการวัด</td>
      <td>[คำตอบ A]</td>
      <td>[คำตอบ B]</td>
    </tr>
    <tr>
      <td>ผลกระทบต่องบกำไรขาดทุน</td>
      <td>[คำตอบ A]</td>
      <td>[คำตอบ B]</td>
    </tr>
  </tbody>
</table>
```

### ตารางไล่คำนวณ

ใช้เมื่อต้องตามยอดหลายปีหรือหลายขั้น

```html
<table>
  <thead>
    <tr>
      <th>วันที่</th>
      <th>Carrying amount ก่อนปรับ</th>
      <th>Fair value</th>
      <th>ส่วนต่าง</th>
      <th>เข้า OCI</th>
      <th>เข้า P/L</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>31/12/X2</td>
      <td>4,800,000</td>
      <td>5,100,000</td>
      <td>300,000 เพิ่มขึ้น</td>
      <td>300,000</td>
      <td>-</td>
    </tr>
  </tbody>
</table>
```

### ตารางสรุปสอบ

ใช้ท้าย segment เพื่อบีบ rule ให้เหลือภาพจำ

```html
<table>
  <thead>
    <tr>
      <th>โจทย์ให้มา</th>
      <th>ให้คิดว่า</th>
      <th>คำตอบที่ควรออก</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ราคายุติธรรมสูงกว่ามูลค่าตามบัญชี</td>
      <td>Revaluation increase</td>
      <td>รับรู้ OCI เว้นแต่ reverse loss เดิมใน P/L</td>
    </tr>
  </tbody>
</table>
```

หลักการทำตาราง

- หัวตารางต้องเป็นคำสั้น อ่านแล้วรู้หน้าที่
- ถ้ามีตัวเลขจำนวนเงิน ใช้ comma
- ถ้าเป็นศูนย์หรือไม่มีรายการ ใช้ `-`
- อย่าใส่ paragraph ยาวใน cell
- ถ้าตารางใหญ่ ให้แบ่งเป็น 2 ตารางแทนการยัดทั้งหมดในตารางเดียว

## รายการบัญชี

รายการบัญชีต้องอยู่ใน `pre` เสมอ ห้ามเขียน Dr/Cr เป็นบรรทัดเดียวกัน

รูปแบบมาตรฐาน

```html
<pre><code>วันที่
Dr [ชื่อบัญชี] xxx
   Cr [ชื่อบัญชี] xxx

วันที่
Dr [ชื่อบัญชี] xxx
   Cr [ชื่อบัญชี] xxx</code></pre>
```

กฎการจัดบรรทัด

- วันที่อยู่บรรทัดแรกของ entry
- `Dr` เริ่มชิดซ้าย
- `Cr` ย่อหน้าเข้ามา 3 ช่อง
- ถ้ามีหลาย debit ให้เรียง debit ก่อน แล้วค่อย credit
- เว้นบรรทัดว่างระหว่างวันที่หรือเหตุการณ์
- ใช้ชื่อบัญชีไทยได้ แต่คง `Dr` และ `Cr`
- ห้ามรวมหลาย entry เป็นบรรทัดเดียว
- ถ้ารายการยาว ให้ขึ้นบรรทัดใหม่ ไม่ฝืนให้อยู่บรรทัดเดียว

ตัวอย่าง

```html
<pre><code>31/12/X2
Dr อาคารโรงงาน 260,000
   Cr ส่วนเกินทุนจากการตีราคาสินทรัพย์ - อาคาร 260,000

31/12/X3
Dr ส่วนเกินทุนจากการตีราคาสินทรัพย์ - อาคาร 260,000
Dr ขาดทุนจากการตีราคาสินทรัพย์ 20,000
   Cr อาคารโรงงาน 280,000</code></pre>
```

ถ้าเฉลยต้องแสดงการคำนวณก่อนรายการบัญชี ให้เขียนแบบนี้

```html
<p>Carrying amount ก่อนตีราคาใหม่ = 5,600,000 - 715,000 = <code>4,885,000</code></p>
<p>Fair value = <code>5,300,000</code> ดังนั้นส่วนต่างเพิ่มขึ้น = <code>415,000</code></p>

<pre><code>31/12/X3
Dr ค่าเสื่อมราคาสะสม - อาคารโรงงาน 715,000
   Cr อาคารโรงงาน 715,000

Dr อาคารโรงงาน 415,000
   Cr ส่วนเกินทุนจากการตีราคาสินทรัพย์ - อาคาร 415,000</code></pre>
```

## Mini Test

ใช้ Mini Test เฉพาะเมื่อ source มีแบบฝึกหัดให้ หรือผู้ใช้สั่งให้สร้างโจทย์เพิ่ม ถ้า source เป็นเนื้อหาล้วน ห้ามแต่งโจทย์ใหม่เองเพียงเพราะ template มี component นี้

```html
<section id="mini-test-1" class="test-box">
  <span class="test-label">Mini Test 1</span>
  <h2>Mini Test 1: [ชื่อสั้น]</h2>
  <p>[โจทย์สถานการณ์]</p>
  <ol>
    <li>[ถามให้ระบุ rule]</li>
    <li>[ถามให้คำนวณ]</li>
    <li>[ถามให้บันทึกบัญชี]</li>
    <li>[ถามให้สรุปผลกระทบต่องบการเงิน]</li>
  </ol>
</section>
```

หลักการจัด Mini Test เมื่อได้รับอนุญาตให้สร้างหรือ source มีโจทย์

- ใช้ตัวเลขไม่เยอะเกิน 1 case
- ถาม 3-5 ข้อ
- ต้องตรงกับ segment ที่เพิ่งเรียน
- อย่าเฉลยใน test box
- เฉลยทั้งหมดไปรวมใน Answer Key ด้านท้าย

ประเภทคำถามที่ดี

```text
1. ระบุ treatment ที่ถูกต้อง
2. คำนวณ carrying amount / gain / loss / depreciation
3. บันทึกรายการบัญชี
4. อธิบายว่ารายการนี้เข้า OCI หรือ P/L
5. หายอดคงเหลือหลังปรับ
```

## Mock Exam

ใช้ Mock Exam เฉพาะเมื่อ source มีข้อสอบรวมให้ หรือผู้ใช้ขอให้สร้างข้อสอบจำลอง ถ้าไม่ได้รับคำสั่ง ให้ละ component นี้ออกจากหน้า

```html
<section id="mock-exam" class="test-box">
  <span class="test-label">Mock Exam</span>
  <h2>Mock Exam: Integrated [Chapter Topic]</h2>
  <div class="roadmap">
    <strong>Exam Scope</strong>
    <p>โจทย์นี้รวม [segment 1] -> [segment 2] -> [segment 3] -> [segment 4]</p>
  </div>
  <p>[โจทย์รวม]</p>
  <ol>
    <li>[คำสั่ง 1]</li>
    <li>[คำสั่ง 2]</li>
    <li>[คำสั่ง 3]</li>
  </ol>
</section>
```

Mock Exam ที่ดีควรมี เมื่อได้รับคำสั่งให้สร้าง

- เหตุการณ์หลายวันหรือหลายปี
- ตัวเลขที่ต้องใช้ rule มากกว่า 1 จุด
- จุดหลอกที่ต้องเลือก treatment
- คำสั่งให้บันทึกบัญชี
- คำสั่งให้คำนวณยอดปลายงวด
- คำสั่งให้อธิบายผลเข้า OCI/P/L ถ้าเกี่ยวข้อง

## Answer Key

ใช้ Answer Key เฉพาะเมื่อมีคำถาม/โจทย์ที่ต้องเฉลยอยู่ใน source หรือผู้ใช้สั่งให้สร้างเฉลย ถ้าไม่มีโจทย์ ห้ามสร้าง Answer Key เอง

```html
<section id="answer-key">
  <span class="answer-label">Answer Key</span>
  <h2>Answer Key</h2>

  <article class="answer-box">
    <h3>Mini Test 1</h3>
    <p>เริ่มจากหา [ฐานคิด] ก่อน เพราะ [เหตุผล]</p>
    <p>[สูตร] = <code>[คำนวณ]</code></p>
    <pre><code>วันที่
Dr [บัญชี] xxx
   Cr [บัญชี] xxx</code></pre>
  </article>
</section>
```

ลำดับการเฉลย

1. ระบุ rule ที่ใช้
2. แสดงสูตร
3. แทนตัวเลข
4. สรุปยอด
5. ลงรายการบัญชี
6. อธิบายผลกระทบถ้าจำเป็น

อย่าเริ่มเฉลยด้วย journal entry ทันทีถ้าโจทย์มีการคำนวณ ต้องพาผู้อ่านเห็นที่มาของตัวเลขก่อน

## น้ำเสียงการเขียน

น้ำเสียงต้องเหมือนติวเตอร์ที่พาอ่านสอบ

ใช้ประโยคแบบนี้

```text
จุดเริ่มต้นของข้อนี้คือ...
ให้แยกก่อนว่าโจทย์ถาม measurement หรือ journal entry
ถ้าโจทย์ให้ fair value มา อย่าเพิ่งลงกำไรทันที ต้องเทียบกับ carrying amount ก่อน
ข้อสอบมักหลอกตรง...
จำ rule นี้ก่อน แล้วค่อยคำนวณ
```

หลีกเลี่ยง

```text
ตามที่กล่าวมาแล้วข้างต้น
เป็นที่ทราบกันดีว่า
ผู้เรียนควรศึกษาเพิ่มเติม
รายละเอียดมีมากมาย
```

## การใช้ภาษาไทยและอังกฤษ

ให้ใช้ภาษาไทยเป็นหลัก แต่คงคำอังกฤษเมื่อเป็นศัพท์สอบหรือชื่อบัญชีสำคัญ

ตัวอย่างที่ควรคงอังกฤษ

```text
cost model
revaluation model
carrying amount
fair value
OCI
P/L
impairment loss
recoverable amount
depreciation
useful life
residual value
```

ตัวอย่างการเขียนที่ดี

```text
ถ้า fair value สูงกว่า carrying amount จะเกิด revaluation increase
แต่ยังต้องดูว่าก่อนหน้านี้เคยมี revaluation decrease ที่เข้า P/L หรือไม่
```

## Pattern สำหรับบทบัญชีประเภทต่าง ๆ

### บทที่เน้น Recognition

โครง segment ที่เหมาะ

```text
Segment 1: Definition and Scope
Segment 2: Recognition Criteria
Segment 3: Initial Measurement
Segment 4: Subsequent Treatment and Derecognition
```

ตารางที่ควรมี

```text
รายการ | เข้าเกณฑ์รับรู้หรือไม่ | เหตุผล | Journal impact
```

### บทที่เน้น Measurement

โครง segment ที่เหมาะ

```text
Segment 1: Measurement Base
Segment 2: Main Formula
Segment 3: Adjustments and Special Cases
Segment 4: Ending Balance and Journal Entries
```

ตารางที่ควรมี

```text
ขั้น | สิ่งที่โจทย์ให้ | สิ่งที่ต้องคำนวณ | Output
```

### บทที่เน้น Journal Entries

โครง segment ที่เหมาะ

```text
Segment 1: Account Map
Segment 2: Normal Entries
Segment 3: Adjusting Entries
Segment 4: Closing / Disposal / Reversal
```

ต้องมี

- ตาราง mapping บัญชี
- journal entry หลายตัวอย่าง
- callout อธิบาย debit/credit logic

### บทที่เน้น Comparison

โครง segment ที่เหมาะ

```text
Segment 1: Concept A
Segment 2: Concept B
Segment 3: Difference and Exam Trap
Segment 4: Integrated Case
```

ต้องมีตารางเทียบหลักอย่างน้อย 1 ตาราง

## Checklist ก่อนส่งงาน

ตรวจทุกครั้งก่อนบอกว่าเสร็จ

- หน้าเปิดด้วย hero แบบบท 6
- มี Quick Frame 4 ช่อง
- สารบัญ link ไปครบทุก anchor
- ทุก segment มี roadmap
- ทุก segment มี formula หรือ callout อย่างน้อยหนึ่งจุด
- ไม่สร้าง Mini Test / Mock Exam / Answer Key เอง เว้นแต่ source มีให้หรือผู้ใช้สั่ง
- ถ้ามี Mini Test / Mock Exam / Answer Key ต้องเฉลยครบและโยงกลับ source
- รายการบัญชีอยู่คนละบรรทัดและใช้ `pre code`
- `pre code` มี `white-space: pre`
- ตารางไม่แน่นเกินไป
- mobile มี horizontal scroll สำหรับตาราง
- ไม่มีข้อความภาษาอังกฤษยาวโดยไม่จำเป็น
- ไม่มีตัวเลขที่แต่งขึ้นโดยไม่อิง source เว้นแต่ระบุว่าเป็นโจทย์จำลอง
- ถ้ามีข้อมูลไม่ชัดเจน ให้ใส่ note ว่า source ไม่ได้ระบุ แทนการเดา

## Prompt สำหรับใช้ในอนาคต

ถ้าจะให้สร้างชีทบทใหม่จากเนื้อหาที่ส่งมา ใช้ prompt นี้ได้

```text
ใช้ template.md ของ AC311 ทำชีทบท [เลขบท] จากเนื้อหาด้านล่าง
ขอ style เหมือน chapter-06-notes.html เป๊ะ ๆ
ให้สร้างเป็น chapter-[เลขสองหลัก]-notes.html
จัดเป็น hero, quick frame, sticky toc และ segment ตามเนื้อหาจริง
อย่าสร้าง mini test, mock exam หรือ answer key เพิ่มเอง เว้นแต่ฉันสั่งให้สร้าง
ถ้ามีรายการบัญชีให้จัด Dr/Cr เป็นหลายบรรทัดใน pre code
ถ้ามีตารางให้ใช้รูปแบบตารางของบท 6
ห้ามตัดประเด็นสำคัญจาก source และถ้าข้อมูลไม่ชัดให้ flag ไว้

[วางเนื้อหาต้นฉบับที่นี่]
```

## Short Builder Formula

เวลาแปลง source เป็นชีท ให้คิดตามสูตรนี้

```text
Raw material
-> group by exam logic
-> choose 4 quick frames
-> split into 3-5 segments
-> add rule/formula/callout/table per segment
-> add mini test / mock exam / answer key only if source has them or user asks for them
-> verify links, tables, and pre code line breaks
```
