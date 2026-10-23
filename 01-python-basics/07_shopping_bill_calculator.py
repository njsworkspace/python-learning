"""
แบบฝึกหัด: คำนวณยอดซื้อหลังหักส่วนลดและบวก VAT
จุดประสงค์: ฝึกรับข้อมูลหลายค่า คำนวณเปอร์เซ็นต์ และจัดลำดับขั้นตอน
โปรแกรมคำนวณราคารวม ส่วนลด ราคาหลังหักส่วนลด VAT และยอดสุทธิ
"""

# Input
# รับราคาสินค้าต่อชิ้นเป็นจำนวนเต็ม
product_price = int(input("ราคาสินค้าต่อชิ้น: "))
# รับจำนวนชิ้นที่ต้องการซื้อ
quantity = int(input("จำนวนสินค้า: "))

# ส่วนลดและ Vat (เป็นค่าคงที่จึงใช้ชื่อตัวแปรเป็นตัวใหญ่)
# รับเปอร์เซ็นต์ส่วนลด แล้วแปลงเป็นเลขทศนิยม
discount = float(input("ส่วนลด %: [เช่น 10] "))
# แปลงส่วนลดจากเปอร์เซ็นต์ เช่น 10 ให้เป็นอัตรา 0.10
discount = discount / 100

# รับเปอร์เซ็นต์ VAT แล้วแปลงเป็นเลขทศนิยม
vat = float(input("VAT %: [เช่น 7] "))
# แปลง VAT จากเปอร์เซ็นต์ เช่น 7 ให้เป็นอัตรา 0.07
vat = vat / 100

# Process
# คำนวณราคารวมก่อนหักส่วนลด
total_product_price = product_price * quantity
# คำนวณจำนวนเงินส่วนลดจากราคารวม
total_discount = total_product_price * discount
# หักส่วนลดออกจากราคารวม
total_price_after_discount = total_product_price - total_discount
# คำนวณ VAT จากราคาหลังหักส่วนลด
vat_amount = total_price_after_discount * vat
# บวก VAT เพื่อหายอดสุทธิที่ต้องจ่าย
net_price = total_price_after_discount + vat_amount


# Output
# แสดงราคาต่อชิ้น
print(f"Product price: ${product_price}")
# แสดงจำนวนสินค้าที่ซื้อ
print(f"Quantity: {quantity} pieces")
# แสดงอัตราส่วนลดในรูปเปอร์เซ็นต์
print(f"Discount: {discount:.0%}")
# แสดงอัตรา VAT ในรูปเปอร์เซ็นต์
print(f"VAT: {vat:.0%}")
# แสดงราคารวมก่อนหักส่วนลด โดยมีทศนิยม 2 ตำแหน่ง
print(f"\nSubtotal: ${total_product_price:.2f}")
# แสดงจำนวนเงินส่วนลด
print(f"Discount: ${total_discount:.2f}")
# แสดงราคาหลังหักส่วนลด
print(f"After discount: ${total_price_after_discount:.2f}")
# แสดงจำนวนเงิน VAT
print(f"VAT: ${vat_amount:.2f}")
# แสดงยอดสุทธิหลังหักส่วนลดและบวก VAT
print(f"Total: ${net_price:.2f}")