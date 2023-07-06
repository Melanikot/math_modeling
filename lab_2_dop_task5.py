a = int(input('Введите натуральное число: '))
if a <= 0:
    print('Ошибка')
else:
    b = []
    c = 0
    g = []
    for y in range(1, a + 1, 1):
        print(f'Зашли сюда {y}')
        for i in range(1, y, 1):
            print(f'Зашли сюда {i}')
            if y % i == 0:
                b.append(i)
                print(f'Зашли сюда {b}')
        for x in b:
            c += x
            print(f'Зашли сюда {c}')
        if c == y:
            g.append(y)
    print(g)
    