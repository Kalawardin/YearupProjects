
f = open("about_me.txt", "a")

f.write("\nPerfect night out: Spending the night parked under the stars in my micro-camper after a long drive, maybe playing some CS2 if I have internet connection.\n")

f.close()


f = open("about_me.txt", "r")

first_50_chars = f.read(50)

readline_list = []
for i in range(1, 5):
    readline_list.append(f.readline())

readlines_output = f.readlines(100)

f.close()

print("First 50 characters:", first_50_chars)
print("\nOutput from loop using .readline():", readline_list)
print("\nOutput from .readlines(100):", readlines_output)