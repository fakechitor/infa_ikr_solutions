import numpy as np
import matplotlib.pyplot as plt
from math import pi, sqrt

# Функция для интегрирования
def f(x):
    return 1 / (1 - x + x ** 2)

# Глобальные переменные
a, b = 0, 1  # границы
eps = 1e-50 # заданная погрешность
exact = 2 * pi / (3 * sqrt(3))  # точное решение

# Подготовим массив значений функции
array_size = 100000 # размер массива
x = np.linspace(a, b, array_size)
y = f(x)

# Метод левых прямоугольников
def left_rect(n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += y[i] * h  # Используем значения из массива y
    return s

# Метод правых прямоугольников
def right_rect(n):
    s = 0
    h = (b - a) / n
    for i in range(1, n + 1):
        s += y[i] * h  # Используем значения из массива y
    return s

# Метод средних прямоугольников
def middle_rect(n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += y[i + 1] * h  # Используем значения из массива y
    return s

# Метод трапеций
def trapezoid(n):
    s = 0
    h = (b - a) / n
    for i in range(n):
        s += h * (y[i] + y[i + 1]) / 2
    return s

# Метод Симпсона
def simpson(n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    s = 0
    for i in range(0, n, 2):
        s += (y[i] + 4 * y[i + 1] + y[i + 2]) * h / 3
    return s

# Метод для подсчета с учетом погрешности
def integrate_with_precision(method):
    n = 2
    max_n = array_size - 2  # Максимально возможное число разбиений
    prev = method(n)
    while True:
        n = min(n * 2, max_n)  # Увеличиваем n, но не превышаем max_n
        curr = method(n)
        if abs(curr - prev) < eps or n == max_n :
            return curr, n
        prev = curr

# Метод для подсчета значений и вывода в консоль
def count_with_method(method, name):
    value, n_used = integrate_with_precision(method)
    abs_err = abs(exact - value)
    rel_err = abs_err / exact
    print(f"{name:20} {value:<12.6f} {abs_err:<12.6f} {rel_err:<12.2e} {n_used}")

print('Mетод', ' ' * 22, 'Значение', ' ' * 2, 'АП', ' ' * 5, 'ОП', ' ' * 2, 'Разбиения')
print('-'*65)

# Подсчет для каждого метода
count_with_method(left_rect, "Левые прямоугольники")
count_with_method(right_rect, "Правые прямоугольники")
count_with_method(middle_rect, "Средние прямоугольники")
count_with_method(trapezoid, "Метод трапеций")
count_with_method(simpson, "Метод Симпсона")


plt.plot(x, y)
plt.title('График подынтегральной функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()
