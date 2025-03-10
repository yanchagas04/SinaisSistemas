from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

MIN = -2
MAX = 2
T = 3
A = 6

def f1():
    return A

y1 = functions.degrau(-1 * T/2, MIN, MAX, f1) - functions.degrau(T/2, MIN, MAX, f1)

degx = np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))
degy = y1

plt.plot(degx, degy)
plt.show()