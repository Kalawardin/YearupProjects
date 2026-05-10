a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b > c:
    print(f"Biggest: {a}\nSmallest: {c}")
elif a > c > b:
    print(f"Biggest: {a}\nSmallest: {b}")
elif b > a > c:
    print(f"Biggest: {b}\nSmallest: {c}")
elif b > c > a:
    print(f"Biggest: {b}\nSmallest: {a}")
elif c > a > b:
    print(f"Biggest: {c}\nSmallest: {b}")
elif c > b > a:
    print(f"Biggest: {c}\nSmallest: {a}")