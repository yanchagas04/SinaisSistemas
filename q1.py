from matplotlib import pyplot as plt
import functions.functions as functions
import numpy as np

MIN = 0
MAX = 8
T = 2
A = 3

def periodo_impar(i: int, T: int) -> bool:
    if (i / T) % 2 == 0:
        return True
    return False

degx = np.linspace(MIN, MAX, num=functions.calculate_points(MIN, MAX))
degy = np.array([])

for i in range(MIN, MAX, T):
    degy = np.concatenate((degy, functions.degrau_etapa(i, i, i + T) * ((A if periodo_impar(i, T) else (-1) * A))))

plt.plot(degx, degy)
plt.show()