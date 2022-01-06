def div_two_args(arg_1, arg_2):
    """Возвращает результат деления двух чисел"""
    try:
        div = arg_1 / arg_2
    except ZeroDivisionError as f:
        print(f)
        return
    else:
        return div


def input_number(number_index):
    """Запрашивает у пользователя число и проверяет корректность ввода

    number_index - порядковый номер вводимого числа
    """
    while True:
        num = input(f"Введите число {number_index}: ")
        try:
            num = float(num)
        except ValueError as f:
            print(f)
        else:
            return num


num1 = input_number(1)
num2 = input_number(2)
print(f"Результат деления {num1} на {num2}:", round(div_two_args(num1, num2), 4))
