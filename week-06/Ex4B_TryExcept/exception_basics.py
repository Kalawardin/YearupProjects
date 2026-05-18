
try:
    
    value = int("TradeBoat")
except ValueError:
    print("ValueError: Oops, looks like you tried to convert a non-numeric string to an integer.")
else:
    print("Success: No ValueError occurred.")
finally:
    print("Let's try another one...\n")


try:
    print(undefined_pc_hardware)
except NameError:
    print("NameError: Oops, looks like you tried to use an undefined variable.")
else:
    print("Success: No NameError occurred.")
finally:
    print("Let's try another one...\n")


try:
    result = "Route " + 66
except TypeError:
    print("TypeError: Oops, you cannot concatenate a string and an integer directly.")
else:
    print("Success: No TypeError occurred.")
finally:
    print("Let's try another one...\n")


try:
    eval("print('Hello World)")
except SyntaxError:
    print("SyntaxError: Oops, invalid syntax detected (like a missing quote).")
else:
    print("Success: No SyntaxError occurred.")
finally:
    print("Let's try another one...\n")