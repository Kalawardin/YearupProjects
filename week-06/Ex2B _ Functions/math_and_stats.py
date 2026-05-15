import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# 75 

sum75 = sum(vals_sample)
avg75 = statistics.mean(vals_sample)
med75 = statistics.median(vals_sample)

# 200

sum200 = statistics.mean(vals_choices) 
avg200 = statistics.median(vals_choices) 
mod200 = statistics.mode(vals_choices) 
stdev200 = statistics.stdev(vals_choices) 
var200 = statistics.variance(vals_choices) 

# area

area = pi * (radius ** 2)
round_up = math.ceil(area)
round_down = math.floor(area)

print("Experimenting with a superset of 200 values, integers 1-100:")

print(f"Sum of 75 sample values from 1 to 100: {sum75}")
print(f"Average of 75 sample values: {avg75}")
print(f"Median of 75 sample values: {med75}\n")

print("Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {sum200}")
print(f"Median of 200 values: {avg200}")
print(f"Mode of 200 values: {mod200}")
print(f"Standard deviation of 200 values: {stdev200}")
print(f"Variance of 200 values: {var200}\n")

print("Modeling a random circle:")
print(f"Radius = {round_up} , area = {area}")
print(f"Radius = {round_down}, area =  {area}")