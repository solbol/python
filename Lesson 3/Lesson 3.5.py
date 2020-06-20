def my_func(my_sum, user_numbers):
    sum_list = user_numbers.split()
    for el in sum_list:
        if el == '*':
            return my_sum, True
        my_sum += int(el)
    return my_sum, False


my_sum = 0

while True:
    user_numbers = input('Введите числа через пробел (для окончания введите *): ')
    my_sum, interrupt_status = my_func(my_sum, user_numbers)
    print(my_sum)
    if interrupt_status:
        break