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
y = f1(x) + f2(x) 
plt.stem(x, np.imag(y) + np.real(y))
plt.xlabel("n", fontsize=12)
plt.ylabel("x[n]", fontsize=12)
plt.title("x[n] x n", fontsize=12)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.suptitle("Questão 6b", fontsize=16)
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.show()