a = int(input('Введите натуральное число: '))
if a <= 0:
    print('Ошибка')
else:
    b = []
    for i in range(1, a + 1, 1):
        if a % i == 0:
            b.append(i)
    print(b)
    if b[1] == a:
        print('a =', a)
    else:
        for x in range


    