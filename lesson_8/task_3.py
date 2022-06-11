class NotNumber(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"'{self.value}' is invalid input, the program can only accept integers and floats as its values"


class CustomInput:
    custom_list = []

    def __init__(self, value=None):
        if value is None or value == []:
            self.custom_list = []
        elif not isinstance(value, (int, float)):
            raise NotNumber(value)
        else:
            self.custom_list.append(value)

    def set_element(self, value):
        try:
            self.custom_list.append(float(value)) if "." in value else self.custom_list.append(int(value))
        except ValueError:
            raise NotNumber(value)


my_list = CustomInput()
while True:
    el = input("Input next element or 'stop' for quit: ")
    if el.lower() == "stop":
        break
    else:
        try:
            my_list.set_element(el)
        except NotNumber as err:
            print(err)

print()
print("Here is your list:")
print(my_list.custom_list)
