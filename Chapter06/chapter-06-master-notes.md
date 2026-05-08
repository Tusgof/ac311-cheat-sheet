# AC311 Chapter 6 Master Notes

## Run Mode

- Workflow mode: strict on-demand loop
- Chapter: 6
- Append order completed: 01 -> 02 -> 03 -> 04

## Refined Segment 01

### Core rule

หลังจากรับรู้ PPE ครั้งแรกแล้ว กิจการเลือก subsequent measurement ได้ 2 แบบ

- `Cost model`
- `Revaluation model`

การเลือกนี้ต้องใช้กับ `entire class of PPE`

### Cost model

`Carrying amount = Cost - Accumulated depreciation - Accumulated impairment losses`

ประเด็นสอบ:

- ยืนบนฐานต้นทุนเดิม
- ลดด้วยค่าเสื่อมและ impairment
- ไม่ใช่ถือไว้ที่ cost เฉย ๆ

### Revaluation model

ใช้ได้เมื่อ `fair value can be measured reliably`

`Carrying amount = Fair value at revaluation date - Subsequent accumulated depreciation - Subsequent accumulated impairment losses`

ประเด็นสอบ:

- fair value เป็นฐานใหม่ในวันตีราคา
- หลังจากนั้นยังต้องคิด depreciation และ impairment ต่อ
- ต้อง revalue ด้วย `sufficient regularity`

### Memory hook

`cost model = cost net`

`revaluation model = fair value reset, then depreciate again`

## Refined Segment 02

### Revaluation increase

หลักทั่วไป:

`Increase -> OCI -> Revaluation surplus`

ข้อยกเว้น:

ถ้าเคยมี prior loss ของสินทรัพย์ตัวเดียวกันใน P/L increase รอบใหม่ต้อง reverse P/L ก่อน

### Revaluation decrease

หลักทั่วไป:

`Decrease -> Profit or loss`

ข้อยกเว้น:

ถ้ามี existing revaluation surplus ของสินทรัพย์ตัวเดียวกัน decrease รอบใหม่ต้องใช้ surplus เดิมก่อน

### Sequence effect

| รูปแบบ | วิธีคิด |
| --- | --- |
| ขึ้นก่อน แล้วลงทีหลัง | ใช้ surplus เดิมก่อน แล้วส่วนเกินลง P/L |
| ลงก่อน แล้วขึ้นทีหลัง | reverse loss เดิมใน P/L ก่อน แล้วส่วนเกินไป OCI |

### Asymmetry ที่ต้องเข้าใจ

- `Increase` ปกติไป `OCI -> Revaluation surplus`
- `Decrease` ปกติไป `Profit or loss`
- ฝั่งกำไรมีบัญชีพักของตัวเองคือ `revaluation surplus`
- ฝั่งขาดทุนไม่มีบัญชีพักลักษณะเดียวกัน จึงกระทบ `retained earnings` ผ่าน P/L ทันที

### Memory hook

`reverse where it came from`

`gain is parked in surplus, but loss hits P/L immediately`

## Refined Segment 03

### Core target

เมื่อ PPE ที่เสื่อมราคาได้ถูก revalue เป้าหมายคือ

`net carrying amount after revaluation = revalued amount`

### Eliminate method

- ล้าง accumulated depreciation ออกก่อน
- จากนั้นค่อยปรับยอดสินทรัพย์ให้ถึง revalued amount

จำแบบเร็ว:

`remove AD first -> adjust net amount`

### Restated method

- ปรับทั้ง gross amount และ accumulated depreciation ให้เป็นสัดส่วนใหม่
- หา ratio จาก `fair value / old carrying amount`

จำแบบเร็ว:

`rescale gross amount and AD together`

### Key exam point

สองวิธีต่างกันที่ `mechanics` ไม่ใช่ผลลัพธ์สุทธิ

## Refined Segment 04

### Depreciation after revaluation

`(Revalued carrying amount - Residual value) / Remaining useful life`

จำแบบเร็ว:

`new amount -> new useful life -> new depreciation`

### If there was a prior revaluation loss

- สินทรัพย์เสื่อมราคาได้ที่ถูกตีราคาลดลงจะมีฐานค่าเสื่อมใหม่ต่ำลง
- ค่าเสื่อมอนาคตจึงต่ำลง และกำไรสะสมจะค่อย ๆ ฟื้นตัวทางอ้อมผ่าน P/L
- ไม่มีการโอนตรงจากบัญชีขาดทุนไป `retained earnings`

### Transfer of revaluation surplus

- โอนเมื่อจำหน่ายสินทรัพย์ได้
- โอนทยอยตามการใช้งานได้
- เป็น `equity to equity transfer`
- ไม่ผ่าน `profit or loss`

### Contrast with loss case

- ฝั่ง `surplus` ต้องโอนตรง `Dr Revaluation Surplus / Cr Retained Earnings`
- ฝั่ง `loss` ไม่ต้องมีรายการโอน เพราะระบบจะชดเชยผ่านค่าเสื่อมที่ลดลงเอง

### Ceiling on reversal

- สำหรับสินทรัพย์เสื่อมราคาได้ prior loss ที่ reverse กลับเข้า P/L ได้จะค่อย ๆ ลดลงเมื่อกิจการได้ประโยชน์จากค่าเสื่อมที่ต่ำลงไปแล้ว
- เช็กเพดานโดยดูว่า carrying amount หลัง reversal ต้องไม่เกิน carrying amount ที่ควรจะเป็น หากไม่เคยตีราคาลดลงมาก่อน

### Disposal sequence

1. Depreciation to date
2. Carrying amount at disposal date
3. Gain or loss on sale
4. Transfer of remaining revaluation surplus

### Key exam point

ห้ามปน `gain on sale` กับ `transfer of revaluation surplus`

## Cumulative Exam Watch

- แยก `measurement basis` ออกจาก `recognition location`
- ติดตาม history ของ `same asset`
- ในโจทย์หลายปีให้คิดทีละปี ทีละรอบ ไม่รวบ logic
- ถ้าเป็นสินทรัพย์เสื่อมราคาได้ ให้ถามต่อเสมอว่า accumulated depreciation จะจัดการอย่างไร
- หลัง revaluation ให้ถามต่อเสมอว่า depreciation ใหม่คิดจากฐานไหน
- ถ้าเคยมี `revaluation loss` มาก่อน อย่าลืมถามต่อว่า loss ก้อนนั้นถูกชดเชยทางอ้อมผ่านค่าเสื่อมที่ลดลงไปแล้วเท่าไร

