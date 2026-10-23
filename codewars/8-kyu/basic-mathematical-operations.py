"""
Kate: Basic Mathematical Operations
kyu: 8
URL: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
Date: 2026-10-23
Concept: เลือกการคำนวณด้วย conditional statements ตาม operator ที่รับเข้ามา
วิธีคิด: ตรวจสอบค่า operator ด้วย if / elif / else แล้วคืนผลการคำนวณที่ตรงกัน
สิ่งที่เรียนรู้:
 - == ใช้เปรียบเทียบค่าที่เท่ากัน
 - if / elif / else ใช้เลือกทำงานตามเงื่อนไข
 - เครื่องหมาย '+' เป็น string แต่เราใช้มันเป็นเงื่อนไขเพื่อเลือกให้ Python ทำการบวกจริง ๆ ได้
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