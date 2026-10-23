"""
Kata: Abbreviate a Two Word Name
kyu: 8
URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
date: 2026-10-23
concept: String methods (`upper()`, `split()`), Indexing, f-string
วิธีคิด: แปลงชื่อเป็นตัวพิมพ์ใหญ่ → แยกชื่อและนามสกุลด้วย `split()` → ดึงตัวอักษรแรกของแต่ละคำด้วย `[0]` → เชื่อมด้วย `.` 
สิ่งที่เรียนรู้: การจัดการ string ด้วย method และการเข้าถึงตัวอักษรด้วย indexing
"""

def abbrev_name(name):
    name = name.upper().split()
    return f"{name[0][0]}.{name[1][0]}"
