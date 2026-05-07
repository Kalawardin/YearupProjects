l,w = map(float,input("Enter room size(length and width): ").split())
area = float(l*w)
tile_boxes = format(float((((area/100)*10)+ area)/12),".2f")

print(f"You need {tile_boxes} tile boxes.")