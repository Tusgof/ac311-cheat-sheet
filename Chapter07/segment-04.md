# Segment 04 Raw Output

## Chapter Map Snapshot

- Segment 1: Standard objective, scope, impairment indicators, and assets that require annual testing
- Segment 2: Definition of impairment, recoverable amount, fair value less costs of disposal, and value in use
- Segment 3: Measuring impairment loss, journal logic, depreciation after impairment, and applied impairment cases
- Segment 4: Reversal of impairment, ceiling rule, revalued-asset interaction, goodwill boundary, and full exam watch

## Current Segment

- Chapter: 7
- Topic boundary: Reversal of impairment and advanced boundaries
- Standard anchor: TAS 36 Impairment of Assets

## Deep Teaching

ส่วนท้ายของ Chapter 7 คือช่วงที่นักศึกษามักพลาดเพราะคิดง่าย ๆ ว่า “ถ้าสถานการณ์ดีขึ้นก็ reverse impairment ได้หมด” แต่ TAS 36 ไม่ได้อนุญาตกว้างขนาดนั้น ต้องผ่านเงื่อนไขและติดเพดาน (`ceiling rule`) ด้วย

### 1. Reversal of impairment loss

มาตรฐานกำหนดว่า ณ วันสิ้นงวดต้องประเมินด้วยว่า impairment loss ที่เคยรับรู้ในอดีตสำหรับสินทรัพย์ `other than goodwill` อาจไม่จำเป็นอีกต่อไป หรืออาจลดลงหรือไม่

ตัวอย่าง indicator ของ reversal

- มีการเปลี่ยนแปลงภายนอกในทางที่ดีขึ้น
- มีการเปลี่ยนแปลงภายในในทางที่ดีขึ้น
- ผลการดำเนินงานดีขึ้น
- อัตราดอกเบี้ยในตลาดลดลง
- มูลค่าสินทรัพย์เพิ่มขึ้น

แต่ reversal ไม่ใช่อัตโนมัติ ต้องมี `change in estimates used to determine recoverable amount`

### 2. Ceiling rule

แม้ recoverable amount ใหม่จะสูงขึ้น กิจการก็ reverse impairment ได้ไม่เกิน carrying amount ที่ “ควรจะเป็น” หากไม่เคยมี impairment มาก่อน หลังหัก depreciation หรือ amortisation ตามปกติแล้ว

นี่คือ `ceiling rule`

จำแบบเร็ว:

`reversal cannot push the asset above its no-impairment path`

### 3. Recognition of reversal

สำหรับ asset ปกติที่ไม่ใช่ goodwill การกลับรายการรับรู้ใน `profit or loss` ทันที

```text
Dr Asset or related contra account
   Cr Reversal Gain
```

แต่ถ้าสินทรัพย์นั้นเป็น `revalued asset` ภายใต้มาตรฐานอื่น เช่น TAS 16 ต้องเชื่อม treatment ของ reversal เข้ากับ revaluation model ของมาตรฐานนั้นด้วย

### 4. Goodwill boundary

ต้องจำให้ชัดว่า `goodwill`

- ต้องทดสอบ impairment ทุกปี
- แต่ reversal logic ในช่วงนี้ใช้กับ `assets other than goodwill`

ในการเขียนตอบข้อสอบ ห้ามเขียนแบบเหมารวมว่าเมื่อ recoverable amount ของ goodwill ดีขึ้นแล้ว reverse ได้ เพราะนั่นผิดหลักสำคัญของบทนี้

### 5. Worked example with ceiling

สมมติ:

- อุปกรณ์มี carrying amount เดิมก่อน impairment path ตามปกติ ณ 31/12/X8 ควรเหลือ 520,000 บาท ถ้าไม่เคย impaired
- แต่ปีก่อนกิจการรับรู้ impairment จน carrying amount เหลือ 430,000 บาท
- ปีนี้ recoverable amount ใหม่ = 560,000 บาท

คำถามคือ reverse ได้เท่าไร

คำตอบ:

- ทางทฤษฎี recoverable amount สูงขึ้นถึง 560,000
- แต่เพดาน reversal คือ 520,000 เพราะเป็น no-impairment carrying amount path
- ดังนั้น reverse ได้เพียง `520,000 - 430,000 = 90,000`

```text
Dr Equipment 90,000
   Cr Reversal Gain 90,000
```

### 6. สรุปปลายบท

Chapter 7 ต้องเดินตาม decision sequence นี้

1. ดูว่ามี indicator หรือเป็น annual-test asset หรือไม่
2. ถ้าต้องวัด ให้หา recoverable amount = higher of FVLCD and VIU
3. ถ้า carrying amount สูงกว่า recoverable amount ให้รับรู้ impairment loss
4. ปรับค่าเสื่อมในอนาคตจาก carrying amount ใหม่
5. ถ้างวดต่อมาสถานการณ์ดีขึ้น ให้ดู reversal indicators
6. ถ้า reverse ได้ ต้องไม่เกิน no-impairment ceiling
7. ห้ามใช้ reversal กับ goodwill แบบ asset ปกติ

## Mini Practice

บริษัท แสงไทยเทค จำกัด มีอุปกรณ์ชิ้นหนึ่งซึ่ง ณ วันที่ 31 ธันวาคม 20X8 มี carrying amount หลังจากรับรู้ impairment ในปีก่อนแล้วเท่ากับ 430,000 บาท

ถ้าไม่มีการรับรู้ impairment ในอดีต carrying amount ของอุปกรณ์นี้ ณ วันที่ 31 ธันวาคม 20X8 หลังหักค่าเสื่อมปกติจะเท่ากับ 520,000 บาท

ในปี 20X8 บริษัทประเมิน recoverable amount ใหม่ได้ 560,000 บาท และพบว่าการปรับดีขึ้นนี้เกิดจากประมาณการกระแสเงินสดใหม่ที่ดีกว่าเดิมอย่างมีหลักฐานรองรับ

จงทำต่อไปนี้

1. พิจารณาว่าสามารถ reverse impairment ได้หรือไม่
2. คำนวณจำนวน reversal ที่รับรู้ได้
3. จัดทำ journal entry
4. อธิบายว่าทำไมจึง reverse ไปถึง 560,000 บาทไม่ได้
5. อธิบายสั้น ๆ ว่าถ้าสินทรัพย์เป็น goodwill logic นี้จะใช้เหมือนเดิมหรือไม่

## Solution

1. สามารถ reverse ได้ เพราะมีการเปลี่ยนแปลงในประมาณการที่ใช้กำหนด recoverable amount และสินทรัพย์นี้ไม่ใช่ goodwill
2. Reversal ที่รับรู้ได้ = `520,000 - 430,000 = 90,000 บาท`
3. Journal entry

```text
Dr Equipment 90,000
   Cr Reversal Gain 90,000
```

4. Reverse ไปถึง 560,000 บาทไม่ได้ เพราะติด `ceiling rule` ซึ่งห้ามให้ carrying amount หลัง reversal สูงกว่ามูลค่าที่สินทรัพย์ควรจะเป็นหากไม่เคยมี impairment มาก่อน
5. ถ้าเป็น goodwill จะใช้ logic นี้ไม่ได้ เพราะ goodwill ไม่ใช่สินทรัพย์ที่ reverse impairment แบบ ordinary assets

## Exam Watch

- Reversal ไม่ใช่อัตโนมัติ
- ต้องมี `change in estimates`
- ต้องติดเพดาน `no-impairment path`
- ห้ามใช้ reversal logic แบบ asset ปกติกับ goodwill

