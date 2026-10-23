"""
Kata: Returning Strings
kyu: 8
URL: https://www.codewars.com/kata/55a70521798b14d4750000a4
Date: 2026-10-23
Concept: การสร้างและคืนค่า string จาก function โดยใช้ parameter ที่รับเข้ามา
วิธีคิด: รับค่า name ผ่าน parameter แล้วใช้ f-string เพื่อแทรกค่าของ name ลงในข้อความทักทายตามรูปแบบที่โจทย์กำหนด จากนั้นใช้ return ส่งข้อความกลับไป
สิ่งที่เรียนรู้:
 - การรับค่า parameter ใน function
 - การใช้ f-string (f"...") เพื่อแทรกค่าตัวแปรใน string
 - การใช้ return เพื่อส่งค่ากลับจาก function
"""
def greet(name):
    return f"Hello, {name} how are you doing today?"