def isfloat(value):
    """Функция проверки на действительное число."""

    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


def func_sum(input_list):
    """Функция подсчета суммы введенных чисел.

    Возвращает сумму введенных чисел (list_sum: float)
    и маркер состояния (status: boolean) - указывает на наличие
    в обрабатываемой строке нечисловых данных.
    """
    status = True
    list_sum = 0
    for el in input_list:
        if isfloat(el):
            list_sum += float(el)
        elif el != "q":
            status = False
    return list_sum, status


sum_input = 0
while True:
    s = input().split()
    str_sum, mode = func_sum(s)
    sum_input += str_sum
    print(f"{str_sum} ({sum_input})")
    if not mode:
        print("Err")
    if 'q' in s:
        print(f"Сумма введенных чисел равна {sum_input}. Заканчиваем подсчет, пора и честь знать.")
        break
