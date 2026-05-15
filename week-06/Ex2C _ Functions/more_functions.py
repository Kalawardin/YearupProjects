def display_mailing_label(name,address,city,state,zip):
    return f"{name}\n{address}\n{city}, {state} ,{zip}"

def add_numbers(*numbers):
    result = sum(numbers)
    formula = ""
    for n in numbers:
        formula =formula + str(n) + " + "
    
    formula = formula[:-3]
    
    print(f"{formula} = {result}\n")

def display_receipt(total_due,amount_paid):
    if total_due > amount_paid:
        print(f"Total Due: ${total_due}\nAmount Paid: ${amount_paid}\n")
        print(f"Remaining Balance {total_due - amount_paid}")
    else:
        print(f"Total Due: ${total_due}\nAmount Paid: ${amount_paid}\n")
        print(f"Change Due{total_due - amount_paid}")
        
print(display_mailing_label("\nAda Lovelace", "3519 N Elston Ave", "Chicago", "IL", "60618"))
print()
print(display_mailing_label("Grace Hopper", "456 Innovation Way", "Seattle", "WA", "98101"))

add_numbers(42)
add_numbers(15, 25)
add_numbers(10, 20, 30, 40, 50)

   

display_receipt(50.00, 75.00)
display_receipt(120.50, 120.50)
display_receipt(200.00, 80.00)

  
        
    