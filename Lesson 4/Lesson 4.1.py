from sys import argv

first_param, second_param, third_param = argv[1:]

print(f'Зарплата сотрудника равна {int(first_param) * int(second_param) + int(third_param)} руб.')