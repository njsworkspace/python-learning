# รับอุณหภูมิหน่วยเซลเซียสและแปลงเป็นเลขทศนิยม
celsius = float(input("Enter temperature in Celsius: "))

# ใช้สูตรแปลงเซลเซียสเป็นฟาเรนไฮต์แล้วเก็บผลไว้
fahrenheit = (celsius * 9/5) + 32

# แสดงอุณหภูมิทั้งสองหน่วยด้วย f-string
print(f"{celsius}°C is equal to {fahrenheit}°F")