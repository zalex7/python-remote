class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}


class Position(Worker):
    def __init__(self, n, s, p, w, b):
        super().__init__(n, s, p, w, b)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


person = Position("Ivan", "Ivanov", "Manager", 50000, 10000)
print(person.get_full_name(), person.get_total_income())
