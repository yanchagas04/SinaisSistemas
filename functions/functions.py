import numpy as np

def calculate_points(min: int, max: int) -> int:
    return (50 * (max - min))

def degrau(a: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n > a else 0 for n in np.linspace(min, max, num=calculate_points(min, max))]) * funcao()