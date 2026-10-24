"""
Kata: Grasshopper - Grade book
kyu: 8
URL: https://www.codewars.com/kata/55cbd4ba903825f7970000f5
date: 2026-10-24
concept: คำนวณคะแนนเฉลี่ยจากคะแนน 3 วิชา แล้วจัดเกรดตามช่วงคะแนน
วิธีคิด: นำคะแนนทั้งสามมาบวกกันและหารด้วย 3 จากนั้นตรวจค่าเฉลี่ยว่าอยู่ในช่วงใด แล้วคืนเกรดที่ตรงกัน
สิ่งที่เรียนรู้: การคำนวณค่าเฉลี่ย และการใช้เงื่อนไข `if` / `elif` / `else` เพื่อตรวจช่วงคะแนน
"""

def get_grade(s1, s2, s3):
    # หาคะแนนเฉลี่ยของทั้งสามวิชา
    avg_score = (s1 + s2 + s3) / 3

    # ตรวจคะแนนเฉลี่ยและคืนเกรดตามช่วงคะแนน
    if 90 <= avg_score <= 100:
        return "A"
    elif 80 <= avg_score < 90:
        return "B"
    elif 70 <= avg_score < 80:
        return "C"
    elif 60 <= avg_score < 70:
        return "D"
    else:
        return "F"


s1 = 90
s2 = 90
s3 = 90

print(get_grade(s1, s2, s3))
    

    