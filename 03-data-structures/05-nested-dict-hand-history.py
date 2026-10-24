# เก็บข้อมูลของ poker hand
hand = {
    "hand_id": "NL001",
    "players": {
        "hero": {
            "position": "BTN",
            "stack": 100,
            "cards": ["As", "Kd"],
        },
        "villain": {
            "position": "BB",
            "stack": 80,
            "cards": ["7h", "7d"],
        },
    },
    "board": ["Ah", "9c", "4d", "Js", "2h"],
}

# สร้างลิสต์ข้อมูลผู้เล่น โดยดึงค่าจาก dictionary "players"
players_list = list(hand["players"].values())

# แสดงตำแหน่งของผู้เล่นแต่ละคน
print(players_list[0]["position"])
print(players_list[1]["position"])

# แสดงไพ่ใบที่สองของผู้เล่นคนแรก
print(players_list[0]["cards"][1])

# แสดงไพ่สามใบแรกบนบอร์ด
print(hand["board"][:3])

# ตรวจสอบว่ามีผู้เล่นชื่อ "hero" อยู่ในข้อมูลหรือไม่
print("hero" in hand["players"])

# รวม stack ของผู้เล่นทุกคน
total_stack = 0

for player_data in hand["players"].values():
    total_stack += player_data["stack"]

# แสดง stack รวม
print(total_stack)