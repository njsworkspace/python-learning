"""
Kata: Square(n) Sum
kyu: 8
URL: https://www.codewars.com/kata/515e271a311df0350d00000f
Date: 2026-10-23
Concept: การหาผลรวมของกำลังสองของตัวเลขในลิสต์
วิธีคิด: ใช้ list comprehension เพื่อสร้างลิสต์ของกำลังสองของตัวเลขในลิสต์ จากนั้นใช้ฟังก์ชัน sum() เพื่อหาผลรวมของลิสต์นั้น
สิ่งที่เรียนรู้: การใช้ list comprehension และฟังก์ชัน sum() ใน Python เพื่อหาผลรวมของกำลังสองของตัวเลข
"""

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)