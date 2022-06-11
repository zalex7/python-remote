class Cell:
    def __init__(self, cell):
        if cell > 0:
            self.cell = cell
        else:
            raise ValueError("Incorrect input data!")

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) > 0:
            return Cell(self.cell - other.cell)
        else:
            print("There are no more cells!")
            return Cell(1)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        if (c := self.cell // other.cell) > 0:
            return Cell(c)
        else:
            print("There are no more cells!")
            return Cell(1)

    def make_order(self, quantity):
        s = "*" * self.cell
        return '\n'.join(s[i:i + quantity] for i in range(0, len(s), quantity))


cell1 = Cell(12)
cell2 = Cell(13)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print()
print(cell2.make_order(3))
