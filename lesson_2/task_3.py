while True:
    month = input("Введите месяц (1 - 12): ")
    if month.isdigit():
        month = int(month)
        if (month >= 1) and (month <= 12):
            break
        else:
            print("Вы ввели некорректное значение!")
    else:
        print("Вы ввели не целое число!")
periods = {"Зиму": [1, 2, 12],
           "Весну": [3, 4, 5],
           "Лето": [6, 7, 8],
           "Осень": [9, 10, 11],
           }
for period, months in periods.items():
    if month in months:
        print(f"Введенный месяц приходится на {period}.")
        break
