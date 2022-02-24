#ДЗ к уроку 7
#Попова Светлана

#1

class Matrix:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                summa = other.a[i][j] + self.a[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __str__(self):
        self.c = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.a])
        return self.c

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[11, 22, 33], [44, 54, 66], [77, 88, 99]])

print(m1 + m2)
print(m1)

#2

from abc import ABC

class Clothes(ABC):
   pass

class Coat:

    def coat_size(self, v):
        fabric_consumption_coat = round((v / 6.5 + 0.5), 1)
        return fabric_consumption_coat

class Suit:

    def suit_heught(self, h):
        fabric_consumption_suit = round((2 * h + 0.3), 1)
        return fabric_consumption_suit

my_coat = Coat()
print(my_coat.coat_size(5))
my_suit = Suit()
print(my_suit.suit_heught(3))

#3
#не получилось с @property
class Cell:

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        print(f'Сумма')
        return self.cell + other.cell

    def __sub__(self, other):
        print(f'Разность')
        return self.cell - other.cell

    def __mul__(self, other):
        print(f'Умножение')
        return self.cell * other.cell

    def __truediv__(self, other):
        print(f'Деление')
        return round(self.cell / other.cell, 2)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.cell//rows)]) + '\n' + '*' * (self.cell % rows)

cell_1 = Cell(13)
cell_2 = Cell(12)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(7))