import numpy as np
import lab_3_osn_task1 as ot1
g = ot1.g
x0 = int(input('Введите х0: '))
y0 = int(input('Введите y0: '))
v0 = int(input('Введите v0: '))
t = [0, 1, 2, 3, 4, 5]
b = []
c = []
for t in range(0, 5, 1):
    x = x0 + v0 * t
    b.append(x)
    y = y0 + v0 * t - g * t ** 2 / 2
    c.append(y)
print(t + b + c)