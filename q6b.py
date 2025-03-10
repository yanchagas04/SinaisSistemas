import functions.functions as functions
import numpy as np
import matplotlib.pyplot as plt

MIN = 0
MAX = 10

def f1(x):
    return (2 * np.cos((0.1 * x * np.pi) + (np.pi / 3)))

def f2(x):
    return (2 * np.sin((0.5 * x * np.pi)))

x = np.arange(MIN, MAX + 1, 1)
# 2cos(0, 1πn+π/3)+2sen(0, 5πn)
y = f1(x) + f2(x) 
plt.stem(x, np.imag(y) + np.real(y))
plt.xlabel("n")
plt.ylabel("x[n]")
plt.show()