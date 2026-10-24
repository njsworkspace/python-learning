# เก็บจำนวนมือที่เล่นและจำนวนมือที่ชนะ แยกตามตำแหน่ง
stats = {
    "BTN": {"hands": 2, "won": 12},
    "SB": {"hands": 80, "won": 5},
}

# เพิ่มจำนวนมือที่เล่นและมือที่ชนะของตำแหน่ง BTN อย่างละ 1
stats["BTN"]["hands"] += 1
stats["BTN"]["won"] += 1

# ตรวจสอบข้อมูลและคำนวณอัตราการชนะของแต่ละตำแหน่ง
for position, info in stats.items():
    if info["won"] > info["hands"]:
        # จำนวนมือที่ชนะต้องไม่มากกว่าจำนวนมือที่เล่น
        print(f"data error: {position}")
    elif info["hands"] > 0:
        winrate = info["won"] / info["hands"]
        print(f"Pos.: {position} - Win Rate: {winrate:.2%}")
    else:
        print("ไปเล่นให้มือมากกว่า 0 ไป๊!")