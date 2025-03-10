#x[n] = 2δ[n + 2] − δ[n − 4], −5 ≤ n ≤ 5
import functions.functions as functions
import numpy as np
import matplotlib.pyplot as plt

MIN = -5
MAX = 5

def f1():
    return 2

x = np.arange(MIN, MAX + 1, 1)
y = functions.impulso(-2, MIN, MAX, f1) - functions.impulso(4, MIN, MAX)

plt.stem(x, y)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()