# รายการตัวเลขที่ต้องการคัดค่าที่ไม่ซ้ำ
numbers = [3, 1, 3, 2, 1, 4, 2]

# สร้างรายการว่างไว้เก็บตัวเลขที่พบเป็นครั้งแรก
unique_numbers = []

# ตรวจตัวเลขทีละตัวจากรายการเดิม
for number in numbers:
    # ถ้ายังไม่มีตัวเลขนี้ในรายการผลลัพธ์ ให้เพิ่มเข้าไป
    if number not in unique_numbers:
        unique_numbers.append(number)

# แสดงรายการตัวเลขที่ไม่ซ้ำ โดยยังคงลำดับที่พบ
print(unique_numbers)