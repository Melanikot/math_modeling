m = int(input('Введите массу тела: '))
v = int(input('Введите скорость тела: '))
h = int(input('Введите высоту полёта: '))
def fly(m, v, h, g):
    E = m * (v ** 2 / 2 + g * h)
    return E
print(fly(m, v, h, g=9.81))