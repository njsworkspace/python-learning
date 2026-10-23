"""
Kata: Grasshopper - Summation
kyu: 8
URL: https://www.codewars.com/kata/55d24f55d7dd296eb9000030
Date: 2026-10-23
Concept: สร้างฟังก์ชันที่รับค่าตัวเลข num และคืนค่าผลรวมของตัวเลขทั้งหมดตั้งแต่ 1 ถึง num
วิธีคิด: ใช้ฟังก์ชัน sum() และ range() เพื่อคำนวณผลรวมของตัวเลขตั้งแต่ 1 ถึง num
สิ่งที่เรียนรู้: ได้เรียนรู้การใช้ฟังก์ชัน sum() และ range() ใน Python เพื่อคำนวณผลรวมของตัวเลข
"""

def summation(num):
    return sum(range(num + 1))
