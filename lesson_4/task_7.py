def fact(n):
    f = 1
    for i in range(n + 1):
        if i == 0:
            yield 1
        else:
            f *= i
            yield f


try:
    number = int(input("Please enter an integer: "))
except ValueError as message:
    print(message)
else:
    for i, el in zip(range(number + 1), fact(number)):
        print(f"The factorial of {i} is {el}.")
