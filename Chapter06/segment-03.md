# Segment 03 Raw Output

## Chapter Map Snapshot

- Segment 1: Measurement after recognition, Cost model, Revaluation model
- Segment 2: Revaluation increase, Revaluation decrease, Sequence effect
- Segment 3: Accumulated depreciation at revaluation date, Eliminate method, Restate method
- Segment 4: Depreciation after revaluation, Transfer of revaluation surplus, Disposal of revalued assets

## Current Segment

- Chapter: 6
- Topic boundary: Accumulated depreciation at revaluation date
- Standard anchor: TAS 16 Property, Plant and Equipment

## Deep Teaching

เมื่อกิจการใช้ `revaluation model` กับสินทรัพย์ที่มีการคิดค่าเสื่อมราคาอยู่แล้ว เช่น เครื่องจักร อุปกรณ์ หรืออาคาร ประเด็นไม่ได้มีแค่ว่า fair value ใหม่เท่าไร แต่ยังต้องตอบให้ได้ว่า `accumulated depreciation เดิมจะจัดการอย่างไร`

เป้าหมายสุดท้ายของทุกวิธีคือ

`net carrying amount after revaluation = revalued amount`

### ข้อมูลตั้งต้นตัวอย่าง

- ซื้อเครื่องจักร 1 มกราคม 25X1 ราคา 100,000 บาท
- อายุการใช้งาน 5 ปี
- ไม่มี residual value
- ค่าเสื่อมราคาปีละ 20,000 บาท
- สิ้นปี 25X2 accumulated depreciation = 40,000 บาท
- Carrying amount ก่อน revaluation = 60,000 บาท
- Fair value ใหม่ = 72,000 บาท

### Eliminate method

วิธีนี้คือการล้าง accumulated depreciation ออกก่อน แล้วค่อยปรับยอดสินทรัพย์ให้ถึง fair value ใหม่

```text
ก่อน revaluation
Equipment                       100,000
Less: Accumulated depreciation   40,000
Carrying amount                  60,000

Step 1 ล้าง accumulated depreciation
Dr Accumulated Depreciation 40,000
   Cr Equipment 40,000

หลัง Step 1
Equipment 60,000
Accumulated depreciation 0

Step 2 ปรับจาก 60,000 เป็น 72,000
Dr Equipment 12,000
   Cr Revaluation Surplus 12,000
```

ผลสุดท้าย:

- Equipment = 72,000
- Accumulated depreciation = 0
- Carrying amount = 72,000

### Restate method

วิธีนี้ไม่ล้าง accumulated depreciation ทิ้งทั้งหมด แต่ปรับทั้ง gross amount และ accumulated depreciation ให้เป็นสัดส่วนใหม่

อัตราปรับ:

`72,000 / 60,000 = 1.2 เท่า`

ดังนั้น

- Gross amount ใหม่ = 100,000 x 1.2 = 120,000
- Accumulated depreciation ใหม่ = 40,000 x 1.2 = 48,000

ตรวจสอบ:

`120,000 - 48,000 = 72,000`

```text
Dr Equipment 20,000
   Cr Accumulated Depreciation 8,000
   Cr Revaluation Surplus 12,000
```

### สรุปแกนคิด

สองวิธีต่างกันที่ `mechanics` ไม่ได้ต่างกันที่ผลลัพธ์สุทธิ เพราะมาตรฐานต้องการให้ net carrying amount จบที่ fair value เดียวกัน

## Mini Practice

บริษัท เมืองทองแมชชีนเนอรี่ จำกัด ซื้อเครื่องจักรเมื่อวันที่ 1 มกราคม 20X1 ในราคา 480,000 บาท อายุการใช้งาน 6 ปี ไม่มีมูลค่าคงเหลือ และใช้วิธีเส้นตรง กิจการใช้นโยบาย `revaluation model`

ณ วันที่ 31 ธันวาคม 20X2 เครื่องจักรมี fair value เท่ากับ 360,000 บาท

จงทำต่อไปนี้

1. คำนวณ carrying amount ก่อน revaluation
2. แสดงวิธีทำภายใต้ `eliminate method`
3. แสดงวิธีทำภายใต้ `restated method`
4. อธิบายว่าทำไมทั้ง 2 วิธีจึงต้องจบที่ net carrying amount เดียวกัน

## Solution

- ค่าเสื่อมต่อปี = 480,000 / 6 = 80,000 บาท
- ค่าเสื่อมสะสม 2 ปี = 160,000 บาท
- Carrying amount ก่อน revaluation = `320,000 บาท`

Eliminate method:

```text
Dr Accumulated Depreciation 160,000
   Cr Machinery 160,000

Dr Machinery 40,000
   Cr Revaluation Surplus 40,000
```

Restated method:

- อัตราปรับ = 360,000 / 320,000 = `1.125 เท่า`
- Gross amount ใหม่ = 480,000 x 1.125 = 540,000
- Accumulated depreciation ใหม่ = 160,000 x 1.125 = 180,000

```text
Dr Machinery 60,000
   Cr Accumulated Depreciation 20,000
   Cr Revaluation Surplus 40,000
```

เหตุผลที่คำตอบสุทธิต้องเท่ากัน เพราะเป้าหมายของมาตรฐานคือให้ `net carrying amount = revalued amount`

## Exam Watch

- ถ้าโจทย์สั่ง `restated method` ให้หา ratio ก่อน
- ถ้าโจทย์สั่ง `eliminate method` ให้ล้าง accumulated depreciation ก่อนเสมอ
- อย่าปรับเฉพาะ cost ใน restated method

