from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

MIN = -1
MAX = 4

def f1():
    return ((2 * np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))) + 1)

def f2():
    return 3

def f3():
    return ((-1 * np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))) + 3)

y1 = functions.degrau(0, MIN, MAX, f1) - functions.degrau(1, MIN, MAX, f1)
y2 = functions.degrau(1, MIN, MAX, f2) - functions.degrau(2, MIN, MAX, f2)
y3 = functions.degrau(2, MIN, MAX, f3) - functions.degrau(3, MIN, MAX, f3)

degx = np.linspace(-1, 4, num=functions.calculate_points(-1, 4))
degy = y1 + y2 + y3

plt.plot(degx, degy)
plt.show()