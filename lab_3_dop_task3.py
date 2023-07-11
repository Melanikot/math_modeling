import numpy as np
m = int(input('Введите количество строк в массиве: '))
n = int(input('Введите количество столбцов в массиве: '))
a = np.zeros((m, n))
for i in range(0, m, 1):
    for j in range(0, n, 1):
        a[i, j] = float(input(f'Введите число {i + 1} строки {j + 1} столбца: '))
print(a)
for y in range(0, n, 1):
    for x in range(0, m, 1):
        if a[0, y] > a[1, y]:
            b = a[0, y]
        elif a[x, y] > a[x - 1, y - 1]:
            b = a[x, y]
    print(b)