# AC311 Chapter 7 Mock Exam

## Instructions

- This is a difficult mixed-concept exam for Chapter 7 only.
- Show calculations clearly.
- Support every conclusion with the correct TAS 36 logic.
- Provide journal entries where required.

## Question 1: Trigger, Recoverable Amount, and Impairment

บริษัท ไทยไพศาลแมชชีน จำกัด ปิดงบวันที่ 31 ธันวาคม 20X8 และพบว่าเครื่องจักรหลักที่ใช้ในสายการผลิตมีประสิทธิภาพลดลงจากเทคโนโลยีของคู่แข่งที่ใหม่กว่าอย่างมาก

ข้อมูลของเครื่องจักร ณ วันสิ้นงวด:

- Carrying amount = 1,480,000 บาท
- Fair value = 1,260,000 บาท
- Costs of disposal = 60,000 บาท
- Value in use = 1,300,000 บาท
- Remaining useful life = 5 ปี
- Residual value = 0

จงทำต่อไปนี้

1. ระบุ impairment indicator ของกรณีนี้
2. คำนวณ `FVLCD`
3. คำนวณ `recoverable amount`
4. คำนวณ `impairment loss`
5. จัดทำ journal entry
6. คำนวณค่าเสื่อมราคาสำหรับปี 20X9 หลัง impairment

## Question 2: Annual Testing and Reversal Boundary

บริษัท วิชั่นมีเดีย จำกัด มีสินทรัพย์ดังต่อไปนี้ ณ วันที่ 31 ธันวาคม 20X9

- `Goodwill` จากการซื้อกิจการ
- เครื่องหมายการค้าที่มี `indefinite useful life`
- โปรแกรมซอฟต์แวร์ที่ยังไม่พร้อมใช้งาน
- อุปกรณ์ตัดต่อที่เคยรับรู้ impairment ในปีก่อน ปัจจุบัน carrying amount = 390,000 บาท

ข้อมูลเพิ่มเติมของอุปกรณ์ตัดต่อ:

- หากไม่เคยมี impairment มาก่อน carrying amount ณ วันที่ 31 ธันวาคม 20X9 หลังหักค่าเสื่อมตามปกติจะเท่ากับ 460,000 บาท
- ปีนี้ recoverable amount ใหม่ = 510,000 บาท
- การปรับดีขึ้นเกิดจากประมาณการกระแสเงินสดใหม่ที่ดีขึ้นอย่างมีหลักฐานรองรับ

จงทำต่อไปนี้

1. รายการใดบ้างที่ต้องทดสอบ impairment ทุกปีแม้ไม่มี indicator
2. สำหรับอุปกรณ์ตัดต่อ พิจารณาว่าสามารถ reverse impairment ได้หรือไม่
3. คำนวณจำนวน reversal ที่รับรู้ได้
4. จัดทำ journal entry สำหรับ reversal
5. อธิบายว่าทำไมจึงไม่ reverse ไปถึง recoverable amount 510,000 บาทเต็มจำนวน
6. อธิบายว่า goodwill ใช้ reversal logic แบบเดียวกับอุปกรณ์ตัดต่อหรือไม่

## Model Solution

### Question 1

1. Indicator คือ adverse technological change และผลประโยชน์ทางเศรษฐกิจจากเครื่องจักรลดลง
2. `FVLCD = 1,260,000 - 60,000 = 1,200,000 บาท`
3. `Recoverable amount = higher of 1,200,000 and 1,300,000 = 1,300,000 บาท`
4. `Impairment loss = 1,480,000 - 1,300,000 = 180,000 บาท`
5. Journal entry

```text
Dr Impairment Loss 180,000
   Cr Machinery 180,000
```

6. Depreciation ปี 20X9 หลัง impairment = `1,300,000 / 5 = 260,000 บาท`

### Question 2

1. สินทรัพย์ที่ต้องทดสอบทุกปีแม้ไม่มี indicator:
   - `goodwill`
   - `intangible asset with indefinite useful life`
   - `intangible asset not yet available for use`
2. อุปกรณ์ตัดต่อสามารถ reverse ได้ เพราะมี change in estimates และไม่ใช่ goodwill
3. Ceiling ของ carrying amount หลัง reversal = 460,000 บาท
   ดังนั้น reversal = `460,000 - 390,000 = 70,000 บาท`
4. Journal entry

```text
Dr Equipment 70,000
   Cr Reversal Gain 70,000
```

5. Reverse ถึง 510,000 บาทไม่ได้ เพราะติด `ceiling rule`
6. Goodwill ใช้ reversal logic แบบเดียวกันไม่ได้ เพราะ goodwill ไม่ reverse impairment แบบ ordinary assets

