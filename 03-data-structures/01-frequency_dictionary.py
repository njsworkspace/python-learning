# กำหนดข้อความที่ต้องการนับจำนวนตัวอักษร
text = "Anuruk Janplang"

# ลบช่องว่างทั้งหมด แล้วแปลงตัวอักษรเป็นตัวพิมพ์เล็ก
text = text.replace(' ', '').lower()

# สร้าง dictionary สำหรับเก็บตัวอักษรและจำนวนครั้งที่พบ
count_characters = {}

# วนดูตัวอักษรแต่ละตัวในข้อความ
for character in text:
    # ถ้าเคยพบตัวอักษรนี้แล้ว ให้เพิ่มจำนวนขึ้น 1
    if character in count_characters:
        count_characters[character] += 1
    # ถ้ายังไม่เคยพบ ให้เพิ่มตัวอักษรนี้ลงใน dictionary โดยเริ่มนับที่ 1
    else:
        count_characters[character] = 1

# แสดงผลตัวอักษรแต่ละตัวพร้อมจำนวนครั้งที่พบ
print(count_characters)