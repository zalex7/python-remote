from functools import reduce


def my_func(el_1, el_2):
    return el_1 * el_2


print(reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))
