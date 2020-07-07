class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for el in self.matrix:
            str_matrix += str(el) + '\n'
        return str_matrix

    def __add__(self, other):
        new_matrix = Matrix(self.matrix)
        new_matrix.matrix.extend(other.matrix)
        return new_matrix


matrix1 = Matrix([[1, 2, 3]])
matrix2 = Matrix([[4, 5]])

print(matrix1 + matrix2)