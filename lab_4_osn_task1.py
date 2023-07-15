import numpy as np
n = int(input('Введите число элементов в массиве: '))
a = np.zeros((1, n))
print(a)
for i in range(0, n, 1):
    a[0, i] = int(input(f'Введите {i + 1} элемент массива: '))
def func(a, b=0):
    for j in range(0, n, 1):
        b += a[0, j]
    c = b / n
    return c
print(func(a))