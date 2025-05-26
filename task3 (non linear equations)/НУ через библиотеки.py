import matplotlib.pyplot as plt
import scipy.optimize

def f(x, a, b, c):
    return a * x ** 2 + b * x + c


Xmin = -2
Xmax = 3
N = 25
A, B, C = -1.5, 2, 0.5

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

a = -0.5
b = 0
X0 = -0.5
roots_fsolve = scipy.optimize.fsolve(f, X0, args=(A, B, C))[0]
print('%15s %10.7f %10.3e' % ('fsolve', roots_fsolve, f(roots_fsolve, A, B, C)))
roots_bisect = scipy.optimize.bisect(f, a, b, args=(A, B, C))
print('%15s %10.7f %10.3e' % ('bisect', roots_bisect, f(roots_bisect, A, B, C)))
roots_newton = scipy.optimize.newton(f, X0, args=(A, B, C))
print('%15s %10.7f %10.3e' % ('newton', roots_newton, f(roots_newton, A, B, C)))