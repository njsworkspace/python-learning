"""
Kata: if you can't sleep, just count sheep!!
kyu: 8
URL: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
Date: 2026-10-23
Concept: สร้างสตริงที่นับจำนวนแกะตามจำนวนที่กำหนด
วิธีคิด: ใช้ list comprehension เพื่อสร้างลิสต์ของสตริงและ join เพื่อรวมสตริงเหล่านั้นเข้าด้วยกัน
สิ่งที่เรียนรู้: การใช้ list comprehension และ join() ใน Python เพื่อสร้างสตริงที่นับจำนวนแกะ
"""

def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n + 1))