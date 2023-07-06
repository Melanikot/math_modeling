a = int(input('Введите натуральное число: '))
if a <= 0:
    print('Ошибка')
else:
    b = []
    c = 0
    g = []
    for y in range(1, a + 1, 1):
        for i in range(1, y, 1):
            if y % i == 0:
                b.append(i)
        for x in b:
            c += x
        if c == y:
            g.append(y)
    print(g)
    