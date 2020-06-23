from random import randint
import functools

random_list = [randint(0, 100) for i in range(randint(10, 20))]

print(random_list)

new_list = []

current_number = random_list[0]

for el in random_list[1:]:
    if el > current_number:
        new_list.append(el)
    current_number = el

print(new_list)