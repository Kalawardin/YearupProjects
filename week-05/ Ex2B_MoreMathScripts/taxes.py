

salary = int(input("Enter your salary:"))
tax_rate = int(salary / 100) * 23
actual_profit = int(salary - tax_rate)
print(f"Your total tax is {tax_rate}. Your actual earnings is {actual_profit}")