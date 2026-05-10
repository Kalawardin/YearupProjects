pay_rate = float(input("Enter pay rate per hour: "))
hours_worked = float(input("How many hours did you work?: "))

if hours_worked > 40:
   overtime_hours = hours_worked - 40
   regular_pay = pay_rate * 40
   overtime_pay = (pay_rate * 1.5) * overtime_hours
   total_pay = regular_pay + overtime_pay
   print(total_pay)
else:
    weekly_pay = pay_rate * hours_worked
    print(weekly_pay)
   
    
    