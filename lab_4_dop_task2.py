import numpy as np
n = int(input('Введите число: '))
if n > 0:
    a = np.zeros((1, n))
else:
    a = np.zeros((1, -n))
a[0, 0]= 0
a[0, 1] = 1
def fib(n):
    if n > 0:
        for i in range(2, n, 1):
            a[0, i] = a[0, i - 1] + a[0, i - 2]
        b = a[0, n - 1]
    else:
        for i in range(2, -n, 1):
            a[0, i] = a[0, i - 2] - a[0, i - 1]
        b = a[0, -n - 1]
    return b
print(f'{n}-е число Фибоначчи:',fib(n))