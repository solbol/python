def my_func(x, y):
    z = x
    ind = 1
    while ind < -y:
        ind += 1
        z = z * x
    return 1 / z

print(my_func(5, -3))