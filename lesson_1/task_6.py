day_res = int(input("Введите результат в первый день, км: "))
result = int(input("Введите требуемый результат, км: "))
day = 1
while day_res < result:
    day += 1
    day_res += day_res * 0.1
print(f"Результат будет достигнут на {day} день.")