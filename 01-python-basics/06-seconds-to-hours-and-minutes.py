seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60


print(f"{seconds} seconds is equal to {hours} hours and {minutes} minutes.")