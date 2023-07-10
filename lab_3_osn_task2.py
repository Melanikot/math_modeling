import numpy as np
import lab_3_osn_task1 as ot1
p = ot1.p
g = ot1.g
h = 100
a = p / 3
b = 30
v = np.sqrt((g * h * np.tan(b) ** 2) / (2 * np.cos(a) ** 2 * (1 - np.tan(b) * np.tan(a))))
print(v, 'м/с2')

T = 200
E = 300
k = ot1.k
h = ot1.h
e = ot1.e
N = 2 / np.sqrt(p) * h / ((k * T) ** 3 / 2) * e ** (-e / (k * T)) * e ** (T / 2)
print(N) 
