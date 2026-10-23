"""
Kata: Reversed Sequence
kyu: 8
URL: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
Date: 2026-10-23
Concept: สร้างลำดับตัวเลขย้อนจาก `n` ถึง `1`
วิธีคิด: สร้างช่วงตัวเลขแล้วใช้ `reversed()`
สิ่งที่เรียนรู้: `range()` และ `reversed()`
"""

def reverse_seq(n):
    return list(reversed(range(1, n + 1)))