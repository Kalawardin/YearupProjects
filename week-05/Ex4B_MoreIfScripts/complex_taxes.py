pay_rate = float(input("Enter pay rate per hour: "))
hours_worked = float(input("How many hours did you work?: "))
marial_status = input("What is your marial status? (Married or Joint):")



if hours_worked > 40:
   overtime_hours = hours_worked - 40
   regular_pay = pay_rate * 40
   overtime_pay = (pay_rate * 1.5) * overtime_hours
   weekly_pay = regular_pay + overtime_pay
else:
    weekly_pay = pay_rate * hours_worked

annual_pay = weekly_pay * 52

if marial_status == "Joint":
    if annual_pay < 12000: 
        tax_rate = 0.05
    elif annual_pay < 24999.99 and annual_pay > 12000:
        tax_rate = 0.10
    elif annual_pay < 74999.99 and annual_pay > 25000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif marial_status == "Married":
    if annual_pay < 12000:
        tax_rate = 0
    elif annual_pay < 24999.99 and annual_pay > 12000:
        tax_rate = 0.06
    elif annual_pay < 74999.99 and annual_pay > 25000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print("Invalid input. Please restart and enter Married or Joint.")
    exit

weekly_tax = weekly_pay * tax_rate
net_pay = weekly_pay - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn {pay_rate} per hour, your gross weekly pay is ${weekly_pay}")
print(f"Your filing status is {marial_status}")
print(f"Your tax withholding for the week is ${weekly_tax}")
print(f"Your net pay is ${net_pay}")

