import functions.functions as functions
import numpy as np
import matplotlib.pyplot as plt

MIN = -3
MAX = 3
T = 6

degx = np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))

def f1():
    return (degx * (1/(T/2))) + 1

def f2():
    return (degx * (-1 * 1/(T/2))) + 1

y1 = functions.degrau(-1 * T/2, MIN, MAX, f1) - functions.degrau(0, MIN, MAX, f1)
y2 = functions.degrau(0, MIN, MAX, f2) - functions.degrau(T/2, MIN, MAX, f2)

degy = y1 + y2

plt.plot(degx, degy)
plt.xlabel("t", fontsize=12)
plt.ylabel("v(t)", fontsize=12)
plt.title("v(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 3", fontsize=16)
plt.show()