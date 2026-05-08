# Segment 02 Raw Output

## Chapter Map Snapshot

- Segment 1: Standard objective, scope, impairment indicators, and assets that require annual testing
- Segment 2: Definition of impairment, recoverable amount, fair value less costs of disposal, and value in use
- Segment 3: Measuring impairment loss, journal logic, depreciation after impairment, and applied impairment cases
- Segment 4: Reversal of impairment, ceiling rule, revalued-asset interaction, goodwill boundary, and full exam watch

## Current Segment

- Chapter: 7
- Topic boundary: Definition of impairment and recoverable amount
- Standard anchor: TAS 36 Impairment of Assets

## Deep Teaching

หลังจากรู้แล้วว่าเมื่อไรต้องเข้าสู่การทดสอบ impairment ขั้นต่อไปคือการตอบให้ได้ว่า “สินทรัพย์ impaired หรือยัง” ซึ่งคำตอบของ TAS 36 ตรงและเด็ดมาก:

`An asset is impaired when carrying amount exceeds recoverable amount`

ดังนั้นคำสำคัญที่สุดของ segment นี้มี 2 คำ

- `carrying amount`
- `recoverable amount`

### 1. Definition of impairment

ถ้า `carrying amount > recoverable amount` ส่วนเกินนั้นคือ `impairment loss`

นี่คือแกน logic ของทั้งบท และต้องจำให้แม่นว่า impairment ไม่ได้ดูจาก fair value อย่างเดียว แต่ดูจาก `recoverable amount`

### 2. Recoverable amount คืออะไร

มาตรฐานกำหนดว่า `recoverable amount` คือ “มูลค่าที่กู้คืนได้” และให้วัดเป็น

`higher of`

- `Fair value less costs of disposal (FVLCD)`
- `Value in use (VIU)`

จุดที่ชอบผิดกันมากคือหลายคนคิดว่าเพราะ impairment เป็นเรื่องอนุรักษ์นิยม จึงควรเลือกตัวเลขที่ต่ำกว่า แต่จริง ๆ มาตรฐานให้เลือก `ตัวที่สูงกว่า` เพราะ recoverable amount หมายถึงมูลค่าทางเศรษฐกิจที่กิจการยังพอจะกู้คืนได้ดีที่สุด ไม่ว่าจะจากการใช้ต่อหรือจากการขาย

จำแบบเร็ว:

`recoverable amount = higher of FVLCD and VIU`

### 3. Fair value less costs of disposal

`FVLCD` คือราคาที่จะได้รับจากการขายสินทรัพย์ในการทำรายการอย่างเป็นระเบียบระหว่าง market participants ณ วันวัดมูลค่า แล้วหัก `costs of disposal`

จุดสำคัญ:

- ต้องเป็น `incremental costs directly attributable to disposal`
- ไม่รวม `finance costs`
- ไม่รวม `income tax expense`

ดังนั้น disposal costs ต้องเป็นต้นทุนที่เกี่ยวกับการขายสินทรัพย์โดยตรง ไม่ใช่ค่าใช้จ่ายดำเนินงานทั่วไป

### 4. Value in use

`VIU` คือมูลค่าปัจจุบันของกระแสเงินสดในอนาคตที่คาดว่าจะได้รับจากการใช้สินทรัพย์ต่อเนื่อง และจากการจำหน่ายสินทรัพย์เมื่อสิ้นสุดการใช้

ต้องจำว่า

- FVLCD เป็น `sale-based value`
- VIU เป็น `use-based value`

VIU จึงเป็นแนวคิดเชิง entity-specific มากกว่า เพราะผูกกับการใช้สินทรัพย์ต่อในธุรกิจ

### 5. ภาพรวมการเลือก recoverable amount

ตัวอย่าง:

- Carrying amount = 900,000
- FVLCD = 720,000
- VIU = 760,000

Recoverable amount = `760,000` เพราะต้องเลือกตัวที่สูงกว่า

ถ้า carrying amount 900,000 มากกว่า recoverable amount 760,000 จึงเกิด impairment loss 140,000

### 6. จุดสับสนที่ออกสอบบ่อย

- เลือกค่าที่ต่ำกว่าระหว่าง FVLCD กับ VIU ซึ่งผิด
- เอา FVLCD ไปสับสนกับ fair value ดิบ ๆ โดยลืมหัก disposal costs
- คิดว่า VIU คือยอดขายในอนาคตแบบไม่ discount ทั้งที่มาตรฐานเน้น present value

## Mini Practice

บริษัท ศรีไทยฟู้ด จำกัด มีอุปกรณ์ผลิตอาหารสำเร็จรูป ณ วันที่ 31 ธันวาคม 20X6 โดยมีข้อมูลดังนี้

- Carrying amount = 1,050,000 บาท
- Fair value = 930,000 บาท
- Costs of disposal = 30,000 บาท
- Value in use = 980,000 บาท

จงทำต่อไปนี้

1. คำนวณ `fair value less costs of disposal`
2. คำนวณ `recoverable amount`
3. พิจารณาว่าสินทรัพย์ impaired หรือไม่
4. ถ้า impaired ให้คำนวณจำนวน impairment loss
5. อธิบายว่าทำไม recoverable amount ไม่ใช่ตัวเลขที่ต่ำกว่าระหว่าง FVLCD และ VIU

## Solution

1. `FVLCD = 930,000 - 30,000 = 900,000 บาท`
2. `Recoverable amount = higher of 900,000 and 980,000 = 980,000 บาท`
3. สินทรัพย์ impaired เพราะ carrying amount 1,050,000 มากกว่า recoverable amount 980,000
4. `Impairment loss = 1,050,000 - 980,000 = 70,000 บาท`
5. เพราะมาตรฐานนิยาม recoverable amount ว่าเป็นมูลค่าที่กิจการยังกู้คืนได้ดีที่สุด จึงต้องเลือกค่าที่สูงกว่าระหว่างมูลค่าจากการขายสุทธิและมูลค่าจากการใช้ต่อ

## Exam Watch

- จำให้แม่นว่า `recoverable amount = higher of FVLCD and VIU`
- ถ้าโจทย์ให้ fair value มาเฉย ๆ อย่าลืมหัก `costs of disposal`
- ถ้าโจทย์พูดถึง VIU ต้องนึกถึง present value logic
- Segment นี้เป็นแกนคำนวณของ impairment ทั้งบท

