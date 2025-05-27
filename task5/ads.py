import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

def f(x):
    return 1 / (1 - x + x ** 2)

def left_rect(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i*h)
    return s * h

def right_rect(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(1, n+1):
        s += f(a + i*h)
    return s * h

def middle_rect(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + (i+0.5)*h)
    return s * h

def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return s * h

def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i*h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i*h)
    return s * h / 3

# Метод для подсчета с учетом погрешности
def integrate_with_precision(method, f, a, b):
    n = 2
    prev = method(f, a, b, n)
    while True:
        n *= 2
        curr = method(f, a, b, n)
        if abs(curr - prev) < eps:
            return curr, n
        prev = curr

# Метод для подсчета значений и вывода в консоль
def count_with_method(method, name):
    value, n_used = integrate_with_precision(method, f, a, b)
    abs_err = abs(exact - value)
    rel_err = abs_err / exact
    print(f"{name:20} {value:<12.6f} {abs_err:<12.6f} {rel_err:<12.2e} {n_used}")



a, b = 0, 1 # границы
eps = 1e-6 # заданная погрешность
exact = 2 * pi / (3 * sqrt(3)) # точное решение

print('Mетод', ' ' * 22, 'Значение', ' ' * 2, 'АП', ' ' * 5, 'ОП', ' ' * 2, 'Разбиения')
print('-'*65)

count_with_method(left_rect, "Левые прямоугольники")
count_with_method(right_rect, "Правые прямоугольники")
count_with_method(middle_rect, "Средние прямоугольники")
count_with_method(trapezoid, "Метод трапеций")
count_with_method(simpson, "Метод Симпсона")

# График функции
x_vals = np.linspace(a, b, 100)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals)
plt.title('График подынтегральной функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()