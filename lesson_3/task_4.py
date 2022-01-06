def my_func(x, y):
    if x > 0:
        if (y - int(y) == 0) and (y < 0):
            xx = 1
            for i in range(abs(y)):
                xx *= x
            return round(1 / xx, 5)
    print("Некорректные значения аргументов")
    return


x = 2
y = -3
print(f"{x} в степени {y} равно {my_func(x, y)}.")
