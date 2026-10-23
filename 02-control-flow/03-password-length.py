# Input
password = input("กรุณาตั้ง Password:")

# Process & Output
count_characters = len(password) # นับตัวอักษรจาก Input

print(f"Enter password: {password}") # แสดงพาสเวิร์ดที่เลือก

# ใส่เงื่อนไข
if count_characters < 8:
    print('Too short')
elif count_characters <= 11:
    print('Acceptable length')
else:
    print('Good length')