import math


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n должно быть чётным для метода Симпсона.")
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        result += 2 * f(a + i * h)
    result *= h / 3
    return result


def max_second_derivative(f, a, b):
    # численное приближение второй производной
    h = 1e-5
    x = a
    max_val = 0
    while x <= b:
        d2 = abs((f(x - h) - 2 * f(x) + f(x + h)) / h**2)
        max_val = max(max_val, d2)
        x += (b - a) / 1000
    return max_val


def max_fourth_derivative(f, a, b):
    # численное приближение четвертой производной
    h = 1e-3
    x = a
    max_val = 0
    while x + 2 * h <= b:
        d4 = abs(
            (f(x - 2 * h) - 4 * f(x - h) + 6 * f(x) - 4 * f(x + h) + f(x + 2 * h))
            / h**4
        )
        max_val = max(max_val, d4)
        x += (b - a) / 1000
    return max_val


if __name__ == "__main__":
    def f1(x):
        return 1 / math.sqrt(x**2 + 0.5)

    def f2(x):
        return math.tan(x**2 + 0.5) / (x**2 + 1)

    a1, b1 = 1.2, 2.6
    a2, b2 = 0.4, 0.8
    # h = (b - a) / n

    # Task 1
    n1 = 10

    result_trapezoidal = trapezoidal_rule(f1, a1, b1, n1)
    error_trapezoidal = abs((b1 - a1)**3 / (12 * n1**2)
                            * max_second_derivative(f1, a1, b1))
    error_n_trapezoidal = abs(((b1 - a1) * ((b1 - a1) / n1)**2) /
                              12 * max_second_derivative(f1, a1, b1))

    print("Задача 1")
    print(
        f"Метод трапеций: {result_trapezoidal:.6f}, error {error_trapezoidal:.8f}, error_n {error_n_trapezoidal:.8f} ")

    # Task 2
    n_s1 = 16
    n_s2 = 8

    result_simpson_s_16 = simpson_rule(f2, a2, b2, n_s1)
    result_simpson_s_8 = simpson_rule(f2, a2, b2, n_s2)

    error_simpson_r_2n = abs(result_simpson_s_8 - result_simpson_s_16) / 15
    error_simpson_r_n = abs((b2 - a2) * ((b2 - a2) / n_s1)
                            ** 4 / 180 * max_fourth_derivative(f2, a2, b2))

    print("Задача 2")
    print(
        f"Метод Симпсона: {result_simpson_s_16:.6f}, error_2n {error_simpson_r_2n:.8f}, error_n {error_simpson_r_n:.8f} ")
