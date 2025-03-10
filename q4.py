from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

MIN = -1
MAX = 4

x1 = np.linspace(MIN, 0, num=functions.calculate_points(MIN, 0))

x2 = np.linspace(0, 1, num=functions.calculate_points(0, 1))

x3 = np.linspace(1, 2, num=functions.calculate_points(1, 2))

x4 = np.linspace(2, 3, num=functions.calculate_points(2, 3))

x5 = np.linspace(3, MAX, num=functions.calculate_points(3, MAX))

degx = np.concatenate((x1, x2, x3, x4, x5))

def f2(x):
    return (2 * x) + 1

def f4(x):
    return (-1 * x) + 3

f1 = np.zeros(functions.calculate_points(-1, 0))
f3 = np.ones(functions.calculate_points(1, 2)) * 3
f5 = np.zeros(functions.calculate_points(3, 4))

degy = np.concatenate((f1, f2(x2), f3, f4(x4), f5))

plt.plot(degx, degy)
plt.show()