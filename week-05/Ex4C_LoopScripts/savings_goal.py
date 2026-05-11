balance = 500
goal = 2000
weekly_savings = 150

while balance < goal:
    balance = balance + weekly_savings 
    print(f"This week my balance increased to {balance} ")
    
print(f"Goal met! My current balance is {balance}")