"""
Kata: Reversed Sequence
kyu: 8
URL: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
Date: 2026-10-23
Concept: สร้างลิสต์ของตัวเลขในลำดับย้อนกลับจาก n ถึง 1
วิธีคิด: ใช้ range() เพื่อสร้างลิสต์ของตัวเลขและใช้ reversed
สิ่งที่เรียนรู้: การใช้ range() และ reversed() ใน Python เพื่อสร้างลิสต์ของตัวเลขในลำดับย้อนกลับ
"""

def reverse_seq(n):
    return list(reversed(range(1, n + 1)))