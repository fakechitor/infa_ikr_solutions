import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b, c):
    return a * x ** 2 + b * x + c


Xmin = -2     # Левая граница интервала построения графика
Xmax = 3      # Правая граница интервала построения графика
N = 25        # Количество точек, на которых будет вычисляться значение функции для графика
A, B, C = -1.5, 2, 0.5 # Коэффициенты квадратичной функции f(x)

# получаем список точек для построения графика
x = []
y = []
h = abs(Xmax - Xmin) / (N - 1)
for i in range(N):
    x.append(Xmin + i * h)
    y.append(f(x[i], A, B, C))

plt.figure('График')
plt.title('График функции y(x)', fontsize=16, fontname='Times New Roman')
plt.grid(True)
plt.plot(x, y, c='m')
plt.show()

# границы интервала, на котором ищем корень (для метода бисекции)
a = -0.5
b = 0

X0 = -0.5 # начальное приближение (для методов Ньютона и fsolve).

roots_fsolve = scipy.optimize.fsolve(f, X0, args=(A, B, C))[0] # через fsolve
print('%15s %10.7f %10.3e' % ('fsolve', roots_fsolve, f(roots_fsolve, A, B, C)))
roots_bisect = scipy.optimize.bisect(f, a, b, args=(A, B, C)) # метод бисекции
print('%15s %10.7f %10.3e' % ('bisect', roots_bisect, f(roots_bisect, A, B, C)))
roots_newton = scipy.optimize.newton(f, X0, args=(A, B, C)) # метод Ньютона
print('%15s %10.7f %10.3e' % ('newton', roots_newton, f(roots_newton, A, B, C)))