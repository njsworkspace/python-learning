"""
Kata: Grasshopper - Debug
kyu: 8
URL: https://www.codewars.com/kata/55cb854deb36f11f130000e1/
Date: 2026-10-23
Concept: แปลงฟาเรนไฮต์เป็นเซลเซียสและบอกจุดเยือกแข็ง
วิธีคิด: ใช้สูตรแปลงอุณหภูมิ แล้วตรวจว่าเกิน `0°C` หรือไม่
สิ่งที่เรียนรู้: สูตรคำนวณและเงื่อนไข `if` / `else`
"""

def weather_info(temp):
    c = convert_to_celsius(temp)
    if c > 0:
        return str(c) + " is above freezing temperature"
    else:
        return str(c) + " is freezing temperature"


def convert_to_celsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius