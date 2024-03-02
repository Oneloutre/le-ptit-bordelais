import random

def roulette():
    if random.randint(1, 6) == 6:
        return 1
    else:
        return 0