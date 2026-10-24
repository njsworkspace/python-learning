"""
Kata: Complementary DNA
kyu: 7
URL: https://www.codewars.com/kata/554e4a2f232cdd87d9000038
date: 2026-10-24
Concept: เบส DNA จับคู่กันเป็นคู่เสริม: `A ↔ T` และ `C ↔ G`
วิธีคิด: วนดูตัวอักษรทีละตัว แทนแต่ละตัวด้วยเบสคู่สม แล้วนำผลลัพธ์มาต่อกันเป็นสตริง
สิ่งที่เรียนรู้: การใช้เงื่อนไขเลือกค่าที่ต้องแทน และการสะสมผลลัพธ์ในลิสต์ก่อนใช้ `"".join()` รวมเป็นสตริง
"""

def DNA_strand(dna):
    dna_symbols = []

    for i in dna:
        # แทนเบสแต่ละตัวด้วยเบสคู่สม
        if "A" in i:
            dna_symbols.append("T")
        elif "T" in i:
            dna_symbols.append("A")
        elif "C" in i:
            dna_symbols.append("G")
        else:
            dna_symbols.append("C")  # เบสที่เหลือคือ G

    # รวมเบสที่จับคู่แล้วให้เป็นสตริง
    return "".join(dna_symbols)


dna = "GTAT"
print(DNA_strand(dna))