import numpy as np
import matplotlib.pyplot as plt

X = [1.1, 1.39, 1.68, 1.97, 2.26, 2.54, 2.83, 3.12, 3.41, 3.7]
Y = [0.73, 1.18, 1.75, 2.46, 3.34, 4.41, 5.7, 7.26, 9.15, 11.44]

degree = 3

coeffs = np.polyfit(X, Y , degree)
print("Коэффициенты полинома (от старшей степени к младшей):", coeffs)

plt.scatter(X, Y, color='red', label='Данные')
x_plot = np.linspace(min(X), max(X), 100)
y_plot = np.polyval(coeffs, x_plot)
plt.plot(x_plot, y_plot, label=f'Полином степени {degree}')
plt.legend()
plt.grid(True)
plt.show()
