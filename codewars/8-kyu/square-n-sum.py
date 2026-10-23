"""
Kata: Square(n) Sum
kyu: 8
URL: https://www.codewars.com/kata/515e271a311df0350d00000f
Date: 2026-10-23
Concept: หาผลรวมกำลังสองของตัวเลขในลิสต์
วิธีคิด: ยกกำลังสองแต่ละค่าแล้วรวมด้วย `sum()`
สิ่งที่เรียนรู้: generator expression และ `sum()`
"""

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)