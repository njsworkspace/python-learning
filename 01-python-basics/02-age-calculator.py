# รับปีเกิดจากผู้ใช้แล้วแปลงข้อความที่กรอกให้เป็นจำนวนเต็ม
birth_year = int(input("Enter your birth year: "))
# กำหนดปีปัจจุบันที่ใช้เป็นฐานในการคำนวณ
current_year = 2026

# หักปีเกิดออกจากปีปัจจุบันเพื่อหาอายุโดยประมาณ
age = current_year - birth_year
# แสดงอายุที่คำนวณได้
print("You are", age, "years old.")