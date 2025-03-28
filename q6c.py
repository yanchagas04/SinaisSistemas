
import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n == a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = -5
MAX = 5

def f1():
    return 2

x = np.arange(MIN, MAX + 1, 1)
y = impulso(-2, MIN, MAX, f1) - impulso(4, MIN, MAX)

plt.stem(x, y)
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6c", fontsize=16)
plt.show()