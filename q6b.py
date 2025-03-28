
import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n == a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = 0
MAX = 10

def f1(x):
    return (2 * np.cos((0.1 * x * np.pi) + (np.pi / 3)))

def f2(x):
    return (2 * np.sin((0.5 * x * np.pi)))

x = np.arange(MIN, MAX + 1, 1)
y = f1(x) + f2(x) 
plt.stem(x, np.imag(y) + np.real(y))
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 6b", fontsize=16)
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.show()