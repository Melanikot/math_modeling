a = int(input('Введите число: '))
b = str(a)
for i in range(len(b), 0, -1):
        print(b[i-1], end='')
print()
