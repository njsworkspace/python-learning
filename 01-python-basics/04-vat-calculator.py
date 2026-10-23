VAT = 0.07
price = float(input("Enter the price of the item: "))

total_price = price + (price * VAT)

print(f"The total price including VAT is: {total_price:.2f} dollars")