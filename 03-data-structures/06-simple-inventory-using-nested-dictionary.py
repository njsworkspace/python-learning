# เก็บราคาและจำนวนสินค้าคงเหลือในคลัง
inventory = {
    "apple": {"price": 20, "qty": 10},
    "banana": {"price": 5, "qty": 30},
}

# ปรับจำนวนแอปเปิลคงเหลือเป็น 8 ชิ้น
inventory["apple"]["qty"] = 8

# เพิ่มส้มเข้าในคลัง
inventory["orange"] = {"price": 15, "qty": 12}

# ลดจำนวนกล้วยลง 5 ชิ้น
inventory["banana"]["qty"] -= 5

# คำนวณมูลค่าสินค้าทั้งหมดในคลัง
total = 0

for product, info in inventory.items():
    total += info["price"] * info["qty"]

# แสดงมูลค่าสินค้ารวมและข้อมูลของกล้วย
print(total)
print(inventory["banana"])

# ตรวจสอบว่ามะม่วงมีอยู่ในคลังหรือไม่
if "mango" in inventory:
    print(inventory["mango"]["qty"])
else:
    print("out of stock")


# ขายสินค้าโดยตรวจสอบชื่อสินค้าและจำนวนคงเหลือก่อน
def sell(inventory, name, amount):
    if name not in inventory:
        print("not found")
    elif inventory[name]["qty"] < amount:
        print("not enough stock")
    else:
        # หักจำนวนสินค้าที่ขายออกจากคลัง
        inventory[name]["qty"] -= amount


# ขายแอปเปิล 3 ชิ้น แล้วแสดงจำนวนคงเหลือ
sell(inventory, "apple", 3)
print(inventory["apple"]["qty"])

# ทดลองขายเกินจำนวนที่มี และขายสินค้าที่ไม่มีในคลัง
sell(inventory, "apple", 100)
sell(inventory, "mango", 1)