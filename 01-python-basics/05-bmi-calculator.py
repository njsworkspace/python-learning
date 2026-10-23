# รับน้ำหนักเป็นกิโลกรัมและแปลงเป็นเลขทศนิยม
weight = float(input("Enter your weight in kilograms: "))
# รับส่วนสูงเป็นเมตรและแปลงเป็นเลขทศนิยม
height = float(input("Enter your height in meters: "))

# คำนวณ BMI ด้วยน้ำหนักหารด้วยส่วนสูงยกกำลังสอง
bmi = weight / (height ** 2)

# แสดงค่า BMI โดยปัดรูปแบบให้มีทศนิยม 2 ตำแหน่ง
print(f"Your BMI is: {bmi:.2f}")