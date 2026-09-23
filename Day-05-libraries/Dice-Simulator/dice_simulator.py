import math , random

roll1 = random.randint(1,7)
roll2 = random.randint(1,7)

print(f"Roll 1: {roll1} | Roll 2: {roll2}")
total_sum = roll1 + roll2;
print(f"Sum : {total_sum}")

root_value = math.sqrt(total_sum)
print(f"Square root: {root_value}")