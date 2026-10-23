"""
Kate: Counting sheep...
kyu: 8
URL: https://www.codewars.com/kata/54edbc7200b811e956000556
Date: 2026-10-23
Concept: ได้รับจำนวนแกะที่อยู่ในลิสต์โดยนับค่าที่เป็น True
วิธีคิด: คำนวณจำนวนแกะที่อยู่ในลิสต์โดยใช้การวนลูปและนับค่าที่เป็น True
สิ่งที่เรียนรู้: การใช้ list comprehension และฟังก์ชัน sum() ใน Python เพื่อคำนวณจำนวนค่าที่เป็น True ในลิสต์
"""

def count_sheeps(sheep):
    return sum(1 for s in sheep if s)
