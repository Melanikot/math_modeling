import numpy as np
m = int(input('Введите количество строк в массиве: '))
n = int(input('Введите количество столбцов в массиве: '))
a = np.zeros((m, n))
for i in range(0, m, 1):
    for j in range(0, n, 1):
        a[i, j] = float(input(f'Введите число {i + 1} строки {j + 1} столбца: '))
for y in range(0, n, 1):
    for x in range(1, m, 1):