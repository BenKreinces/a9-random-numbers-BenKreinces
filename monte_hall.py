import random
import numpy as np


def monteHall(k=10000, seed = None):
    rng = (np.random.default_rng(seed) if seed else np.random.default_rng())
    N = [2, 3, 10, 100]
    for n in N:
        numWinStay = 0
        numWinSwitch = 0
        for _ in range(k): #Always Switch Case
            prize = rng.integers(0,n)
            choice = rng.integers(0,n)
            if prize != choice:
                numWinSwitch +=1
        for _ in range(k): #Always Stay Case
            prize = rng.integers(0,n)
            choice = rng.integers(0,n)
            if prize == choice:
                numWinStay += 1
    


            