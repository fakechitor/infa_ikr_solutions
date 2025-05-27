from math import *
import matplotlib.pyplot as plt
import scipy.optimize as so

def f(x):
    return 4 * sin(x + 0.5) + 0.1 * x ** 3 - x

def derivative(x):
    return 4 * cos(x + 0.5) + 0.3 * x ** 2 - 1

def newton(x, eps):
    n = 0
    while abs(f(x)) > eps:
        x = x - f(x) / derivative(x)
        n += 1
    return x, n

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


x_min = -4
x_max = 5
N = 100

x = []
y = []
h = abs(x_max - x_min) / (N - 1)
for i in range(N):
    x.append(x_min + i * h)
    y.append(f(x[i]))

plt.figure('График')
plt.title('График функции y(x)', fontsize=16, fontname='Times New Roman')
plt.grid(True)
plt.plot(x, y, c='m')

print('    Метод            X         f(x)       n')
print('-' * 45)


eps = 0.001
x0 = -1
x0_1 = 2
x0_2 = 4
a, b = -1, 0
a_1, b_1 = 2 ,3
a_2, b_2 = 4, 5

x1, n1 = newton(x0, eps)
print('%14s %10.4f %11.3e %5.d' % ('newton(свой)', x1, f(x1), n1))
x2, n2 = bisect(a_1, b_1, eps)
print('%14s %9.4f %11.3e %5.d' % ('bisect(свой)', x2, f(x2), n2))
x3, n3 = xord(a_2, b_2, eps)
print('%14s %10.4f %11.3e %5.d' % ('xord(свой)', x3, f(x3), n3))

x1 = so.newton(f, x0)
print('%14s %10.4f %11.3e' % ('newton(библ)', x1, f(x1)))
x2 = so.newton(f, x0_1)
print('%14s %10.4f %11.3e' % ('newton(библ)', x2, f(x2)))
x3 = so.newton(f, x0_2)
print('%14s %10.4f %11.3e' % ('newton(библ)', x3, f(x3)))

x1 = so.bisect(f, a, b)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x1, f(x1)))
x2 = so.bisect(f, a_1, b_1)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x2, f(x2)))
x3 = so.bisect(f, a_2, b_2)
print('%14s %9.4f %11.3e' % ('bisect(библ)', x3, f(x3)))

plt.scatter(x1, f(x1), label='Ньютон', color='red')
plt.scatter(x2, f(x2), label='Дихотомия', color='green')
plt.scatter(x3, f(x3), label='Хорд', color='orange')
plt.legend()
plt.show()