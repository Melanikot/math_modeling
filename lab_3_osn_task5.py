import lab_3_osn_task4 as ot4
from lab_3_osn_task4 import a, n, m
if m == 1:
    print(a)
else:
    for i in range(0, n, 1):
        x = a[i, 0]
        a[i, 0] = a[i, 1]
        a[i, 1] = x
    print(a)