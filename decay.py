import random
import numpy as np
import matplotlib.pyplot as plt



def decay(m0 = 100000, p = (0.1, 0.02), timestep = 1, nstep = 200, seed = None):
    if not isinstance(m0, int) or m0 < 1:
            raise ValueError("m0 must be a positive integer")
    if not isinstance(nstep, int) or nstep < 1:
        raise ValueError("nstep must be a positive integer")
    if timestep <= 0:
        raise ValueError("timestep must be positive")
    for decayP in p:
        if not 0 <= decayP < 1:
            raise ValueError("p must be between 0 and 1")
    

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

    
    average = survivorCounts.mean(axis = 1)
    assert np.all((survivorCounts >= 0) & (survivorCounts <= m0))
    assert np.all(np.diff(survivorCounts, axis=2) <= 0)
    for row, decayP in enumerate(p):
        if decayP == 0:
            assert np.all(survivorCounts[row] == m0)

    fig, axs = plt.subplots(1, len(p), figsize=(7 * len(p), 5), squeeze=False)

    for row, decayP in enumerate(p):
        ax = axs[0, row]
        lmda = -np.log(1 - decayP) / timestep

        if lmda > 0:
            predicted = np.log(2) / lmda
            measured = times[np.argmin(abs(average[row] - m0 / 2))]
            difference = (measured - predicted) / predicted
            print(f'p = {decayP}, lambda = {lmda} 1/s')
            print(f'Predicted half-life = {predicted} s')
            print(f'Measured half-life = {measured}')
            print(f'Relative difference = {difference}\n')
        else:
            measured = None
            print('p = 0: no decay; half-life is infinite\n')

        for col in range(5):
            counts = survivorCounts[row, col].astype(float)
            counts[counts == 0] = np.nan
            ax.plot(times, counts, linewidth=0.8, label=f'Run {col + 1}')

        ax.plot(times, np.where(average[row] > 0, average[row], np.nan),
                color='black', linewidth=2, label='Average')
        ax.plot(times, np.where(survivorCountsTheory[row] > 0, survivorCountsTheory[row],np.nan),
                color='red', linestyle='--', label='Theory')
        ax.axhline(m0 / 2, color='gray', linestyle=':', label='Half population')
        if measured is not None:
            ax.axvline(measured, color='purple', linestyle=':', label='Measured half-life')
        ax.set_yscale('log')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Number of surviving nuclei')
        ax.set_title(f'p = {decayP}')
        ax.legend(fontsize=8)
        ax.grid(True)

        ax.set_ylim(bottom=1)
    plt.tight_layout()
    return survivorCounts




if __name__ == '__main__':
  
    decay(seed=42)
    plt.show()