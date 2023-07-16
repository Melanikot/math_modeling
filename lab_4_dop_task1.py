a = float(input('Введите основание степени: '))
n = int(input('Введите показатель степени: '))
def f(a, n):
    b = 1
    while n != 0:
        b *= a
        n -= 1
    return b
print('Ответ:', f(a, n))