from itertools import cycle
from time import sleep


class TrafficLight:
    __color = ["red", "yellow", "green"]
    __colors = {"red": "\033[31m", "yellow": "\033[33m", "green": "\033[32m"}

    def running(self, red_time=7, yellow_time=3, green_time=10):
        times = {"red": red_time, "yellow": yellow_time, "green": green_time}
        if self.__color != ["red", "yellow", "green"]:
            return "TrafficLight is broken!!!"
        for phase in cycle(self.__color):
            print(f"{self.__colors[phase]}Starting {phase} phase!")
            sleep(times[phase])


TrafficLight_1 = TrafficLight()
TrafficLight_1.running(4, 3, 4)
