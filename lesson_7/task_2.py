from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.__size = size

    def fabric_consumption(self):
        return round(self.__size / 6.5 + 0.5, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if 44 < new_size < 62:
            self.__size = new_size
        else:
            raise ValueError("Incorrect size!")


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.__height = height

    def fabric_consumption(self):
        return round(self.height * 2 / 100 + 0.3, 2)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if 167 <= new_height <= 186:
            self.__height = new_height
        else:
            raise ValueError("Incorrect height!")


my_coat = Coat("HENDERSON", 54)
my_wife_suit = Suit("Victoria Beckham", 167)
print(f"{my_coat.fabric_consumption()} meters of fabric were spent on sewing "
      f"the coat {my_coat.title} with size {my_coat.size}.")
print(f"{my_wife_suit.fabric_consumption()} meters of fabric were spent on sewing "
      f"the suit {my_wife_suit.title} with height {my_wife_suit.height}.")
print(f"Total fabric consumption {round(my_coat.fabric_consumption() + my_wife_suit.fabric_consumption(), 2)} m.")
print()
my_coat.size = 58
print(f"{my_coat.fabric_consumption()} meters of fabric will be spent on sewing "
      f"the coat {my_coat.title} with size {my_coat.size}.")
