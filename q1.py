from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

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

degx = np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))
degy = np.zeros(functions.calculate_points(MIN, MAX))

for i in range(MIN, MAX, T):
    degy += functions.degrau(i, MIN, MAX, f1 if periodo_impar(i) else f2) - functions.degrau(i + T, MIN, MAX, f1 if periodo_impar(i) else f2)

plt.plot(degx, degy)
plt.ylabel("v(t)", fontsize=12)
plt.xlabel("t", fontsize=12)
plt.title("v(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 1", fontsize=16)
plt.show()