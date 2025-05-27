import matplotlib.pyplot as plt
import scipy.optimize

def  f(x):
    return -1.5 * x ** 2 +2 * x + 0.5


x_min = -2
x_max = 3
N = 25

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

a = -0.5
b = 0
X0 = -0.5

# тут вывод более простой, если тот формат вывода некритичен, можешь этот лучше использовать, он намного легче как будто
roots_fsolve = scipy.optimize.fsolve(f, X0)[0]
print("fsolve:", roots_fsolve, "f(root):", f(roots_fsolve))
roots_bisect = scipy.optimize.bisect(f, a, b)
print("bisect:", roots_bisect, "f(root):", f(roots_bisect))
roots_newton = scipy.optimize.newton(f, X0)
print("newton:", roots_newton, "f(root):", f(roots_newton))
