class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Рисуем ручкой {self.title}")


class Pencil(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Рисуем карандашом {self.title}")


class Handle(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Рисуем маркером {self.title}")


p = Pen("Bic")
p.draw()
ps = Pencil("Koh-i-Noor")
ps.draw()
h = Handle("Xsg")
h.draw()
