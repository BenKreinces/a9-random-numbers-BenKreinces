import random
import numpy as np
import matplotlib.pyplot as plt


def decay(m0 = 100000, p = (0.1, 0.02), timestep = 1, nstep = 200, seed = None):
    survivors = m0
    survivorCounts = np.zeros((len(p), 5, nstep + 1), dtype=int)
    survivorCountsTheory = np.zeros((len(p), nstep + 1))
    rng = np.random.default_rng(seed)
    times = np.arange(nstep + 1) * timestep
    for row, decayP in enumerate(p):
        lmda = -1 * np.log(1-decayP) / timestep 
        survivorCountsTheory[row]= m0 * np.exp(-lmda * times)
        for col in range(5):
            survivors = m0
            survivorCounts[row, col, 0] = m0
            for t in range(1, nstep + 1, 1):
                
                
                u = rng.random(survivors)
                decays = (u < decayP).sum()
                survivors -= decays
                survivorCounts[row, col, t]= survivors

    
decay()