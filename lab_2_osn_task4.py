a = int(input('Введите натуральное число: '))
b = 1
c = 0
d = b + c
i = 2
if a <= 0:
    print('Ошибка')
else:
    print(d)
    while i <= a:
        d += c
        print(d)
        c = b
        b = d
        i += 1