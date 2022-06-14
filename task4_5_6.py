class Storage:
    def __init__(self):
        self._present = {}

    @classmethod
    def checking(cls, quantity):
        try:
            if not isinstance(quantity, int):
                raise ValueError
        except ValueError:
            print('Должно быть число.')
        else:
            return quantity

    def add_to(self, name, quantity):
        Storage.checking(quantity)

        self._present[name.name] = quantity

    def move(self, name, quantity, other):
        Storage.checking(quantity)
        try:
            try:
                self._present[name.name] -= quantity
            except KeyError:
                print('Вы не добавляли это.')
        except TypeError:
            print('опять ошибка, проверьте правильность данных')
        other.add_to(name, quantity)

    @property
    def show_present(self):
        return self._present


class Tech:
    def __init__(self, name, serial):
        self.name = name  # имя например hp-123
        self.serial = serial  # серийник например 111111
        # self.quantity = quantity  # сколько вообще в наличии
        self.group = self.__class__.__name__


class Printer(Tech):
    def __repr__(self):
        return f'{self.name} {self.serial}'

    @staticmethod
    def action():
        return 'Печатает'


class Scaner(Tech):
    def __repr__(self):
        return f'{self.name} {self.serial}'

    @staticmethod
    def action():
        return 'Сканирует'


class Xerox(Tech):
    def __repr__(self):
        return f'{self.name} {self.serial}'

    @staticmethod
    def action():
        return 'Копирует'


printer1 = Printer('hp-123', '111111')
main_store = Storage()
small_store = Storage()
main_store.add_to(printer1, 'abc')
main_store.move(printer1, 2, small_store)
print(main_store.show_present)
print(small_store.show_present)
