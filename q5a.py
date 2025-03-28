
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Configurações
t_min, t_max = -5, 5
num_frames = 100
t_values = np.linspace(t_min, t_max, num_frames)

# Funções definidas por partes
def x(tau):
    return np.exp(tau) * (tau <= 0)  # x(tau) = e^tau * u(-tau)

def h(tau):
    return 1.0 * (tau >= 0)          # h(tau) = u(tau)

# Cálculo da convolução y(t)
def y(t):
    if t < 0:
        return np.exp(t)              # y(t) = e^t para t < 0
    else:
        return 1.0                   # y(t) = 1 para t >= 0

# Configuração da figura
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.tight_layout()

# Frame inicial
def init():
    ax1.clear()
    ax2.clear()
    ax1.set_xlim(t_min, t_max)
    ax1.set_ylim(-0.1, 1.5)
    ax1.set_title("Sinais $x(\\tau)$ e $h(t-\\tau)$")
    ax1.set_xlabel("$\\tau$")
    ax1.grid(True)
    
    ax2.set_xlim(t_min, t_max)
    ax2.set_ylim(-0.1, 1.5)
    ax2.set_title("Resultado da Convolução $y(t)$")
    ax2.set_xlabel("$t$")
    ax2.grid(True)
    return []

# Atualização para cada frame
def update(frame):
    t = t_values[frame]
    tau = np.linspace(t_min, t_max, 1000)
    
    # Plotar x(tau) e h(t - tau) em ax1
    ax1.clear()
    ax1.plot(tau, x(tau), 'b-', label='$x(\\tau) = e^\\tau u(-\\tau)$', linewidth=2)
    ax1.plot(tau, h(t - tau), 'r-', label='$h(t-\\tau) = u(t-\\tau)$', linewidth=2)
    
    # Destacar a área de sobreposição (integral)
    mask = (tau <= min(t, 0))  # Região onde x(tau) e h(t-tau) são não-nulos
    ax1.fill_between(tau[mask], 0, x(tau)[mask], color='purple', alpha=0.3)
    
    ax1.set_xlim(t_min, t_max)
    ax1.set_ylim(-0.1, 1.5)
    ax1.legend(loc='upper right')
    ax1.set_title(f"Convolução em $t = {t:.1f}$")
    ax1.grid(True)
    
    # Plotar y(t) acumulado em ax2
    ax2.clear()
    ax2.plot(t_values[:frame+1], [y(t_val) for t_val in t_values[:frame+1]], 
             'k-', linewidth=2, label='$y(t) = x(t) * h(t)$')
    ax2.set_xlim(t_min, t_max)
    ax2.set_ylim(-0.1, 1.5)
    ax2.legend(loc='upper right')
    ax2.grid(True)  
    
    return []

# Criar a animação
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=50)

# Salvar como GIF (requer pillow)
ani.save('Graficos/questao5a.gif', writer='pillow', fps=20, dpi=100)
print("GIF salvo como 'questao5a.gif' na pasta 'Graficos'.")