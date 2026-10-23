"""
Kata: Counting sheep...
kyu: 8
URL: https://www.codewars.com/kata/54edbc7200b811e956000556
Date: 2026-10-23
Concept: นับจำนวนค่า `True` ในลิสต์
วิธีคิด: รวมค่า `1` สำหรับสมาชิกที่เป็นจริง
สิ่งที่เรียนรู้: generator expression และ `sum()`
"""

def count_sheeps(sheep):
    return sum(1 for s in sheep if s)
