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
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6c", fontsize=16)
plt.show()