"""
Kata: Remove First and Last Character
kyu: 8
URL: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
Date: 2026-10-23
Concept: ตัดตัวอักษรตัวแรกและตัวสุดท้าย
วิธีคิด: ใช้ slicing `s[1:-1]`
สิ่งที่เรียนรู้: slicing และ negative index
"""
def remove_char(s):
    return s[1:-1]