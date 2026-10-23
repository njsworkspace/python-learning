"""
Kata: Abbreviate a Two Word Name
kyu: 8
URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
date: 2026-10-23
Concept: การจัดการข้อความและเข้าถึงตัวอักษร
วิธีคิด: แยกคำ แล้วนำอักษรแรกมาเชื่อมด้วยจุด
สิ่งที่เรียนรู้: `upper()`, `split()` และ indexing
"""

def abbrev_name(name):
    name = name.upper().split()
    return f"{name[0][0]}.{name[1][0]}"
