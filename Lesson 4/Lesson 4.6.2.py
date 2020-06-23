from sys import argv
from itertools import cycle

my_list = []

с = 0
for el in cycle(argv[1:]):
    if с > 10:
        break
    my_list.append(el)
    с += 1

print(my_list)