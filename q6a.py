import functions.functions as functions
import numpy as np
import matplotlib.pyplot as plt

MIN = 0
MAX = 10

#e^jn
def f_imaginario(n):
    return (np.sin(n))

def f_real(n):
    return (np.cos(n))

x = np.arange(MIN, MAX + 1, 1)
y_real = functions.impulso(0, MIN, MAX) * f_real(x)
y_imag = functions.impulso(0, MIN, MAX) * f_imaginario(x)

plt.subplots_adjust(hspace=0.5)
plt.subplot(2, 1, 1).title.set_text("Parte Real")
plt.stem(x, y_real)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))

plt.subplot(2, 1, 2).title.set_text("Parte Imaginária")
plt.stem(x, y_imag)
plt.grid(axis='both', color='lightgray', linestyle='--')
plt.xticks(np.arange(MIN, MAX + 1, 1))
plt.suptitle("Questão 6a", fontsize=16)

plt.show()

# plt.stem(x, y)
# plt.xlabel("n", fontsize=12)
# plt.ylabel("x[n]", fontsize=12)
# plt.title("x[n] x n", fontsize=12)
# plt.grid(axis='both', color='lightgray', linestyle='--')
# plt.xticks(np.arange(MIN, MAX + 1, 1))
# plt.suptitle("Questão 6a", fontsize=16)
# plt.show()