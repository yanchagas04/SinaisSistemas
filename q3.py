
import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def degrau(t, a: float, funcao = lambda: 1) -> np.array:
    return np.heaviside(t - a, 1) * funcao()


MIN = -3
MAX = 3
T = 6

degx = np.linspace(MIN, MAX, num=calculate_points(MIN, MAX))

def f1():
    return (degx * (1/(T/2))) + 1

def f2():
    return (degx * (-1 * 1/(T/2))) + 1

y1 = degrau(t=degx, a=-T/2, funcao=f1) - degrau(t=degx, a=0, funcao=f1)
y2 = degrau(t=degx, a=0, funcao=f2) - degrau(t=degx, a=T/2, funcao=f2)

degy = y1 + y2

plt.plot(degx, degy)
plt.xlabel("t", fontsize=12)
plt.ylabel("v(t)", fontsize=12)
plt.title("v(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 3", fontsize=16)
plt.show()