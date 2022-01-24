from random import random, randint


class Matrix:
    def __init__(self, matrix):
        check_list = [(len(el), type(i)) if isinstance(el, list) else (0, type(el)) for el in matrix for i in el]
        if all(True if (el[0] == check_list[0][0]) and (el[1] in (int, float)) else False for el in check_list):
            self.matrix = matrix
            self.len_row = len(matrix)
            self.len_col = check_list[0][0]
        else:
            raise ValueError("Incorrect input data!")

    def __str__(self):
        max_digits = max(len(str(round(el, 4))) for el in sum(self.matrix, []))
        return '\n'.join('\t'.join([f'{round(el[j], 4): {max_digits}}'
                                    for j in range(self.len_col)]) for el in self.matrix)

    def __add__(self, other):
        if self.len_row == other.len_row and self.len_col == other.len_col:
            return Matrix([
                [self.matrix[i][j] + other.matrix[i][j] for j in range(self.len_col)] for i in range(self.len_row)])
        else:
            raise ValueError("The dimensions of the matrices do not match!")


# Оптимизировал код для "красивого" вывода и для float, и для int

matrix1 = Matrix([[random() * 1000 for _ in range(5)] for _ in range(10)])
print(matrix1)
print()
matrix2 = Matrix([[random() * 1000 for _ in range(5)] for _ in range(10)])
print(matrix2)
print()
print(matrix1 + matrix2)
matrix3 = Matrix([[randint(-10000, 10000) for _ in range(5)] for _ in range(10)])
print(matrix3)
print()
matrix4 = Matrix([[randint(-10000, 10000) for _ in range(5)] for _ in range(10)])
print(matrix4)
print()
print(matrix3 + matrix4)
