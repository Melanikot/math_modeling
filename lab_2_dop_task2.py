a = float(input('Введите значение стороны а: '))
b = float(input('Введите значение стороны b: '))
c = float(input('Введите значение стороны c: '))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or b == c or a == c:
            print('Треугольник равнобедреннй')
        else:
            print('Треугольник разносторонний')
    else:
        print('Такого треугольника не существует')
else:
    print('Такого треугольника не существует')