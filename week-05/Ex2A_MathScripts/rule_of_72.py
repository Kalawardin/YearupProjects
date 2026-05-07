savings = float(input("Enter your current saving: "))
interest_rate = float(input("Enter interest rate: "))
years = float(format(72 / interest_rate , ".2f"))
total = (((savings / 100) * interest_rate) * years) + savings


print(f"Your current savings is {total}.")
print(f"At a {interest_rate}% interest rate, your savings account will be worth {total} in {years} years.")

