from math import factorial


def fact(border):
    for el in range(1, border + 1):
        yield factorial(el)


border = int(input('Введите границу факторила: '))

for el in fact(border):
    print(el)