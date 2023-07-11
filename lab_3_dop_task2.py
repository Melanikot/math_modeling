import numpy as np
a = np.zeros((1, 5))
for i in range(0, 4, 1):
    a[0, i] = int(input(f'Введите значение {i + 1}-го элемента: '))
b = int(input('Введите число: '))
c = int(input('Введите номер позиции: '))
for j in range(c, 4, 1):
    a[0, j] = a[0, j - 1]
a[0, 4] = a[0, 3]
a[0, c - 1] = b
print(a)