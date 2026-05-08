# Segment 04 Raw Output

## Chapter Map Snapshot

- Segment 1: Measurement after recognition, Cost model, Revaluation model
- Segment 2: Revaluation increase, Revaluation decrease, Sequence effect
- Segment 3: Accumulated depreciation at revaluation date, Eliminate method, Restate method
- Segment 4: Depreciation after revaluation, Transfer of revaluation surplus, Disposal of revalued assets

## Current Segment

- Chapter: 6
- Topic boundary: Depreciation after revaluation and disposal sequence
- Standard anchor: TAS 16 Property, Plant and Equipment

## Deep Teaching

หลังจากกิจการทำ `revaluation` แล้ว งานบัญชียังไม่จบเพียงแค่การปรับ carrying amount เพราะฐานใหม่จะส่งผลต่อ

- ค่าเสื่อมราคาในอนาคต
- การโอน `revaluation surplus`
- การบันทึกบัญชีเมื่อสินทรัพย์ถูกขาย

### Depreciation after revaluation

สูตร:

`(Revalued carrying amount - Residual value) / Remaining useful life`

ตัวอย่างเดิม:

- Revalued amount = 72,000
- Remaining useful life = 3 ปี

ดังนั้นค่าเสื่อมใหม่ต่อปี = `24,000`

จุดสำคัญคือ หลัง revaluation ห้ามกลับไปใช้ต้นทุนเดิมเป็นฐานคิดค่าเสื่อม

### ถ้าเคยตีราคาลดลงมาก่อน

ถ้าสินทรัพย์ที่เสื่อมราคาได้เคยมี `revaluation loss` มาก่อน ฐานค่าเสื่อมใหม่จะต่ำลง ทำให้ค่าเสื่อมในปีถัด ๆ ไปต่ำลงตาม

ผลที่ตามมาคือ:

- ค่าใช้จ่ายลดลง
- กำไรสุทธิเพิ่มขึ้นเมื่อเทียบกับกรณีที่ไม่เคยตีราคาลดลง
- กำไรสะสมจึงค่อย ๆ ฟื้นตัวกลับมาทางอ้อมผ่าน P/L

จุดสำคัญคือ การฟื้นตัวนี้ **ไม่ได้เกิดจากการโอนบัญชีขาดทุนโดยตรง** เพราะฝั่งขาดทุนไม่มีบัญชีสะสมแบบ `revaluation surplus`

จำแบบเร็ว:

`loss recovers indirectly through lower depreciation`

### Transfer of revaluation surplus

ยอด `revaluation surplus` อยู่ใน equity และสามารถโอนไป `retained earnings` ได้

1. เมื่อสินทรัพย์ถูกจำหน่าย
2. หรือโอนทยอยตามการใช้งาน

ถ้าโอนทยอย จำนวนที่โอนได้คือ

`Depreciation based on revalued amount - Depreciation based on original cost`

เช่น ถ้าค่าเสื่อมตามต้นทุนเดิม = 20,000 และหลัง revaluation = 24,000 ส่วนต่างที่โอนได้คือ 4,000

```text
Dr Revaluation Surplus 4,000
   Cr Retained Earnings 4,000
```

รายการนี้เป็น `equity to equity transfer` ไม่ผ่าน P/L

### ความต่างระหว่างฝั่ง surplus กับฝั่ง loss

- ฝั่ง `revaluation surplus` ต้องมีการโอนตรง `Dr Revaluation Surplus / Cr Retained Earnings` ถ้ากิจการเลือกโอนทยอยหรือโอนเมื่อจำหน่าย
- แต่ฝั่ง `revaluation loss` ไม่มีรายการโอนลักษณะเดียวกัน
- เหตุผลคือ surplus ถูกพักอยู่นอก P/L ตั้งแต่ต้น จึงต้องมีทางย้ายกลับเข้า `retained earnings`
- ส่วน loss ถูกลง P/L ไปแล้วตั้งแต่วันแรก การชดเชยจึงเกิดเองผ่านค่าเสื่อมที่ลดลงในอนาคต

### เพดานการกลับรายการสำหรับสินทรัพย์เสื่อมราคาได้

เมื่อมูลค่าสินทรัพย์ฟื้นกลับขึ้นมา อย่าคิดว่าขาดทุนเดิมทั้งก้อนยังรอ reverse อยู่ครบทุกบาท

- ถ้าระหว่างทางกิจการได้ประโยชน์จากค่าเสื่อมที่ลดลงแล้ว ส่วนนี้ถือว่าได้รับการชดเชยไปบางส่วน
- ดังนั้นยอดที่กลับเข้า P/L ได้จริงจะค่อย ๆ แคบลงตามเวลา
- วิธีเช็กแบบสอบคือ carrying amount หลังกลับรายการต้องไม่สูงกว่ามูลค่าตามบัญชีที่ควรจะเป็น หากไม่เคยตีราคาลดลงมาก่อน

### Disposal sequence

ถ้าสินทรัพย์ที่เคย revalue ถูกขาย ลำดับที่ถูกต้องคือ

1. บันทึกค่าเสื่อมถึงวันขายก่อน
2. หา carrying amount ณ วันขาย
3. เปรียบเทียบกับราคาขายเพื่อหากำไรหรือขาดทุนจากการขาย
4. โอน revaluation surplus ที่เกี่ยวข้องไป retained earnings

ตัวอย่าง:

- Revalued amount ณ 31/12/X2 = 72,000
- ขายวันที่ 1/7/X3 ราคา 65,000
- ค่าเสื่อมต่อปี 24,000

ครึ่งปีแรกของ X3:

```text
Dr Depreciation Expense 12,000
   Cr Accumulated Depreciation 12,000
```

Carrying amount ณ วันขาย = 72,000 - 12,000 = `60,000`

ขายได้ 65,000 จึงมีกำไรจากการขาย = `5,000`

```text
Dr Cash 65,000
Dr Accumulated Depreciation 12,000
   Cr Equipment 72,000
   Cr Gain on Sale 5,000
```

ถ้ายังมียอด revaluation surplus คงเหลือ 10,000:

```text
Dr Revaluation Surplus 10,000
   Cr Retained Earnings 10,000
```

## Mini Practice

บริษัท รุ่งเรืองวิศวกรรม จำกัด ซื้ออุปกรณ์เมื่อวันที่ 1 มกราคม 20X1 ในราคา 500,000 บาท อายุการใช้งาน 5 ปี ไม่มีมูลค่าคงเหลือ และใช้วิธีเส้นตรง

ณ วันที่ 31 ธันวาคม 20X2 กิจการใช้นโยบาย `revaluation model` และตีราคาอุปกรณ์ใหม่เป็น 360,000 บาท โดยรับรู้ส่วนเกินจากการตีราคาไว้ใน `revaluation surplus`

ต่อมาในวันที่ 1 กรกฎาคม 20X3 กิจการขายอุปกรณ์ดังกล่าวในราคา 340,000 บาท

จงทำต่อไปนี้

1. คำนวณ carrying amount ก่อน revaluation ณ 31/12/X2
2. คำนวณ carrying amount หลัง revaluation
3. คำนวณค่าเสื่อมครึ่งปีแรกของ 20X3
4. คำนวณ carrying amount ณ วันที่ขาย
5. คำนวณกำไรหรือขาดทุนจากการขาย
6. จัดทำ journal entries สำหรับค่าเสื่อม การขาย และการโอน revaluation surplus

## Solution

- ค่าเสื่อมต่อปีเดิม = 500,000 / 5 = 100,000 บาท
- ค่าเสื่อมสะสม 2 ปี = 200,000 บาท
- Carrying amount ก่อน revaluation = `300,000 บาท`
- Carrying amount หลัง revaluation = `360,000 บาท`
- ค่าเสื่อมใหม่ต่อปี = 360,000 / 3 = 120,000 บาท
- ค่าเสื่อมครึ่งปีแรกของ 20X3 = `60,000 บาท`
- Carrying amount ณ วันที่ขาย = 360,000 - 60,000 = `300,000 บาท`
- Gain on sale = 340,000 - 300,000 = `40,000 บาท`

```text
1/7/X3
Dr Depreciation Expense 60,000
   Cr Accumulated Depreciation 60,000

Dr Cash 340,000
Dr Accumulated Depreciation 60,000
   Cr Equipment 360,000
   Cr Gain on Sale 40,000

Dr Revaluation Surplus 60,000
   Cr Retained Earnings 60,000
```

## Exam Watch

- หลัง revaluation ค่าเสื่อมต้องคิดจากฐานใหม่
- วันขายต้องบันทึกค่าเสื่อมถึงวันขายก่อน
- แยก `gain on sale` ออกจาก `transfer of revaluation surplus`
- การโอน surplus ไม่ผ่าน `profit or loss`
- ถ้าโจทย์มี `revaluation loss` ของสินทรัพย์เสื่อมราคาได้ ให้ถามต่อเสมอว่าค่าเสื่อมใหม่ต่ำลงเท่าไร และกิจการได้คืน loss ไปแล้วบางส่วนหรือยัง

