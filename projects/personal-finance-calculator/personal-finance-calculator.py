# Start: Financial Calculator

# Input: User's financial data
income_amount = float(input("Enter your monthly income: "))
food_expenses = float(input("Enter your monthly food expenses: "))
rent_expenses = float(input("Enter your monthly rent expenses: "))
utilities_expenses = float(input("Enter your monthly utilities expenses: "))
transportation_expenses = float(input("Enter your monthly transportation expenses: "))
savings = float(input("Enter your monthly savings: "))

# Process: Calculate financial metrics
total_expenses = food_expenses + rent_expenses + utilities_expenses + transportation_expenses
net_income = income_amount - total_expenses - savings
food_rate = (food_expenses / income_amount)
rent_rate = (rent_expenses / income_amount)
utilities_rate = (utilities_expenses / income_amount)
transportation_rate = (transportation_expenses / income_amount)
savings_rate = (savings / income_amount)

# Output: Display financial metrics and recommendations
print("\nFinancial Summary:")
print(f"Total income: ${income_amount:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")
print(f"Net income after expenses and savings: ${net_income:.2f}")
print(f"Food expenses rate: {food_rate:.2%}")
print(f"Rent expenses rate: {rent_rate:.2%}")
print(f"Utilities expenses rate: {utilities_rate:.2%}")
print(f"Transportation expenses rate: {transportation_rate:.2%}")
print(f"Savings rate: {savings_rate:.2%}")

# End: Financial Calculator