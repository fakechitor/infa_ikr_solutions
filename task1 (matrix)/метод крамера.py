import numpy as np
# 3x+2y=5
# 1x+4y=6
A = np.array([[3,2],[1,4]])
b = np.array([5,6])
A_det = np.linalg.det(A)
if A_det == 0:
    print("Метод Крамера нельзя применить")
else:
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        x[i] = det_Ai / A_det
    print("Решение системы методом Крамера:", x)
