class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __str__(self):
        return str(self.cell_count)

    def __add__(self, new_cell):
        return Cell(self.cell_count + new_cell.cell_count)

    def __sub__(self, new_cell):
        if self.cell_count >= new_cell.cell_count:
            return Cell(self.cell_count - new_cell.cell_count)
        else:
            print('Ошибка вычитания клетки: клетка 2 больше клетки 1')
            return Cell(0)

    def __mul__(self, new_cell):
        return Cell(self.cell_count * new_cell.cell_count)

    def __truediv__(self, new_cell):
        return Cell(int(self.cell_count / new_cell.cell_count))

    def make_order(self, row):
        str_cell = ''.join(['*' for i in range(row)]) + '\n'
        str_cell = ''.join([str_cell for i in range(self.cell_count // row)])
        str_cell = str_cell + ''.join(['*' for i in range(self.cell_count % row)])
        return str_cell

cell1 = Cell(10)
cell2 = Cell(15)
cell3 = Cell(20)

print(cell1 + cell2 + cell3)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell1 * cell2 * cell3)
print(cell2 / cell1)

print(cell3.make_order(6))