import numpy as np
a = np.zeros((1, 5))
for i in range(0, 5, 1):
    a[0, i] = int(input(f'Введите значение {i + 1}-го элемента: '))
a[0, 4] = 0
print(a)
b = int(input('Введите число: '))
c = int(input('Введите номер позиции: '))
for j in range(4, c - 1, -1):
    a[0, j] = a[0, j - 1]
a[0, c - 1] = b
print(a)