

import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n == a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = 0
MAX = 20

def f1(x):
    return x

def f2(x):
    return pow(10, -0.3 * (x - 10))

x = np.arange(MIN, MAX + 1, 1)
y1 = (impulso(0, MIN, MAX) - impulso(10, MIN, MAX)) * f1(x)
y2 = (impulso(10, MIN, MAX) - impulso(20, MIN, MAX)) * f2(x)
y = y1 + y2

plt.stem(x, y)
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6d", fontsize=16)
plt.show()