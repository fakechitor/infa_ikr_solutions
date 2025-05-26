import numpy as np
# 2x+3y = 8
# 5x+4y = 13
A = [[2,3],[5,4]]
b = [8, 13]
det_A = np.linalg.det(A)
if det_A == 0:
    print("Обратная матрица не существует")
else:
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    print("Решение системы (x, y):", x)