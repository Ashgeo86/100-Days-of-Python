import random

#random_integer = random.randint(1, 10)
#print(random_integer)

#random.random will randomly generate a number between 0.0 and 1.0
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#random.uniform return a random floating point that are between a and b, inclusive of a and b
random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")