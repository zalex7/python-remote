from sys import argv


def calculation(arg1, arg2, arg3):
    return arg1 * arg2 + arg3


try:
    output_in_hours, rate, prize = argv[1:4]
    output_in_hours = int(output_in_hours)
    rate = int(rate)
    prize = int(prize)
except ValueError:
    print("Script arguments are not correct!")
    print("Use: task_1.py output_in_hours rate prize")
    print("Where output_in_hours, rate, prize are numbers.")
else:
    print(f"Заработная плата сотрудника: {calculation(output_in_hours, rate, prize)} рублей.")
