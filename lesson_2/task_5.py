my_list = [7, 5, 3, 3, 2]
new_values = list(map(int, input("Введите новые значения рейтинга через пробел: ").split()))
for value in new_values:
    if value <= my_list[-1]:
        my_list.append(value)
    else:
        for i in range(len(my_list)):
            if value > my_list[i]:
                my_list.insert(i, value)
                break
print(my_list)
