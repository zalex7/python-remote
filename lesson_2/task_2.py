my_list = []
while True:
    el = input("Введите следующий элемент списка или stop для завершения ввода: ")
    if el.lower() == "stop":
        break
    else:
        my_list.append(el)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print()
print("Результат обработки:")
print(my_list)
