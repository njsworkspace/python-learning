"""
Kata: Basic Mathematical Operations
kyu: 8
URL: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
Date: 2026-10-23
Concept: เลือกการคำนวณตามเครื่องหมายที่รับมา
วิธีคิด: ใช้ `if` / `elif` ตรวจเครื่องหมาย แล้วคืนผลลัพธ์
สิ่งที่เรียนรู้: การเปรียบเทียบ string ด้วย `==` และเลือกทำงานด้วยเงื่อนไข
"""

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 / value2