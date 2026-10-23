"""
Kata: a needle in the haystack
kyu: 8
URL: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/
date: 2026-10-23
Concept: ค้นหาตำแหน่งของค่าในลิสต์
วิธีคิด: ใช้ `in` ตรวจสอบ แล้วใช้ `index()` หาตำแหน่ง
สิ่งที่เรียนรู้: การค้นหาข้อมูลในลิสต์
"""

def find_needle(haystack):
    if "needle" in haystack:
        return f"found the needle at position {haystack.index('needle')}"
    else:
        return "needle not found"