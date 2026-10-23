# Input
score = int(input("Enter Score: "))

# Process & Output
print(f"Score: {score}")

if score > 100 or score < 0:
    print('Invalid score')
elif score >= 80:
    print('Grade: A')
elif score >= 70:
    print('Grade: B')
elif score >= 60:
    print('Grade: C')
elif score >= 50:
    print('Grade: D')
else:
    print('Grade: F')

