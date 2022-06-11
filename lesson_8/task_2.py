class DivByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    if b == 0:
        raise DivByZero("division by zero is not allowed!")
    else:
        return a / b


try:
    a = int(input("input a: "))
    b = int(input("input b: "))
except ValueError as err:
    print(err)
else:
    c = div(a, b)
