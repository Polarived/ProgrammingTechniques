import random

def bformat(rng: int):
    num = random.randint(0,rng)
    tries = 0
    while True:
        tries += 1
        if rng == num:
            print(f"It took {tries}, tries")
            print("Found the number!")
            break
        elif num < rng:
            rng /= 2
        else:
            print(f"Tries: {tries}")



bformat(1000000)
