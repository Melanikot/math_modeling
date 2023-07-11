import numpy as np
a = np.zeros((4, 3))
b = np.zeros((4, 3))
c = np.zeros((4, 3))
for i in range(0, 4, 1):
    for j in range(0, 3, 1):
        a[i, j] = float(input(f'Введите число для {i + 1} строки {j + 1} столбца первого массива: '))
        b[i, j] = float(input(f'Введите число для {i + 1} строки {j + 1} столбца второго массива: '))
        if a[i, j] > b[i, j]:
            c[i, j] = a[i, j]
        else: c[i, j] = b[i, j]
print(c)