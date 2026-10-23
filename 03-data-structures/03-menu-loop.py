# วนรับคำสั่งไปเรื่อย ๆ จนกว่าผู้ใช้จะพิมพ์ Stop
while True:
    # รับคำสั่งจากผู้ใช้
    # lower() ทำให้ตัวอักษรเป็นตัวพิมพ์เล็ก
    # strip() ลบช่องว่างที่อยู่หัวและท้ายข้อความ
    choice = input("Enter command: ['Hi', 'Count', 'Sum', 'Stop'] ")
    choice = choice.lower().strip()

    # คำสั่ง Hi: แสดงข้อความทักทาย
    if choice == "hi":
        print("Hello World!")

    # คำสั่ง Count: นับถอยหลังจากตัวเลขที่ผู้ใช้ระบุจนถึง 1
    elif choice == "count":
        try:
            # แปลงข้อความที่รับมาให้เป็นจำนวนเต็ม
            count_number = int(input("Enter your number: "))

            # ตรวจสอบว่าตัวเลขเป็นบวกหรือไม่
            if count_number > 0:
                # range(ค่าเริ่มต้น, ค่าสุดท้าย, ระยะห่าง)
                # ใส่ -1 เพื่อให้ตัวเลขลดลงทีละ 1
                # ค่า 0 จะไม่ถูกรวมในผลลัพธ์
                for number in range(count_number, 0, -1):
                    print(number)
            else:
                print("Please enter a positive value!")

        # ทำงานส่วนนี้เมื่อผู้ใช้ป้อนสิ่งที่แปลงเป็นจำนวนเต็มไม่ได้
        except ValueError:
            print("Please enter a valid integer!")

    # คำสั่ง Sum: หาผลรวมตั้งแต่ 1 ถึงตัวเลขที่ผู้ใช้ระบุ
    elif choice == "sum":
        try:
            number = int(input("Enter number: "))

            # ตรวจสอบว่าตัวเลขเป็นบวกหรือไม่
            if number > 0:
                total = 0

                # บวกตัวเลขตั้งแต่ 1 ถึง number เข้ากับ total ทีละรอบ
                # ต้องใช้ number + 1 เพราะค่าท้ายสุดของ range จะไม่ถูกรวม
                for i in range(1, number + 1):
                    total = total + i

                print(total)
            else:
                print("Please enter a positive value!")

        # ทำงานส่วนนี้เมื่อผู้ใช้ป้อนสิ่งที่แปลงเป็นจำนวนเต็มไม่ได้
        except ValueError:
            print("Please enter a valid integer!")

    # คำสั่ง Stop: แสดงข้อความลา แล้วออกจาก while
    elif choice == "stop":
        print("Goodbye!")
        break

    # กรณีที่พิมพ์คำสั่งอื่นที่ไม่มีในรายการ
    else:
        print("Try again!")