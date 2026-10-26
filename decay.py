import random
import numpy as np
import matplotlib.pyplot as plt


def decay(m0 = 100000, p = [0.1, 0.02], timestep = 1, nstep = 200):
    survivors = m0
    survivorCounts = np.empty((p.length, 5))
    rng = np.random.default_rng()
    for row, decayP in enumerate(p):
        for col in range(5):
            survivors = m0
            for t in range(1, nstep + 1, 1):
                survivorCounts[row, col].append(survivors)
                u = rng.random(survivors)
                decays = (u < decayP).sum()
                survivors -= decays
            survivorCounts[row, col].append(survivors)
decay()