

import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def degrau_impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n >= a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = 0
MAX = 20

def f1(n):
    return n

def f2(n):
    return n

def f3(n):
    return pow(10, -0.3 * (n - 10))


x = np.arange(MIN, MAX + 1, 1)
y = (degrau_impulso(0, MIN, MAX) * x) + (degrau_impulso(10, MIN, MAX) * (f3(x) - f2(x))) - (degrau_impulso(20, MIN, MAX) * f3(x))

plt.stem(x, y)
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6d", fontsize=16)
plt.show()