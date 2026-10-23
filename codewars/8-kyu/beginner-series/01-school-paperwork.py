"""
Kata: Beginner Series #1 School Paperwork
kyu: 8
URL: https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
date: 2026-10-23
concept: Conditional, comparison operators, multiplication
วิธีคิด: ตรวจสอบว่า n หรือ m ติดลบหรือไม่ ถ้าติดลบคืนค่า 0 มิฉะนั้นคืนค่า n * m
สิ่งที่เรียนรู้: การใช้ if เพื่อตรวจสอบเงื่อนไข และใช้ * คำนวณจำนวนหน้ากระดาษทั้งหมด
"""

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m