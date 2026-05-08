# AC311 Chapter 6 Mock Exam

## Instructions

- This is a difficult mixed-concept exam for Chapter 6 only.
- Show calculations clearly.
- Separate amounts recognized in `OCI` and `profit or loss`.
- Provide journal entries where required.

## Question 1: Land A Revaluation Sequence

บริษัท ธาราอุตสาหกรรม จำกัด ใช้นโยบาย `revaluation model` สำหรับ class ของที่ดินทั้งหมด

ที่ดินแปลง A ซื้อเมื่อวันที่ 1 มกราคม 20X1 ในราคา 2,000,000 บาท

มูลค่ายุติธรรมของที่ดินแปลง A มีดังนี้

| วันที่ | Fair value |
| --- | --- |
| 31 ธันวาคม 20X2 | 2,260,000 |
| 31 ธันวาคม 20X3 | 1,980,000 |
| 31 ธันวาคม 20X4 | 2,140,000 |

จงทำต่อไปนี้

1. จัดทำตารางวิเคราะห์ revaluation increase หรือ decrease ในปี 20X2, 20X3 และ 20X4
2. แยกให้ชัดว่าแต่ละปีมีจำนวนเท่าไรรับรู้ใน `OCI` และเท่าไรรับรู้ใน `profit or loss`
3. จัดทำ journal entries สำหรับการ revaluation ของแต่ละปี
4. อธิบายเหตุผลของการรับรู้ในปี 20X4

## Question 2: Machinery B Revaluation and Disposal

เครื่องจักร B ซื้อเมื่อวันที่ 1 มกราคม 20X1 ในราคา 900,000 บาท อายุการใช้งาน 6 ปี ไม่มีมูลค่าคงเหลือ กิจการใช้วิธีเส้นตรง

ณ วันที่ 31 ธันวาคม 20X2 เครื่องจักร B มี fair value เท่ากับ 720,000 บาท

ต่อมา กิจการขายเครื่องจักร B เมื่อวันที่ 30 มิถุนายน 20X4 ในราคา 470,000 บาท

กำหนดให้กิจการใช้นโยบาย `revaluation model` สำหรับ class ของเครื่องจักรทั้งหมด และใช้ `eliminate method` ในวัน revaluation

จงทำต่อไปนี้

1. คำนวณ carrying amount ก่อน revaluation ณ 31 ธันวาคม 20X2
2. แสดงการจัดการ accumulated depreciation ภายใต้ eliminate method
3. คำนวณ carrying amount หลัง revaluation
4. คำนวณค่าเสื่อมราคาสำหรับปี 20X3 และครึ่งปีแรกของ 20X4
5. คำนวณ carrying amount ณ วันที่ขาย
6. คำนวณกำไรหรือขาดทุนจากการขาย
7. จัดทำ journal entries สำหรับการ revaluation ค่าเสื่อม การขาย และการโอน revaluation surplus
8. อธิบายว่าทำไมการโอน revaluation surplus จึงไม่ผ่าน `profit or loss`

## Model Solution

### Question 1

| ปี | Land A change | OCI | P/L |
| --- | --- | --- | --- |
| 20X2 | 2,000,000 -> 2,260,000 เพิ่ม 260,000 | 260,000 | 0 |
| 20X3 | 2,260,000 -> 1,980,000 ลด 280,000 | (260,000) | (20,000) |
| 20X4 | 1,980,000 -> 2,140,000 เพิ่ม 160,000 | 140,000 | 20,000 recovery |

```text
31/12/X2
Dr Land 260,000
   Cr Revaluation Surplus 260,000

31/12/X3
Dr Revaluation Surplus 260,000
Dr Loss from Revaluation 20,000
   Cr Land 280,000

31/12/X4
Dr Land 160,000
   Cr Recovery from Revaluation 20,000
   Cr Revaluation Surplus 140,000
```

Logic ของปี 20X4 คือ increase รอบใหม่ต้อง reverse prior loss ใน P/L ก่อน

### Question 2

- ค่าเสื่อมต่อปีเดิม = 900,000 / 6 = 150,000 บาท
- ค่าเสื่อมสะสม 2 ปี = 300,000 บาท
- Carrying amount ก่อน revaluation = `600,000 บาท`

```text
31/12/X2
Dr Accumulated Depreciation 300,000
   Cr Machinery 300,000

Dr Machinery 120,000
   Cr Revaluation Surplus 120,000
```

- Carrying amount หลัง revaluation = `720,000 บาท`
- ค่าเสื่อมปี 20X3 = 720,000 / 4 = `180,000 บาท`
- ค่าเสื่อมครึ่งปีแรกของ 20X4 = `90,000 บาท`
- Carrying amount ณ วันที่ขาย = 720,000 - 180,000 - 90,000 = `450,000 บาท`
- Gain on sale = 470,000 - 450,000 = `20,000 บาท`

```text
31/12/X3
Dr Depreciation Expense 180,000
   Cr Accumulated Depreciation 180,000

30/6/X4
Dr Depreciation Expense 90,000
   Cr Accumulated Depreciation 90,000

Dr Cash 470,000
Dr Accumulated Depreciation 270,000
   Cr Machinery 720,000
   Cr Gain on Sale 20,000

Dr Revaluation Surplus 120,000
   Cr Retained Earnings 120,000
```

การโอน revaluation surplus ไม่ผ่าน P/L เพราะเป็น `equity to equity transfer`

