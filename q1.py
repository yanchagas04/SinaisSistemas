from matplotlib import pyplot as plt

import numpy as np

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def degrau(t, a: float, funcao = lambda: 1) -> np.array:
    return np.heaviside(t - a, 1) * funcao()

MIN = 0
MAX = 8
T = 2
A = 3

def periodo_impar(i: int) -> bool:
    if (i / T) % 2 == 0:
        return True
    return False

def f1():
    return A

def f2():
    return -1 * A

degx = np.linspace(MIN, MAX, num=calculate_points(MIN, MAX))
degy = np.zeros(calculate_points(MIN, MAX))

for i in range(MIN, MAX, T):
    degy += degrau(t=degx, a=i, funcao=f1 if periodo_impar(i) else f2) - degrau(t=degx, a=i + T, funcao=f1 if periodo_impar(i) else f2)

plt.plot(degx, degy)
plt.ylabel("v(t)", fontsize=12)
plt.xlabel("t", fontsize=12)
plt.title("v(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 1", fontsize=16)
plt.show()