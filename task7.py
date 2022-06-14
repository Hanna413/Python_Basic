class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        if self.b < 0 or other.b < 0:
            return ComplexNumber((self.a * other.a) + abs(self.b * other.b), (self.a * other.b) + (self.b * other.a))
        else:
            return ComplexNumber((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))

    def __str__(self):
        if self.b < 0:
            return f'{self.a} {self.b} * j'
        else:
            return f'{self.a} + {self.b} * j'


d1 = ComplexNumber(2, 3)
print(d1)
d2 = ComplexNumber(1, -5)
print(d1 + d2)
