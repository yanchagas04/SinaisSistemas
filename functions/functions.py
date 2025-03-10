import numpy as np
import matplotlib.pyplot as plt

def calculate_points(min: int, max: int) -> int:
    return (50 * (max - min))

def degrau(a: int, b: int, min: int, max: int, funcao = lambda: 1) -> np.array:
    return np.array([1 if n > a and n < b else 0 for n in np.linspace(min, max, num=calculate_points(min, max))]) * funcao()