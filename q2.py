from matplotlib import pyplot as plt

import numpy as np

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def degrau(t, a: float, funcao = lambda: 1) -> np.array:
    return np.heaviside(t - a, 1) * funcao()

T = 3
MIN = -T/2
MAX = T/2
A = 6

def f1():
    return A


degx = np.linspace(MIN - T, MAX + T, num=10000)
y1 = degrau(t=degx, a=-T/2, funcao=f1) - degrau(t=degx, a=T/2, funcao=f1)
degy = y1

plt.plot(degx, degy)
plt.ylabel("i(t)", fontsize=12)
plt.xlabel("t", fontsize=12)
plt.title("i(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 2", fontsize=16)
plt.show()