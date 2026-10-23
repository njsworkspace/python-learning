# ข้อความตัวอย่าง มีช่องว่างและเครื่องหมายวรรคตอนปะปนอยู่
fruits = " Banana, Apple! Orange. Grape: Banana? Apple Watermelon Strawberry. "

# ลบช่องว่างด้านหน้าและด้านหลัง
# แล้วเปลี่ยนตัวอักษรทั้งหมดให้เป็นตัวพิมพ์เล็ก
fruits = fruits.strip().lower()

# สร้าง dictionary ว่างไว้เก็บชื่อผลไม้และจำนวนครั้งที่พบ
# ตัวอย่าง: {"banana": 2, "apple": 2}
frequency = {}

# รายการเครื่องหมายที่ต้องการลบออกจากข้อความ
# เครื่องหมาย * เขียนได้ตรง ๆ ไม่ต้องใส่ backslash
punctuation = "!@#$%^&*?.,:"

# วนตรวจเครื่องหมายทีละตัว
for symbol in punctuation:
    # แทนที่เครื่องหมายนั้นด้วยข้อความว่าง
    # จึงเท่ากับลบเครื่องหมายนั้นออกจาก fruits
    fruits = fruits.replace(symbol, "")

# แยกข้อความออกเป็นคำ โดยใช้ช่องว่างเป็นตัวแบ่ง
# ผลลัพธ์จะเป็น list เช่น ["banana", "apple", "orange", ...]
fruit_list = fruits.split()

# วนดูผลไม้แต่ละคำใน list
for fruit in fruit_list:
    # ถ้าเคยนับผลไม้นี้แล้ว ให้เพิ่มจำนวนขึ้น 1
    if fruit in frequency:
        frequency[fruit] = frequency[fruit] + 1
    # ถ้าเพิ่งพบครั้งแรก ให้เริ่มนับที่ 1
    else:
        frequency[fruit] = 1

# แสดง dictionary ที่เก็บชื่อผลไม้และจำนวนครั้งที่พบ
print(frequency)