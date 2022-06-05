class Matrix:
    def __init__(self, list0):
        self.list0 = list0

    def __add__(self, other):
        try:
            matr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            for i in range(len(self.list0)):
                for j in range(len(self.list0[i])):
                    matr[i][j] = self.list0[i][j] + other.list0[i][j]

            return Matrix(matr)
        except IndexError:
            print('Проверьте, что матрицы одинаковые по размеру.')

    def __str__(self):
        res = ''
        for i in range(len(self.list0)):
            res += f'{" ".join(map(str, self.list0[i]))}\n'
            i += 1
        return res


my_matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_matr1)
my_matr2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])  # работает
print(my_matr1 + my_matr2)

my_matr3 = Matrix([[0, 0], [0, 0, 0]])  # генерация исключения
print(my_matr2 + my_matr3)
