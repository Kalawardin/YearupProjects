import math

passenger = float(input("How many tourists?: "))
van_count = math.ceil(passenger/15)
van_cost = van_count * 250
per_person_cost = math.ceil(van_cost/passenger)

print(f"We need {van_count} vans.\nIt cost us in total ${van_cost}\nWe spend each passenger ${per_person_cost}.")