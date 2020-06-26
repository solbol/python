from random import randint


my_string = ''

for i in range(randint(5, 15)):
    my_string += str(randint(1, 1000)) + ' '

with open('user_file.txt', 'w') as f:
    f.write(my_string)


with open('user_file.txt') as f:
    my_sum = 0
    for line in f:
        for i in line.split():
            my_sum += int(i)
    print(f'Сумма чисел в файле: {my_sum}')