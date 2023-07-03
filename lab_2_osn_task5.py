a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
if b == 0:
    print('Oшибка')
else:
    if a % b == 0:
        print('Делится, a / b = ', a / b)
    else:
        print('Не делится, a / b = ', a // b, ' (остаток ', a % b, ')')