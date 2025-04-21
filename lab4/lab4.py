import numpy as np
import matplotlib.pyplot as plt


# Интерполяция функции 
x = np.array([1.8545, 1.5022, 1.1732, 0.8330, 0.5589, 0.3354, 0.1948])
y = np.array([0.8492, 0.9002, 0.9387, 0.9689, 0.9860, 0.9949, 0.9983])
xc = 0.3

print("Интерполяция функции")
v = np.vander(x, N=len(x))
print("v = ", v)

coeff = np.linalg.solve(v, y)
print("c = ", coeff)

xd = np.linspace(np.min(x), np.max(x), 200)
yd = np.polyval(coeff, xd)
yc = np.polyval(coeff, xc)

plt.plot(x, y, 'ro', label="Исходные точки")
plt.plot(xc, yc, 'g*', label="Точка")
plt.plot(xd, yd, 'b-', label="Интерполяция")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Метод Лагранжа
X = np.array([1.8545, 1.5022, 1.1732, 0.8330, 0.5589, 0.3354, 0.1948])
Y = np.array([0.8492, 0.9002, 0.9387, 0.9689, 0.9860, 0.9949, 0.9983])
N = len(x)

def ll (i, x):
    acc = 1
    for k in range(N):
        if i != k:
            acc *= (x - X[k])
    return acc

def l (i, x):
    return ll(i,x) / ll(i, X[i])

def Lagrange(x):
    return sum(Y[i] * l(i,x) for i in range(N))

print("\nМетод Лагранжа")
vector = np.vectorize(Lagrange)

v = np.vander(X, N=len(X))
print("v = ", v)

coeff = np.linalg.solve(v, Y)
print("c = ", coeff)

x = np.linspace(np.min(X), np.max(X), 200)
y = vector(x)

xc = 0.3
yc = np.polyval(coeff, xc)

plt.plot(X, Y, 'ro', label="Исходные точки")
plt.plot(xc, yc, 'g*', label="Точка")
plt.plot(x, y, 'b-', label="Интерполяция")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
