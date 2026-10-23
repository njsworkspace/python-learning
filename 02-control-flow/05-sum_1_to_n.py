number = int(input("Enter number: "))

print(f"Enter number: {number}")

total = 0
# คำนวณผลรวมโดยใช้ลูป
for i in range(1, number + 1):
    total += i
    print(f"Total: {total}")