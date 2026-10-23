"""
Kata: Rock Paper Scissors
kyu: 8
URL: https://www.codewars.com/kata/5672a98bdbdd995fad00000f
Date: 2026-10-23
Concept: เกมเป่ายิ้งฉุบระหว่างผู้เล่นสองคน โดยผู้เล่นแต่ละคนเลือก "rock", "paper" หรือ "scissors" และผลลัพธ์จะถูกตัดสินตามกฎของเกม
วิธีคิด: ใช้เงื่อนไข if-elif-else เพื่อตรวจสอบผลลัพธ์ของเกม
สิ่งที่เรียนรู้: การใช้เงื่อนไขและการเปรียบเทียบค่าของตัวแปร
"""

def rps(p1, p2):

    p1 = p1.lower()
    p2 = p2.lower()

    # กรณีที่ผู้เล่นทั้งสองเลือกเหมือนกัน
    if p1 == p2:
        return "Draw!"

    # กรณีที่ผู้เล่น 1 ชนะ
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "scissors" and p2 == "paper") or \
         (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"

    # กรณีที่ผู้เล่น 2 ชนะ
    else:
        return "Player 2 won!"