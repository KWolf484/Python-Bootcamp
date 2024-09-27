import random


num_gen = random.randint(1, 10)

if num_gen % 2 == 0:
    print("Heads")
else:
    print("Tails")