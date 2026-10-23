numbers = [1, 2, 3, 4, 5]
if not numbers:
    highest = "List is empty"
else:
    highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number


print(f"Maximux value: {highest}")