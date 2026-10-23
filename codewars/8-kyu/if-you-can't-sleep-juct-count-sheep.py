"""
Kata: if you can't sleep, just count sheep!!
kyu: 8
URL: https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
Date: 2026-10-23
Concept: สร้างข้อความนับแกะตามจำนวนที่กำหนด
วิธีคิด: สร้างข้อความแต่ละลำดับ แล้วรวมด้วย `join()`
สิ่งที่เรียนรู้: generator expression และ `join()`
"""

def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n + 1))