import random
import numpy as np
import matplotlib.pyplot as plt

def montyHall(k=10000, seed = None):
    if k <= 0 or not isinstance(k, int):
        raise ValueError("k must be a positive integer")
    rng = np.random.default_rng(seed)
    N = [2, 3, 10, 100]
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.flatten()
    for index, n in enumerate(N):
        numWinStay = 0
        numWinSwitch = 0
        switchHist = []
        stayHist = []
        for i in range(1, k+1): #Always Switch Case
            prize = rng.integers(0,n)
            choice = rng.integers(0,n)
            if prize != choice:
                numWinSwitch +=1
            switchHist.append(numWinSwitch / i)
        for j in range(1, k+1): #Always Stay Case
            prize = rng.integers(0,n)
            choice = rng.integers(0,n)
            if prize == choice:
                numWinStay += 1
            stayHist.append(numWinStay / j)
        stayTheory = 1/n
        switchTheory = 1 - 1/n
        stayExperimental = numWinStay / k
        switchExperimental = numWinSwitch / k
        print(f"N = {n}: \nStay Theory: {stayTheory}, Stay Experimental: {stayExperimental}\nSwitch Theory: {switchTheory}, Switch Experiment: {switchExperimental}")
        ax = axs[index]
        trials = range(1, k + 1, 1)

        ax.plot(trials, stayHist, label="Stay Experimental")
        ax.plot(trials, switchHist, label="Switch Experimental")
        ax.axhline(stayTheory, color="blue", linestyle="--",
                   label="Stay Theory")
        ax.axhline(switchTheory, color="red", linestyle="--",
                   label="Switch Theory")
        ax.set_xscale("log")
        ax.set_xlabel("Number of Trials")
        ax.set_ylabel("Running Win Probability")
        ax.set_title(f"N = {n}")
        ax.grid(True)
        ax.legend()

        
    plt.show()
if __name__ == "__main__":
    montyHall(seed = 22)
    

