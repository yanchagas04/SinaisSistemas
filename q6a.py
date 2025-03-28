import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: float, max: float):
    return (50 * (int(max) - int(min)))

def impulso(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n >= a else 0 for n in np.arange(min, max + 1, 1)]) * funcao()

MIN = 0
MAX = 10

#e^jn
def f(n):
    return (np.exp(1j * n))

x = np.arange(MIN, MAX + 1, 1)
y = impulso(0, MIN, MAX) * f(x) 
y_real = impulso(0, MIN, MAX) * np.real(f(x))
y_imag = impulso(0, MIN, MAX) * np.imag(f(x))

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando a parte real
plt.stem(x, y_real, linefmt='b-', markerfmt='bo', basefmt=' ', label='Parte Real')

# Plotando a parte imaginária
plt.stem(x, y_imag, linefmt='r--', markerfmt='rs', basefmt=' ', label='Parte Imaginária')

# Configurações do gráfico
plt.title('Questão 6a', fontsize=14)
plt.xlabel('n', fontsize=12)
plt.ylabel('x[n]', fontsize=12)
plt.xticks(x)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()