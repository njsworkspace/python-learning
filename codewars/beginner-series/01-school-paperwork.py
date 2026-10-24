"""
Kata: Beginner Series #1 School Paperwork
kyu: 8
URL: https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
date: 2026-10-23
Concept: ตรวจค่าติดลบและคูณตัวเลข
วิธีคิด: ถ้ามีค่าติดลบคืน `0`; มิฉะนั้นคืนผลคูณ
สิ่งที่เรียนรู้: เงื่อนไข `if` และการคูณ
"""

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m