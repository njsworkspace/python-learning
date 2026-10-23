# Input
product_price = int(input("ราคาสินค้าต่อชิ้น: "))
quantity = int(input("จำนวนสินค้า: "))

# ส่วนลดและ Vat (เป็นค่าคงที่จึงใช้ชื่อตัวแปรเป็นตัวใหญ่)
discount = float(input("ส่วนลด %: [เช่น 10] "))
discount = discount / 100

vat = float(input("VAT %: [เช่น 7] "))
vat = vat / 100

# Process
total_product_price = product_price * quantity
total_discount = total_product_price * discount
total_price_after_discount = total_product_price - total_discount
vat_amount = total_price_after_discount * vat
net_price = total_price_after_discount + vat_amount


# Output
print(f"Product price: ${product_price}")
print(f"Quantity: {quantity} pieces")
print(f"Discount: {discount:.0%}")
print(f"VAT: {vat:.0%}")
print(f"\nSubtotal: ${total_product_price:.2f}")
print(f"Discount: ${total_discount:.2f}")
print(f"After discount: ${total_price_after_discount:.2f}")
print(f"VAT: ${vat_amount:.2f}")
print(f"Total: ${net_price:.2f}")