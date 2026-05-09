candy = ("Skittles","Starburst","Jolly Ranchers")
flavors = ("Strawberry","Watermelon","Mango")

candy_combos = set()
candy_combos.add(candy[0] + " " + flavors[1])  # Skittles Watermelon
candy_combos.add(candy[1] + " " + flavors[0])  # Starburst Strawberry
candy_combos.add(candy[2] + " " + flavors[2])  # Jolly Ranchers Mango

print("Today's candy options include:")
print(candy_combos)