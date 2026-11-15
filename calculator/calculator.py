import numpy as np

def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b

def divide(a, b):
    """Делит первое число на второе."""
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a / b

def square_root(a):
    """Возвращает квадратный корень числа."""
    return np.sqrt(a)

print(add(2, 3))
print(subtract(5, 4))
print(multiply(4, 21))
print(divide(10, 2))
print(square_root(16))
