
import numpy as np
import matplotlib.pyplot as plt

# Definir o intervalo de t
t = np.linspace(-5, 5, 1000)

# Calcular y(t)
y = np.piecewise(t, [t < 0, t >= 0], [lambda t: np.exp(t), lambda t: 1])

# Plotar o gráfico
plt.figure(figsize=(8, 4))
plt.plot(t, y, label='$y(t) = x(t) * h(t)$', color='blue')
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.title('Convolução entre $x(t) = e^t u(-t)$ e $h(t) = u(t)$')
plt.axvline(x=0, color='black', linestyle='--', alpha=0.3)
plt.axhline(y=1, color='black', linestyle='--', alpha=0.3)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
