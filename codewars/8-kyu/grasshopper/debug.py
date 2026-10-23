"""
Kata: Grasshopper - Debug
kyu: 8
URL: https://www.codewars.com/kata/55cb854deb36f11f130000e1/
Date: 2026-10-23
Concept: สร้าง function ที่รับอุณหภูมิเป็นองศาฟาเรนไฮต์และแปลงเป็นองศาเซลเซียสและฟ function บอกสภาพอากาศตามอุณหภูมิที่แปลงแล้ว
วิธีคิด: ใช้สูตรการแปลงอุณหภูมิจากฟาเรนไฮต์เป็นเซลเซียส และใช้เงื่อนไข if-elif-else เพื่อตรวจสอบสภาพอากาศตามอุณหภูมิที่แปลงแล้ว
สิ่งที่เรียนรู้: ได้เรียนรู้การใช้สูตรการแปลง
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