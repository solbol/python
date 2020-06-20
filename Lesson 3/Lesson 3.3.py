def my_func(*args):
    return sum(args) - min(args)

print(my_func(5, 7, 2))