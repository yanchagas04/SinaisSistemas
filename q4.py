from matplotlib import pyplot as plt

import numpy as np

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def degrau(t, a: float, funcao = lambda: 1) -> np.array:
    return np.heaviside(t - a, 1) * funcao()

MIN = -1
MAX = 4

def f1():
    return ((2 * np.linspace(MIN, MAX, num=calculate_points(MIN, MAX))) + 1)

def f2():
    return 3

def f3():
    return ((-1 * np.linspace(MIN, MAX, num=calculate_points(MIN, MAX))) + 3)

degx = np.linspace(-1, 4, num=calculate_points(-1, 4))

y1 = degrau(degx, 0, f1) - degrau(degx, 1, f1)
y2 = degrau(degx, 1, f2) - degrau(degx, 2, f2)
y3 = degrau(degx, 2, f3) - degrau(degx, 3, f3)

degy = y1 + y2 + y3

plt.plot(degx, degy)
plt.xlabel("t", fontsize=12)
plt.ylabel("v(t)", fontsize=12)
plt.title("v(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 4", fontsize=16)
plt.show()