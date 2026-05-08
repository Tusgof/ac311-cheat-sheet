# Segment 02 Raw Output

## Chapter Map Snapshot

- Segment 1: Measurement after recognition, Cost model, Revaluation model
- Segment 2: Revaluation increase, Revaluation decrease, Sequence effect
- Segment 3: Accumulated depreciation at revaluation date, Eliminate method, Restate method
- Segment 4: Depreciation after revaluation, Transfer of revaluation surplus, Disposal of revalued assets

## Current Segment

- Chapter: 6
- Topic boundary: Revaluation increase, Revaluation decrease, and repeated revaluations
- Standard anchor: TAS 16 Property, Plant and Equipment

## Deep Teaching

เมื่อกิจการเลือกใช้ `revaluation model` คำถามต่อมาที่สำคัญที่สุดคือ “ส่วนต่างจากการตีราคาใหม่จะรับรู้ที่ไหน” จุดนี้คือกับดักใหญ่ของ Chapter 6 เพราะคำตอบไม่ใช่เข้า `profit or loss` ทั้งหมด และไม่ใช่เข้า `OCI` ทั้งหมดเสมอไป

### Revaluation increase

ถ้า carrying amount ของสินทรัพย์เพิ่มขึ้นเพราะ revaluation หลักทั่วไปคือ

`Increase -> OCI -> Revaluation surplus`

ตัวอย่างง่าย:

- Carrying amount เดิม 40,000
- Fair value ใหม่ 45,000
- Increase = 5,000

```text
Dr Land 5,000
   Cr Revaluation Surplus 5,000
```

### ข้อยกเว้นของ increase

ถ้าสินทรัพย์ตัวเดียวกันเคยถูก revalue ลดลงและกิจการรับรู้ขาดทุนไว้ใน `profit or loss` มาก่อน increase รอบใหม่ต้อง reverse ขาดทุนเดิมใน P/L ก่อน ส่วนเกินจึงค่อยไป OCI

จำแบบเร็ว:

`Increase after prior loss -> reverse P/L first -> excess to OCI`

### Revaluation decrease

ถ้า carrying amount ของสินทรัพย์ลดลงเพราะ revaluation หลักทั่วไปคือ

`Decrease -> Profit or loss`

ตัวอย่างง่าย:

- Carrying amount เดิม 40,000
- Fair value ใหม่ 38,000
- Decrease = 2,000

```text
Dr Loss from Revaluation 2,000
   Cr Land 2,000
```

### ข้อยกเว้นของ decrease

ถ้าสินทรัพย์ตัวนั้นมียอด `revaluation surplus` คงเหลืออยู่แล้ว ส่วนที่ลดลงจะต้องไปลด `OCI / revaluation surplus` ก่อนเท่าที่ยอดคงเหลือมี ส่วนที่เกินค่อยลง P/L

จำแบบเร็ว:

`Decrease with existing surplus -> use OCI first -> excess to P/L`

### Sequence effect

ข้อสอบชอบให้สินทรัพย์ตัวเดียวถูกตีราคาหลายรอบ เพราะบังคับให้เราจำได้ว่าต้องติดตาม history ของ `same asset`

| รูปแบบ | วิธีคิด |
| --- | --- |
| ขึ้นก่อน แล้วลงทีหลัง | ใช้ revaluation surplus เดิมก่อน แล้วส่วนเกินค่อยลง P/L |
| ลงก่อน แล้วขึ้นทีหลัง | reverse ขาดทุนเดิมใน P/L ก่อน แล้วส่วนเกินค่อยไป OCI |

#### กรณี 1: ขึ้นก่อน แล้วลงทีหลัง

- 400,000 -> 450,000 -> 380,000
- รอบแรกเพิ่ม 50,000 -> OCI
- รอบถัดมาลด 70,000
- ใช้ surplus เดิม 50,000 ก่อน
- อีก 20,000 ลง P/L

```text
Dr Revaluation Surplus 50,000
Dr Loss from Revaluation 20,000
   Cr Land 70,000
```

#### กรณี 2: ลงก่อน แล้วขึ้นทีหลัง

- 400,000 -> 340,000 -> 430,000
- รอบแรกลด 60,000 -> P/L
- รอบถัดมาเพิ่ม 90,000
- reverse loss เดิมใน P/L ก่อน 60,000
- ส่วนเกิน 30,000 -> OCI

```text
Dr Land 90,000
   Cr Recovery from Revaluation 60,000
   Cr Revaluation Surplus 30,000
```

## Mini Practice

บริษัท ศิลาไทย จำกัด มีที่ดินแปลงหนึ่งซึ่งรับรู้ครั้งแรกเมื่อวันที่ 1 มกราคม 20X1 ในราคาทุน 1,200,000 บาท และกิจการใช้นโยบาย `revaluation model` สำหรับ class ของที่ดินทั้งหมด

ข้อมูลเพิ่มเติม:

- 31 ธันวาคม 20X2 fair value = 1,350,000 บาท
- 31 ธันวาคม 20X3 fair value = 1,140,000 บาท
- 31 ธันวาคม 20X4 fair value = 1,290,000 บาท

จงทำต่อไปนี้

1. จัดทำตารางวิเคราะห์จำนวนที่รับรู้ใน `OCI` และ `profit or loss` สำหรับปี 20X2, 20X3 และ 20X4
2. จัดทำ journal entries ของแต่ละปี
3. อธิบาย logic ของปี 20X4 ว่าทำไม increase รอบนั้นไม่เข้า OCI ทั้งหมด

## Solution

| ปี | Carrying amount เดิม | Fair value ใหม่ | OCI | P/L |
| --- | --- | --- | --- | --- |
| 20X2 | 1,200,000 | 1,350,000 | 150,000 | 0 |
| 20X3 | 1,350,000 | 1,140,000 | (150,000) | (60,000) |
| 20X4 | 1,140,000 | 1,290,000 | 90,000 | 60,000 recovery |

```text
31/12/X2
Dr Land 150,000
   Cr Revaluation Surplus 150,000

31/12/X3
Dr Revaluation Surplus 150,000
Dr Loss from Revaluation 60,000
   Cr Land 210,000

31/12/X4
Dr Land 150,000
   Cr Recovery from Revaluation 60,000
   Cr Revaluation Surplus 90,000
```

Logic ของปี 20X4 คือ กิจการเคยรับรู้ `revaluation decrease` จำนวน 60,000 บาทใน `profit or loss` มาก่อน ดังนั้น increase รอบใหม่ต้อง reverse ขาดทุนเดิมใน P/L ก่อน ส่วนที่เหลือจึงค่อยไป OCI

## Exam Watch

- Increase ไม่ได้เข้า OCI ทั้งหมดเสมอไป
- Decrease ไม่ได้เข้า P/L ทั้งหมดเสมอไป
- คำว่า `same asset` สำคัญมาก
- ถ้าโจทย์หลายปี ให้คิดทีละรอบ ไม่ต้องพยายามหายอดสุทธิรวดเดียว

