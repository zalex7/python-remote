class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w
        self._weight = 25
        self._thickness = 5

    def calc_weight(self):
        return f"Asphalt mass is {round(self._length * self._width * self._weight * self._thickness / 1000, 2)} ton."


dor1 = Road(float(input("Enter the length of the road section, m: ")),
            float(input("Enter the width of the road section, m: ")))
print(dor1.calc_weight())
