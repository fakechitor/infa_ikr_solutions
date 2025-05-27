from scipy.optimize import fsolve
from sympy import exp


def f_sist(t):
    x, y = t
    return (exp(-0.2 * x + y) - x * y - 1.4, x ** 2 + 2 * y ** 2 - 4)


print(' X       Y')
print('-' * 15)
x1, y1 = fsolve(f_sist, (-2, 0))
print('%5.2f %6.2f' % (x1, y1))
x2, y2 = fsolve(f_sist, (1, 1))
print('%5.2f %6.2f' % (x2, y2))
x3, y3 = fsolve(f_sist, (1.7, -0.5))
print('%5.2f %6.2f' % (x3, y3))
x4, y4 = fsolve(f_sist, (1, -1))
print('%5.2f %6.2f' % (x4, y4))
