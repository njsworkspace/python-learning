"""
Kata: a needle in the haystack
kyu: 8
URL: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/
date: 2026-10-23
conept: หาตำแหน่งของค่าหนึ่งในลิสต์
วิธีคิด: ใช้การตรวจสอบค่าด้วย in operator และ index() method
สิ่งที่เรียนรู้: ได้เรียนรู้การใช้ in operator และ index() method ใน Python
"""

def find_needle(haystack):
    if "needle" in haystack:
        return f"found the needle at position {haystack.index('needle')}"
    else:
        return "needle not found"