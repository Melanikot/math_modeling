import numpy as np
a = np.zeros((4, 3))
b = np.zeros((4, 3))
c = np.zeros((4, 3))
for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        a[i, j] = float(input('Введие число для первого массива: '))
        b[i, j] = float(input('Введите число для второго массива: '))
        if a[i, j] > b[i, j]:
            c[i, j] = a[i, j]
        else: c[i, j] = b[i, j]
print(c)