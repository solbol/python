def my_func(var_1, var_2):
    if not var_1.isdigit():
        return 'числитель не является числом!'
    if not var_2.isdigit():
        return 'знаменатель не является числом!'
    if int(var_2) == 0:
        return 'деление на ноль!'
    return int(var_1) / int(var_2)


var_1 = input('Введите числитель: ')
var_2 = input('Введите знаменатель: ')

result = my_func(var_1, var_2)

if isinstance(result, str):
    print(f'Ошибка: {result}')
else:
    print(f'Результат деления {result}')