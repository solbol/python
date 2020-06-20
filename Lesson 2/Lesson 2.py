# # 1
# my_list = ['list item', 547, True, [124, 'sub item']]
# for a in my_list:
#     print(type(a))
#
# # 2
# user_list = []
#
# while True:
#     input_value = input('Введите значение (для прекращения введите *): ')
#     if input_value == '*':
#         break
#     user_list.append(input_value)
#
# print(user_list)
#
# index = 0
#
# while True:
#     if index > len(user_list) / 2:
#         break
#     # value1 = user_list[a * 2]
#     # value2 = user_list[a * 2 + 1]
#     user_list.insert(index * 2 + 1, user_list.pop(index * 2))
#     index += 1
#
# print(user_list)
#
# # 3
# number_of_month = int(input('Введите месяц числом: '))
#
# # list
# list_winter = [12, 1, 2]
# list_spring = [3, 4, 5]
# list_summer = [6, 7, 8]
# list_autumn = [9, 10, 11]
#
# if number_of_month in list_winter:
#     print('Зима')
# elif number_of_month in list_spring:
#     print('Весна')
# elif number_of_month in list_summer:
#     print('Лето')
# elif number_of_month in list_autumn:
#     print('Осень')
# else: print('Введён неверный месяц')
#
# # dict
# my_dict = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
#
# if number_of_month > 12:
#     print('Введён неверный месяц')
# else: print(my_dict.get(number_of_month))
#
# # 4
# phrase = input('Введите набор слов: ')
#
# for ind, word in enumerate(phrase.split(), 1):
#     print(ind, word[:10])
#
# # 5
# my_list = [7, 5, 3, 3, 2]
#
# my_list.append(int(input('Введите число: ')))
# my_list.sort(reverse = True)
#
# print(my_list)
#
# # 6
# products = []
#
# number_of_product = 0
#
# while True:
# 
#     product_name     = input('Введите название товара: ')
#     product_price    = input('Введите цену товара: ')
#     product_quantity = input('Введите количество товара: ')
#     product_unit     = input('Введите единицу измерения товара: ')
#
#     number_of_product += 1
#
#     products.append((number_of_product, {'название': product_name, 'цена': int(product_price), 'количество': int(product_quantity), 'ед.': product_unit}))
#
#     if input('Чтобы ввести ещё один товар, нажмите любую клавишу, чтобы закончить, нажмите * ') == '*':
#         break
#
# print(products)
#
# list_name     = []
# list_price    = []
# list_quantity = []
# list_unit     = []
#
# for el in products:
#     list_name    .append(el[1].get('название'))
#     list_price   .append(el[1].get('цена'))
#     list_quantity.append(el[1].get('количество'))
#     list_unit    .append(el[1].get('ед.'))
#
# analytics_of_products = {'название': list_name, 'цена': list_price, 'количество': list_quantity, 'ед.': list_unit}
#
# print(analytics_of_products)