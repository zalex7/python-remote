class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __str__(self):
        return f"({self.real}+{self.imaginary}j)"


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(3, 7)
print(c1 + c2)
print(c1 * c2)
