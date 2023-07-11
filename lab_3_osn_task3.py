import numpy as np
import lab_3_osn_task1 as ot1
g = ot1.g
x0 = int(input('Введите х0: '))
y0 = int(input('Введите y0: '))
v0x = int(input('Введите v0x: '))
v0y = float(input('Введите v0y: '))
t = np.arange(0, 5, 1)
x = x0 + v0x * t
y = y0 + v0y * t - g * t ** 2 / 2 
a = np.zeros((len(t), 3))
print(a)
for i in range(len(t)):
    a[i, 0] = t[i]
    a[i, 1] = x[i]
    a[i, 2] = y[i]