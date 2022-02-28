#ДЗ к уроку 8

#1

class Data:
    def __init__(self, my_data):
        self.my_data = my_data

    @classmethod
    def my_data_int(cls, my_data):
        my_date = [i for i in my_data.split() if i != ' ']
        #return int(my_date[0]), int(my_date[1]), int(my_date[2])
        return ':'.join(my_date)

    @staticmethod
    def valid(d, m, y):
         if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2022 >= y >= 0:
                    return f'Вы ввели корретные данные! {d:02}:{m:02}:{y:02}'
                else:
                    return f'Вы ввели неправильный год!'
            else:
                return f'Вы ввели неправильный месяц!'
         else:
            return f'Вы ввели неправильный день!'

    def __str__(self):
        return f'Вы ввели: {Data.my_data_int(self.my_data)}'


#today = Data(input('Введите текущую дату через пробел: '))
today = Data('22 02 2022')
print(today)
print(Data.valid(42, 2, 2022)) #Почему при вводе 02 ошибка: reading zeros in decimal integer literals are not
                                # permitted; use an 0o prefix for octal integers
print(Data.valid(22, 41, 2022))
print(today.valid(22, 2, 2222))

#2

class DivByNull:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def divide_by_null(x, y):
        try:
            return (x / y)
        except:
            return (f"Деление на ноль недопустимо!")


div = DivByNull(10, 100)
print(DivByNull.divide_by_null(10, 0))
print(DivByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

#3

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                num = int(input('Введите число и нажмите Enter: '))
                self.my_list.append(num)
                print(f'Текущий список чисел: {self.my_list} \n ')
            except:
                print(f'Вы ввели недопустимое значение! Введите число!')
                exit = input(f'Попробовать еще раз? Y/N ')

                if exit == 'Y' or exit == 'y':
                    print(try_except.my_input())
                elif exit == 'N' or exit == 'n':
                    return f'Пока!'
                else:
                    return f'Пока!'


try_except = Error(1)
print(try_except.my_input())

#4-5-6

class Store:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Наименование: {self.name} цена: {self.price} количество: {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за ед: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных!'

        print(f'Для выхода нажмите - Q, для продолжения - Enter')
        q = input(f'>>>>>> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: \n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return self.name


class Scanner(Store):
    def to_scan(self):
        return self.name


class Copier(Store):
    def to_copier(self):
        return self.name

total = Store('', 1, 1)
print(total.reception())

#7

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + bj'

    def __add__(self, other):
        print(f'Сумма a и b равна: ')
        return f'z = {self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        print(f'Произведение a и b равно: ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a}j'

    def __str__(self):
        return f'z = {self.a} + {self.b}j'


obj_1 = ComplexNumber(1, -2)
obj_2 = ComplexNumber(3, 4)
print(obj_1)
print(obj_1 + obj_2)
print(obj_1 * obj_2)
