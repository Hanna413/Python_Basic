class Cell:
    def __init__(self, number):
        self._number = number

    def __add__(self, other: 'Cell'):
        return Cell(self._number + other._number)

    def __sub__(self, other: 'Cell'):
        if self._number > other._number:
            return Cell(self._number - other._number)
        elif self._number == other._number:
            return 'Клетки уничтожили друг друга.'
        else:
            return 'Из меньшей клетки нельзя вычесть большую.'

    def __mul__(self, other: 'Cell'):
        return Cell(self._number * other._number)

    def __floordiv__(self, other: 'Cell'):
        return Cell(self._number // other._number)

    def __str__(self):
        return f"Клетка состоит из {self._number} ячеек."

    def make_order(self, per_row):
        if not isinstance(self, str):
            rows, tail = self._number // per_row, self._number % per_row
            return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))
        else:
            return 'Клетки не получилось'


cell_1 = Cell(16)
print(cell_1.make_order(5))
cell_2 = Cell(10)
print(cell_1 - cell_2)
print((cell_1 - cell_2).make_order(3))
