import numpy as np

def simple_method(matrix_A, matrix_B, accuracy = 1e-10, max_iter = 1000):
    matrix_X = np.zeros_like(matrix_B)
    matrix_X = matrix_B.copy()
    for _ in range(max_iter):
        matrix_X_old = matrix_X.copy()
        matrix_X = matrix_X + (matrix_B - np.dot(matrix_A, matrix_X)) / np.diagonal(matrix_A)
        if np.linalg.norm(matrix_X_old - matrix_X, ord = np.inf) < accuracy:
            return matrix_X
    raise ValueError("Метод простых итераций не сошёлся")

def seidel_method(matrix_A, matrix_B, accuracy = 1e-10, max_iter = 1000):
    matrix_X = np.zeros_like(matrix_B)
    matrix_X = matrix_B.copy()
    for _ in range(max_iter):
        matrix_X_old = matrix_X.copy()

        for i in range(len(matrix_A)):
            s = np.dot(matrix_A[i], matrix_X) - matrix_A[i,i] * matrix_X[i]
            matrix_X[i] = (matrix_B[i] - s) / matrix_A[i,i]
        if np.linalg.norm(matrix_X_old - matrix_X, ord = np.inf) < accuracy:
            return matrix_X
    raise ValueError("Метод Зейделя не сошёлся")

matrix_A = np.array([[40.42, 2.42, 3.24],
                    [2.31, 32.49, 1.52],
                    [1.49, 2.85, 20.92]], dtype = float)
matrix_B = np.array([10.75,20.16,22.51], dtype = float)

matrix_X_by_simple = simple_method(matrix_A, matrix_B)
matrix_X_by_seidel = seidel_method(matrix_A, matrix_B)

print("Решение с помощью метода простых итераций:", matrix_X_by_simple)
print("Проверка метода простых итераций: ", np.round(np.dot(matrix_A, matrix_X_by_simple) - matrix_B))

print("Решение с помощью метода Сейделя:", matrix_X_by_seidel)
print("Проверка метода Сейделя: ", np.round(np.dot(matrix_A, matrix_X_by_seidel) - matrix_B))
