import math

x1,y1 = map(float,input("Enter coordinate 1 (x,y): ").split())
x2,y2 = map(float,input("Enter coordinate 2 (x,y): ").split())

distance = format(math.sqrt(pow(x2-x1,2) + pow(y2-y1,2)),".2f")

print(f"Distanece between this two locations is {distance}")