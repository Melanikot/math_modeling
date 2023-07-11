import math
import numpy as np
n = int(input('Введите количество строк в массиве: '))
m = int(input('Введите количество столбцов в массиве: '))
a = np.zeros((n, m))
for i in range(0, n, 1):
    for j in range(0, m, 1):
        a[i, j] = math.sin(n * (i + 1) + m * (j + 1))
        if a[i, j] < 0:
            a[i, j] = 0
print(a)