#n [u[n]−u[n−10]]

#10 ^ −0,3(n−10) [u[n−10] − u[n − 20]]
import functions.functions as functions
import numpy as np
import matplotlib.pyplot as plt

MIN = 0
MAX = 20

def f1(x):
    return x

def f2(x):
    return pow(10, -0.3 * (x - 10))

x = np.arange(MIN, MAX + 1, 1)
y1 = (functions.impulso(0, MIN, MAX) - functions.impulso(10, MIN, MAX)) * f1(x)
y2 = (functions.impulso(10, MIN, MAX) - functions.impulso(20, MIN, MAX)) * f2(x)
y = y1 + y2

plt.stem(x, y)
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6d", fontsize=16)
plt.show()