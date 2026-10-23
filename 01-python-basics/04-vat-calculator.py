# เก็บอัตรา VAT 7% ในรูปทศนิยมเพื่อใช้คำนวณ
VAT = 0.07
# รับราคาสินค้าและแปลงเป็นเลขทศนิยม
price = float(input("Enter the price of the item: "))

# บวกภาษีเข้าไปในราคาสินค้าเพื่อหายอดรวม
total_price = price + (price * VAT)

# แสดงราคารวมโดยจัดรูปแบบทศนิยม 2 ตำแหน่ง
print(f"The total price including VAT is: {total_price:.2f} dollars")