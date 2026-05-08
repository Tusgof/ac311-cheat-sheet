# Segment 03 Raw Output

## Chapter Map Snapshot

- Segment 1: Standard objective, scope, impairment indicators, and assets that require annual testing
- Segment 2: Definition of impairment, recoverable amount, fair value less costs of disposal, and value in use
- Segment 3: Measuring impairment loss, journal logic, depreciation after impairment, and applied impairment cases
- Segment 4: Reversal of impairment, ceiling rule, revalued-asset interaction, goodwill boundary, and full exam watch

## Current Segment

- Chapter: 7
- Topic boundary: Measuring impairment loss and accounting after recognition
- Standard anchor: TAS 36 Impairment of Assets

## Deep Teaching

เมื่อเรารู้แล้วว่า recoverable amount เท่าไร ขั้นที่ตามมาคือการวัด `impairment loss` และบันทึกบัญชีให้ครบ ซึ่งจุดนี้เป็นช่วงที่ข้อสอบชอบผูก computation เข้ากับ journal entries และต่อยอดไปถึง depreciation ของงวดถัดไป

### 1. Measuring impairment loss

ลำดับคิดมาตรฐานคือ

1. Determine `carrying amount`
2. Determine `FVLCD`
3. Determine `VIU`
4. Take the higher of FVLCD and VIU as `recoverable amount`
5. Compare recoverable amount with carrying amount
6. Recognize impairment loss for the excess carrying amount

สูตรตรง ๆ:

`Impairment loss = Carrying amount - Recoverable amount`

เฉพาะเมื่อ carrying amount มากกว่า recoverable amount

### 2. Journal logic

ในโจทย์พื้นฐาน มักบันทึกเป็น

```text
Dr Impairment Loss
   Cr Asset
```

แต่บางโจทย์อาจใช้บัญชี contra เช่น accumulated impairment หรือสะท้อนผ่าน accumulated depreciation ตามรูปแบบ presentation ที่อาจารย์กำหนด ดังนั้นเวลาทำข้อสอบต้องอ่านว่าต้องการให้เครดิตที่ asset ตรง ๆ หรือผ่าน related contra account

### 3. Depreciation after impairment

หลายคนคิดว่าพอบันทึก impairment แล้วจบ แต่จริง ๆ impairment จะเปลี่ยนฐานคิดค่าเสื่อมของงวดถัดไปทันที

สูตร:

`Depreciation after impairment = (new carrying amount - residual value) / remaining useful life`

ดังนั้น impairment ไม่ใช่ one-time event อย่างเดียว แต่เปลี่ยน periodic expense ในอนาคตด้วย

### 4. Worked example

สมมติ:

- เครื่องจักร carrying amount = 840,000
- FVLCD = 700,000
- VIU = 760,000
- Residual value = 0
- Remaining useful life = 4 ปี

วิเคราะห์:

- Recoverable amount = higher of 700,000 and 760,000 = `760,000`
- Impairment loss = 840,000 - 760,000 = `80,000`

Journal entry:

```text
Dr Impairment Loss 80,000
   Cr Machinery 80,000
```

หลัง impairment:

- New carrying amount = `760,000`
- Depreciation ใหม่ต่อปี = 760,000 / 4 = `190,000`

### 5. Applied impairment cases

slide ของบทนี้ไม่ได้หยุดแค่คำนวณตัวเลข แต่ชอบพาไปถึง

- identify indicator
- determine recoverable amount
- calculate impairment loss
- prepare journal entry
- recompute next-period depreciation
- บางกรณีให้แสดงผลกระทบในงบแสดงฐานะการเงินและงบกำไรขาดทุนเบ็ดเสร็จ

ดังนั้นตรรกะที่ต้องแม่นคือ “จาก trigger ไปจนถึง presentation” ไม่ใช่แค่จำสูตร

## Mini Practice

บริษัท ริเวอร์ฟู้ด จำกัด มีเครื่องจักรผลิตอาหารแช่แข็ง ณ วันที่ 31 ธันวาคม 20X7 โดยมีข้อมูลดังนี้

- Carrying amount = 1,200,000 บาท
- Fair value = 1,020,000 บาท
- Costs of disposal = 40,000 บาท
- Value in use = 950,000 บาท
- Remaining useful life หลังวันที่ 31 ธันวาคม 20X7 = 5 ปี
- Residual value = 0

จงทำต่อไปนี้

1. คำนวณ `FVLCD`
2. คำนวณ `recoverable amount`
3. คำนวณ `impairment loss`
4. จัดทำ journal entry สำหรับการรับรู้ impairment
5. คำนวณค่าเสื่อมราคาสำหรับปี 20X8 หลัง impairment

## Solution

1. `FVLCD = 1,020,000 - 40,000 = 980,000 บาท`
2. `Recoverable amount = higher of 980,000 and 950,000 = 980,000 บาท`
3. `Impairment loss = 1,200,000 - 980,000 = 220,000 บาท`
4. Journal entry

```text
Dr Impairment Loss 220,000
   Cr Machinery 220,000
```

5. ค่าเสื่อมราคาปี 20X8 หลัง impairment = `980,000 / 5 = 196,000 บาท`

## Exam Watch

- วัด recoverable amount ก่อนเสมอ แล้วค่อยหาผลขาดทุน
- อย่าบันทึก impairment loss จากตัวเลข valuation ตัวแรกที่เห็น
- หลัง impairment ต้อง recalibrate ค่าเสื่อมของงวดถัดไปทันที
- ข้อสอบชอบลากจาก measurement ไปถึง journal entry และ statement effect

