from math import *
import matplotlib.pyplot as plt
import scipy.optimize as so

# метод с заданной функцией
def f(x):
    return 4 * sin(x + 0.5) + 0.1 * x ** 3 - x

# метод с производной заданной функции
def derivative(x):
    return 4 * cos(x + 0.5) + 0.3 * x ** 2 - 1

# самописный метод Ньютона
def newton(x, eps):
    n = 0
    while abs(f(x)) > eps:
        x = x - f(x) / derivative(x)
        n += 1
    return x, n

# самописный метод Дихтомии
def bisect(a, b, eps):
    n = 0
    while abs(b - a) / 2 > eps:
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        n += 1
    return (a + b) / 2, n

# самописный метод хорд
def xord(a, b, eps):
    n = 0
    x = a - f(a) * (b - a) / (f(b) - f(a))
    while abs(f(x)) > eps:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = a - f(a) * (b - a) / (f(b) - f(a))
        n += 1
    return x, n


x_min = -4 # Левая граница интервала построения графика
x_max = 5 # Правая граница интервала построения графика
N = 100 # Количество точек, на которых будет вычисляться значение функции для графика

# получаем точки для графика
x = []
y = []
h = abs(x_max - x_min) / (N - 1)
for i in range(N):
    x.append(x_min + i * h)
    y.append(f(x[i]))

# рисуем график по точкам
plt.figure('График')
plt.title('График функции y(x)', fontsize=16, fontname='Times New Roman')
plt.grid(True)
plt.plot(x, y, c='m')
# я закомментировал plt.show(), если ты будешь использовать легенду и точки в конце, то забей,
# если не будешь - надо писать строчку снизу без комментария
# plt.show()

# Выводим названия столбцов для таблички
print('    Метод            X         f(x)       n')
print('-' * 45)

# тут вынес все значения в переменные
eps = 0.001 # эпсилон для погрешности
x0 = -1  # начальное приближение
x0_1 = 2 # начальное приближение
x0_2 = 4 # начальное приближение
a, b = -1, 0  # границы интервала, на котором ищем корень
a_1, b_1 = 2 ,3 # границы интервала, на котором ищем корень
a_2, b_2 = 4, 5 # границы интервала, на котором ищем корень

# находим и выводим в консоль значения для самописных методов
x1, n1 = newton(x0, eps) # метод Ньютона
print('%14s %10.4f %11.3e %5.d' % ('newton(свой)', x1, f(x1), n1))
x2, n2 = bisect(a_1, b_1, eps) # метод Дихтомии
print('%14s %9.4f %11.3e %5.d' % ('bisect(свой)', x2, f(x2), n2))
x3, n3 = xord(a_2, b_2, eps) # метод хорд
print('%14s %10.4f %11.3e %5.d' % ('xord(свой)', x3, f(x3), n3))

# находим и выводим в консоль значения для библиотечных методов, чтобы проверить свои методы на валидность
# метод Ньютона
x1 = so.newton(f, x0) # тут so, потому что используем метод из библиотеки scipy.optimize который импортим как so
print('%14s %10.4f %11.3e' % ('newton(библ)', x1, f(x1)))
x2 = so.newton(f, x0_1)
print('%14s %10.4f %11.3e' % ('newton(библ)', x2, f(x2)))
x3 = so.newton(f, x0_2)
print('%14s %10.4f %11.3e' % ('newton(библ)', x3, f(x3)))

# через метод Дихтомии
x1 = so.bisect(f, a, b)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x1, f(x1)))
x2 = so.bisect(f, a_1, b_1)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x2, f(x2)))
x3 = so.bisect(f, a_2, b_2)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x3, f(x3)))


# тут ниже будет код для точек на графике и легенды, если не нужно можешь забить
plt.scatter(x1, f(x1), label='Ньютон', color='red')
plt.scatter(x2, f(x2), label='Дихотомия', color='green')
plt.scatter(x3, f(x3), label='Хорд', color='orange')
plt.legend()
plt.show()