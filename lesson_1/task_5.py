revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))
if revenue > costs:
    print("Фирма работает с прибылью")
    rent = (revenue - costs) / costs * 100
    print("Рентабельность:", rent, "%")
    staff = int(input("Введите численность сотрудников фирмы:"))
    print("Прибыль фирмы в расчете на одного сотрудника:", (revenue - costs) / staff)
elif revenue < costs:
    print("Фирма работает с убытком")
else:
    print("Фирма работает без прибыли и без убытка")
