"""
Kata: How good are you really?
kyu: 8
URL: https://www.codewars.com/kata/5601409514fc93442500010b
Date: 2026-10-23
Concept: การตรวจสอบว่าคะแนนของคุณสูงกว่าค่าเฉลี่ยของคะแนนของคลาสหรือไม่
วิธีคิด: คำนวณค่าเฉลี่ยของคะแนนของคลาสรวมกับคะแนนของคุณ จากนั้นเปรียบเทียบคะแนนของคุณกับค่าเฉลี่ยนั้น
สิ่งที่เรียนรู้: การใช้ฟังก์ชัน sum() และ len() ใน Python เพื่อคำนวณค่าเฉลี่ย และการใช้ if statement เพื่อเปรียบเทียบค่าต่าง ๆ
"""

def better_than_average(class_points, your_points):
    average_class_points = (sum(class_points) + your_points) / (len(class_points) + 1)
    if your_points > average_class_points:
        return True
    else:
        return False