"""
Kata: Remove First and Last Character
kyu: 8
URL: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
Date: 2026-10-23
Concept: การตัดตัวอักษรตัวแรกและตัวสุดท้ายออกจาก string
วิธีคิด: วิธีคิด: ใช้ string slicing ด้วย s[1:-1] โดยเริ่มจาก index 1 (ตัวอักษรตัวที่ 2) และหยุดก่อน index -1 (ตัวอักษรตัวสุดท้าย)
สิ่งที่เรียนรู้:
 -การใช้ string slicing [start:stop]
 -การใช้ negative index เช่น -1
 -ตำแหน่ง stop ใน slicing จะไม่ถูกรวมในผลลัพธ์
"""
def remove_char(s):
    return s[1:-1]