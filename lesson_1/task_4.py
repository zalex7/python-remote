number = int(input("Введите целое положительное число: "))
mod = 1
max_figure = 0
while number // mod != 0:
    figure = number // mod % 10
    if figure > max_figure:
        max_figure = figure
    mod *= 10
print("Самая большая цифра в числе:", max_figure)
