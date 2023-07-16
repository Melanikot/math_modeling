import numpy as np
a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
N = int(input('Введите значение N: '))
c = (b - a) / (N + 1)
y = np.zeros((1, N))
x = np.arange(a + c, b, c)
def f(a, b, N, d=0):
    for i in x :
        y[0, d] = i ** 2
        d += 1
    return y
print('Значения у:', f(a, b, N))