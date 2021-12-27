menu = ["Ввести новый товар", "Вывести аналитику о товарах", "Закончить работу"]
submenu = ["Название", "Цена", "Количество", "Ед."]
products = []
prod_info = {}
while True:
    print("Доступные операции")
    for i in range(len(menu)):
        print(f"{i}: {menu[i]}")
    command = input("Введите команду: ")
    if not command.isdigit():
        print("Введена некорректная команда. Пожалуйста повторите!")
        continue
    else:
        command = int(command)
        if (command < 0) and (command >= len(menu)):
            print("Введена некорректная команда. Пожалуйста повторите!")
            continue
    if command == 2:
        break
    elif command == 1:
        if len(products) == 0:
            print("База товаров пуста, аналитика недоступна.")
            continue
        else:
            for el in submenu:
                inf = []
                for i in range(len(products)):
                    inf.append(products[i][1][el])
                prod_info[el] = inf
            print(prod_info)
    else:
        prod = {}
        for el in submenu:
            s = input(f"{el}: ")
            prod[el] = int(s) if s.isdigit() else s
        products.append((len(products) + 1, prod))
print(products)
