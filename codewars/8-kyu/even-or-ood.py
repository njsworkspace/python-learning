"""
Kata: Even or Odd
kyu: 8
URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
Date: 2026-10-23
Concept: ให้ฟังก์ชันตรวจสอบว่าตัวเลขที่กำหนดเป็นเลขคู่หรือเลขคี่
วิธีคิด: ใช้ตัวดำเนินการโมดูลัส (%) เพื่อตรวจสอบว่าตัวเลขหารด้วย 2 ลงตัวหรือไม่
สิ่งที่เรียนรู้: การใช้ตัวดำเนินการโมดูลัส (%) ใน Python เพื่อตรวจสอบความเป็นเลขคู่หรือเลขคี่
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"