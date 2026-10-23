"""
Kata: Even or Odd
kyu: 8
URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
Date: 2026-10-23
Concept: ตรวจว่าเลขเป็นคู่หรือคี่
วิธีคิด: ตรวจเศษจากการหารด้วย `2`
สิ่งที่เรียนรู้: การใช้ modulo (`%`)
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"