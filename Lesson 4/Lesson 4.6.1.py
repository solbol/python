from sys import argv
from itertools import count

first_param, second_param = argv[1:]
first_param = int(first_param)
second_param = int(second_param)

first_param = first_param if first_param % 2 == 0 else first_param + 1

my_list = []

for el in count(first_param, 2):
    if el > second_param:
        break
    else:
        my_list.append(el)

print(my_list)