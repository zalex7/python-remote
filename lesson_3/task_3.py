def my_func(arg_1, arg_2, arg_3):
    if arg_1 > arg_2:
        if arg_2 > arg_3:
            return arg_1 + arg_2
        else:
            return arg_1 + arg_3
    else:
        if arg_1 > arg_3:
            return arg_2 + arg_1
        else:
            return arg_2 + arg_3


print(my_func(1, 2, 3))
