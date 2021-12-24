h1 = "Обработка переменных"
h2_1 = "Операция умножения"
h2_2 = "Операция деления"
h2_3 = "Объединение строк"

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
name = input("Ваше имя: ")
surname = input("Ваша фамилия: ")

print(h1)
print(h2_1)
print(f"{number_1} * {number_2} =", number_1 * number_2)

print(h2_2)
print(f"{number_1} / {number_2} =", number_1 / number_2)

print(h2_3)
print("Вас зовут:", name + " " + surname)
