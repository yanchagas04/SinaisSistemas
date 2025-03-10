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
    degy += functions.degrau(i, i + T, MIN, MAX, f1 if periodo_impar(i) else f2)

plt.plot(degx, degy)
plt.show()