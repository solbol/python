from random import randint, choice
from string import ascii_letters


# Подготовим файл (хоть в задании и просили подготовить вручную, но так интересней)
my_string = ''

for i in range(randint(3, 10)):
    for i in range(randint(3, 10)):
        my_string += ''.join(choice(ascii_letters) for a in range(randint(3, 10))) + ' '
    my_string += '\n'

with open('user_file.txt', 'w') as f:
    f.write(my_string)


# Выполним само задание
with open('user_file.txt') as f:
    str_number = 0
    for line in f:
        str_number += 1
        print(f'Количество слов в строке {str_number}: {len(line.split())}')
    f.seek(0)
    print(f'Количество строк в файле: {len(f.readlines())}')