from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

T = 3
MIN = -T/2
MAX = T/2
A = 6

def f1():
    return A

y1 = functions.degrau(-1 * T/2, MIN, MAX, f1) - functions.degrau(T/2, MIN, MAX, f1)

degx = np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))
degy = y1

plt.plot(degx, degy)
plt.ylabel("i(t)", fontsize=12)
plt.xlabel("t", fontsize=12)
plt.title("i(t) x t", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 2", fontsize=16)
plt.show()