import numpy as np
import math


def simple_iter(f, x0, psi, accuracy=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 + f(x0)/psi
        if abs(x1 - x0) < accuracy:
            return x1
        x0 = x1
    raise ValueError("Метод простых итераций не сошёлся")


def newton_iter(f, df, x0, accuracy=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 + f(x0)/(-df(x0))
        if abs(x1 - x0) < accuracy:
            return x1
        x0 = x1
    raise ValueError("Метод Ньютона не сошёлся")


def secant_iter(f, x0, h=1e-4, accuracy=1e-6, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 + f(x0) / -((f(x0+h)-f(x0)) / h)
        if abs(x1 - x0) < accuracy:
            return x1
        x0 = x1
    raise ValueError("Метод секущих не сошёлся")


def wegstein_iter(f, x0, x1, accuracy=1e-6, max_iter=100):
    for _ in range(max_iter):
        x2 = x1 + f(x1) / -((f(x1)-f(x0))/(x1 - x0))
        if abs(x2 - x1) < accuracy:
            return x2
        x0, x1 = x1, x2
    raise ValueError("Метод Вегстейна не сошёлся")


def function(x): return math.sin(x) - 2.3 * x - 2.8
def dFunction(x): return math.cos(x) - 2.3


psi = (max(abs(dFunction(x)) for x in np.arange(-10, 10, 0.01))) / 2 + 1e-5
x = simple_iter(function, 1, psi)
print("Метод простых итераций:", x)

x = newton_iter(function, dFunction, 1)
print("Метод Ньютона:", x)

x = secant_iter(function, 1)
print("Метод секущих:", x)

x = wegstein_iter(function, 1, 1.01)
print("Метод Вегстейна:", x)
