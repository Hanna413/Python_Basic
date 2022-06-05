from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def size(self):  # размер v для пальто или рост h для костюма
        pass

    @abstractmethod
    def _calc_tissue_required(self):  # для расчета ткани
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name, size):
        self.name = name
        self._size = size
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):  # если в потомках не будет написана формула
        raise NotImplemented

    @property
    def tissue_required(self):
        if not self._tissue_required:
            self._calc_tissue_required()  # кэширование

        return self._tissue_required

    @property
    def size(self):
        return self._size

    @size.setter         # новый размер
    def size(self, size):
        self._size = size
        self._tissue_required = None  # сброс старого расчета

    @property
    def total_tissue_required(self):
        total_tissue = round(sum([item.tissue_required for item in self._clothes]), 2)
        return f'Всего для костюма и пальто надо {total_tissue} м ткани'


class Coat(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(self.size / 6.5 + 0.5, 2)

    @property
    def v(self):
        return self.size

    @v.setter
    def v(self, size):
        self.size = size

    def __str__(self):
        return f"Для пошива пальто {self.size} размера требуется {self.tissue_required} м ткани"


class Suit(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.size * 0.01 + 0.3, 2)

    @property
    def h(self):
        return self.size

    @h.setter
    def h(self, height):
        self.size = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.size} см требуется {self.tissue_required} м ткани"


coat = Coat('Пальто', 10)
print(coat)
coat.v = 12
print(coat)
suit = Suit('Костюм', 178)
print(suit)
suit.h = 170
print(suit)

print(coat.total_tissue_required)
