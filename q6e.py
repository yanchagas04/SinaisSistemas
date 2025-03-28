
import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n == a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = 0
MAX = 25

x = np.arange(MIN, MAX + 1, 1)
y = np.array([])


y = 0    
for m in np.arange(MIN, 11, 1):
    y += (impulso((2*m), MIN, MAX, lambda: (m + 1)) - impulso((2*m) + 1, MIN, MAX, lambda: (m + 1)))

plt.stem(x, y)
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6e", fontsize=16)
plt.show()