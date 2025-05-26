import matplotlib.pyplot as plt
import scipy.optimize

def f(x):
    return -1.5 * x ** 2 +2 * x + 0.5


x_min = -2     # Левая граница интервала построения графика
x_max = 3      # Правая граница интервала построения графика
N = 25         # Количество точек, на которых будет вычисляться значение функции для графика

# получаем список точек для построения графика
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
plt.show()

# границы интервала, на котором ищем корень (для метода бисекции)
a = -0.5
b = 0

X0 = -0.5 # начальное приближение (для методов Ньютона и fsolve).

roots_fsolve = scipy.optimize.fsolve(f, X0)[0] # через fsolve
print('%15s %10.7f %10.3e' % ('fsolve', roots_fsolve, f(roots_fsolve)))
roots_bisect = scipy.optimize.bisect(f, a, b) # метод бисекции
print('%15s %10.7f %10.3e' % ('bisect', roots_bisect, f(roots_bisect)))
roots_newton = scipy.optimize.newton(f, X0) # метод Ньютона
print('%15s %10.7f %10.3e' % ('newton', roots_newton, f(roots_newton)))