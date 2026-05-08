# Segment 01 Raw Output

## Chapter Map Snapshot

- Segment 1: Measurement after recognition, Cost model, Revaluation model
- Segment 2: Revaluation increase, Revaluation decrease, Sequence effect
- Segment 3: Accumulated depreciation at revaluation date, Eliminate method, Restate method
- Segment 4: Depreciation after revaluation, Transfer of revaluation surplus, Disposal of revalued assets

## Current Segment

- Chapter: 6
- Topic boundary: Measurement after recognition of PPE
- Standard anchor: TAS 16 Property, Plant and Equipment
- Related reference: TFRS 13 Fair Value Measurement

## Deep Teaching

หลังจากกิจการรับรู้ `Property, Plant and Equipment (PPE)` ครั้งแรกแล้ว คำถามสำคัญของ Chapter 6 คือ “ต่อจากนี้จะวัดมูลค่าสินทรัพย์อย่างไร” คำถามนี้คือหัวใจของ `measurement after recognition` หรือ `subsequent measurement`

ภายใต้ `TAS 16` กิจการเลือกนโยบายบัญชีได้ 2 แบบ

- `Cost model`
- `Revaluation model`

แต่การเลือกนโยบายนี้ต้องใช้กับ `entire class of PPE` ไม่ใช่เลือกเฉพาะรายการที่อยากให้มูลค่าสูงขึ้น เพราะมาตรฐานต้องการความสม่ำเสมอและความสามารถในการเปรียบเทียบของงบการเงิน

### Cost model

ภายใต้ cost model สินทรัพย์จะถูกแสดงที่

`Cost - Accumulated depreciation - Accumulated impairment losses`

ดังนั้น cost model ไม่ได้แปลว่า “ถือไว้ที่ต้นทุนเดิมเฉย ๆ” แต่แปลว่าให้ยืนบนฐาน cost เดิม แล้วลดด้วย

- ค่าเสื่อมราคาสะสม (`accumulated depreciation`)
- ขาดทุนจากการด้อยค่าสะสม (`accumulated impairment losses`)

จุดนี้ออกสอบบ่อยมาก เพราะนักศึกษามักจำคำว่า cost model แบบสั้นเกินไป แล้วลืมว่า impairment ยังมีผลกับ carrying amount ได้

### Revaluation model

ภายใต้ revaluation model กิจการใช้ได้เมื่อ `fair value can be measured reliably`

หลังวันตีราคาใหม่ สินทรัพย์จะแสดงที่

`Fair value at revaluation date - Subsequent accumulated depreciation - Subsequent accumulated impairment losses`

ต้องเน้นว่า revaluation model ไม่ได้หมายความว่า fair value เข้าแทนที่ทุกอย่างแบบถาวรโดยไม่เกิดค่าเสื่อมอีก แต่หมายความว่า ณ วัน revaluation กิจการ reset ฐานมูลค่าไปที่ fair value แล้วจากนั้นยังต้องคิดค่าเสื่อมและ impairment ต่อจากฐานใหม่

มาตรฐานยังกำหนดว่า revaluation ต้องทำด้วย `sufficient regularity` เพื่อไม่ให้ carrying amount แตกต่างจาก fair value อย่างมีสาระสำคัญ

### เปรียบเทียบเชิงตัวเลข

สมมติ:

- ซื้ออุปกรณ์วันที่ 1 มกราคม 20X1 ราคา 100,000 บาท
- อายุการใช้งาน 5 ปี
- ไม่มีมูลค่าคงเหลือ
- ค่าเสื่อมราคาเส้นตรงปีละ 20,000 บาท

ณ 31 ธันวาคม 20X2

- Cost = 100,000
- Accumulated depreciation = 40,000
- Carrying amount ก่อน revaluation = 60,000
- Fair value = 72,000

ผลลัพธ์:

| รายการ | Cost model | Revaluation model |
| --- | --- | --- |
| Carrying amount ณ 31/12/X2 | 60,000 | 72,000 |
| ฐานคิดค่าเสื่อมหลังจากนั้น | 60,000 ตาม cost net | 72,000 ตาม revalued amount |

### ทำไมต้องใช้กับทั้ง class

ถ้าเปิดให้กิจการเลือกตีราคาเฉพาะสินทรัพย์ที่ fair value สูง แต่ไม่ตีสินทรัพย์ที่ fair value ต่ำ งบจะถูกปรับแต่งได้ง่าย มาตรฐานจึงบังคับให้เลือก policy ระดับ class เช่น ที่ดินทั้งกลุ่ม เครื่องจักรทั้งกลุ่ม หรืออาคารทั้งกลุ่ม

## Mini Practice

บริษัท เหนือฟ้าอุตสาหกรรม จำกัด ซื้อเครื่องจักรเมื่อวันที่ 1 มกราคม 20X1 ในราคา 750,000 บาท อายุการใช้งาน 5 ปี ไม่มีมูลค่าคงเหลือ และกิจการใช้วิธีเส้นตรงในการคิดค่าเสื่อมราคา

ณ วันที่ 31 ธันวาคม 20X2 ผู้ประเมินอิสระรายงานว่าเครื่องจักรดังกล่าวมี `fair value` เท่ากับ 510,000 บาท

จงทำต่อไปนี้

1. คำนวณ `carrying amount` ณ วันที่ 31 ธันวาคม 20X2 หากกิจการใช้ `cost model`
2. ถ้ากิจการเลือกใช้ `revaluation model` ณ วันเดียวกัน จงระบุ carrying amount ใหม่หลังการตีราคา
3. อธิบายว่าทำไมกิจการไม่ควรเลือกใช้ revaluation model เฉพาะเครื่องจักรเครื่องนี้ แต่ยังคงใช้ cost model กับเครื่องจักรอื่นใน class เดียวกัน
4. ถ้าหลังการ revalue แล้ว เครื่องจักรมีอายุใช้งานคงเหลืออีก 3 ปี จงคำนวณค่าเสื่อมราคาสำหรับปี 20X3

## Solution

- ค่าเสื่อมต่อปี = 750,000 / 5 = 150,000 บาท
- ค่าเสื่อมสะสม 2 ปี = 300,000 บาท
- Carrying amount ภายใต้ cost model = 750,000 - 300,000 = `450,000 บาท`
- Carrying amount ภายใต้ revaluation model ณ วันตีราคา = `510,000 บาท`
- ห้ามเลือกใช้ revaluation model เฉพาะบางรายการ เพราะ `TAS 16` กำหนดให้ใช้กับ `entire class of PPE`
- ค่าเสื่อมปี 20X3 หลัง revaluation = 510,000 / 3 = `170,000 บาท`

## Exam Watch

- อย่าสับสนว่า cost model คือไม่หัก impairment
- อย่าสับสนว่า revaluation model ตีราคาแล้วไม่คิดค่าเสื่อมต่อ
- ข้อสอบชอบถามคำว่า `entire class of PPE`
- Segment นี้เป็นฐานของทั้งบท ถ้าฐานนี้ไม่แม่น Segment 2 ถึง 4 จะสับสนทันที

