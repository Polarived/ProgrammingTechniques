import random

class Format():
    def __init__(self):
        pass
    def bformat(self, rng: int):
        num = random.randint(0,self.rng)
        tries = 0
        while True:
            self.rng /= 2
            tries += 1
            if rng == num:
                print(f"It took {tries}, tries")
                print("Found the number!")
                break
            else:
                print(f"Tries: {tries}")


RAHH = Format()
RAHH.bformat(1000000)
