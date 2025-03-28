import numpy as np
import matplotlib.pyplot as plt

# Definir os valores de n e y[n]
n = np.array([-3, -2, -1, 0, 2])
y = np.array([2, 4, 2, 2, -2])

# Plotar o gráfico usando stem
plt.figure(figsize=(8, 4))
markerline, stemlines, baseline = plt.stem(n, y, label='x[n]')
plt.setp(markerline, color='blue', markersize=8)
plt.setp(stemlines, color='blue', linewidth=1.5)
plt.setp(baseline, color='black', linewidth=0.5)

plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Convolução entre x[n+2] e h[n]')
plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
