"""
Kata: How good are you really?
kyu: 8
URL: https://www.codewars.com/kata/5601409514fc93442500010b
Date: 2026-10-23
Concept: ตรวจว่าคะแนนสูงกว่าค่าเฉลี่ยหรือไม่
วิธีคิด: คำนวณค่าเฉลี่ยรวมคะแนนของตน แล้วเปรียบเทียบ
สิ่งที่เรียนรู้: `sum()`, `len()` และการเปรียบเทียบ
"""

def better_than_average(class_points, your_points):
    average_class_points = (sum(class_points) + your_points) / (len(class_points) + 1)
    if your_points > average_class_points:
        return True
    else:
        return False