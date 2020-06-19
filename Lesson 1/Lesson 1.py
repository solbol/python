# # 1
# perem_1 = 123
# perem_2 = 'asdf'
# print(perem_1)
# print(perem_2)
#
# # 2
# time_ss = int(input('Введите время в секундах: '))
#
# '''
# time_h = time_ss // (60 * 60)
# time_m = (time_ss - time_h * 60 * 60) // 60
# time_s = time_ss - time_h * 60 * 60 - time_m * 60
# '''
#
# time_h = int(time_ss / (60 * 60))
# time_m = int((time_ss - time_h * 60 * 60) / 60)
# time_s = time_ss - time_h * 60 * 60 - time_m * 60
#
# time_str = str(time_h) + ':' + str(time_m) + ':' + str(time_s)
# print(time_str)
#
# # 3
# number_n = str(input('Введите число: '))
#
# number_nn  = int(number_n + number_n)
# number_nnn = int(number_n + number_n + number_n)
# number_n   = int(number_n)
#
# print(number_n + number_nn + number_nnn)
#
# # 4
# number = str(input('Введите число: '))
#
# max_number = 0
#
# number_length = len(number)
# current_character = 0
#
# while current_character <= number_length - 1:
#     current_numeral = int(number[current_character])
#     max_number = max(max_number, current_numeral)
#     current_character += 1
#
# print(max_number)
#
# # 5
# revenue = int(input('Введите сумму выручки: '))
# costs   = int(input('Введите сумму издержек: '))
#
# profitability = 0
#
# if revenue > costs:
#     profitability = (revenue - costs) / revenue * 100
#     massage = 'Вы отработали с прибылью: ' + str(revenue - costs)
# elif revenue < costs:
#     massage = 'Вы отработали с убытком: ' + str(costs - revenue)
# else: massage = 'Вы отработали в ноль'
#
# print(massage)
#
# if profitability > 0:
#     print(f'Ваша рентабельность: {int(profitability)}%')
#
# # 6
# first_day_km = int(input('Введите количество километров в первый день: '))
# target_result = int(input('Введите целевой результат в километрах: '))
#
# target_day = 1
#
# while first_day_km < target_result:
#     first_day_km = first_day_km * 1.1
#     target_day += 1
#
# print(f'День достигнутого результата: {target_day}')