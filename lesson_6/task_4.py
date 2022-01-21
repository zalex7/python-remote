from random import randint, choice


class Car:
    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        print("The car is going.")

    def stop(self):
        print("The car is stopped.")

    def turn(self, direction):
        print(f"The car turns {direction}" if direction in ["left", "right"] else f"The car go {direction}")

    def show_speed(self):
        print(f"The car is moving at a speed of {self.speed} km/h.")


class TownCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f"The car is moving at a speed of {self.speed} km/h." if self.speed < 60 else
              f"Current car speed - {self.speed} km/h - exceeds the speed limit!!!")


class WorkCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f"The car is moving at a speed of {self.speed} km/h." if self.speed < 40 else
              f"Current car speed - {self.speed} km/h - exceeds the speed limit!!!")


class SportCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f"The car is moving at a speed of {self.speed} km/h." if self.speed < 200 else
              f"Current car speed - {self.speed} km/h - exceeds the speed limit!!!")


class PoliceCar(Car):
    def __init__(self, s, c, n, p):
        super().__init__(s, c, n, p)

    def show_speed(self):
        print(f"The car is moving at the right speed!")


car_1 = TownCar(randint(10, 100), "black", "Mercedes", True)
car_2 = WorkCar(randint(10, 100), "green", "UAZ", True)
car_3 = SportCar(randint(100, 300), "white", "Lada", True)
car_4 = PoliceCar(randint(0, 300), "blue", "Ford", True)

route = ["left", "right", "forward"]

# The trip of the first car
print(car_1.name, car_1.color, car_1.speed, car_1.is_police)
car_1.go()
car_1.show_speed()
for _ in range(randint(5, 20)): car_1.turn(choice(route))
car_1.stop()
print()

# The trip of the second car
print(car_2.name, car_2.color, car_2.speed, car_2.is_police)
car_2.go()
car_2.show_speed()
for _ in range(randint(5, 20)): car_2.turn(choice(route))
car_2.stop()
print()

# The trip of the third car
print(car_3.name, car_3.color, car_3.speed, car_3.is_police)
car_3.go()
car_3.show_speed()
for _ in range(randint(5, 20)): car_3.turn(choice(route))
car_3.stop()
print()

# The trip of the fourth car
print(car_4.name, car_4.color, car_4.speed, car_4.is_police)
car_4.go()
car_4.show_speed()
for _ in range(randint(5, 20)): car_4.turn(choice(route))
car_4.stop()
