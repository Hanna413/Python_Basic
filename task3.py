class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(' '.join([self.name, self.surname]))

    def get_total_income(self):
        print(f'Total income is {self.wage + self.bonus}')


biologist = Position('John', 'Johnson', 'biologist', 2000, 1000)
print(vars(biologist))
biologist.get_full_name()
biologist.get_total_income()
