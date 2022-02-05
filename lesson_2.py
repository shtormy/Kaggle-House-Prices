# Попова Светлана
# ДЗ №2 к уроку №2

# 1

my_list = ['abc', 3, True, 88, 'sos', 7.85, [1, 2]]
for i in my_list:
    print(type(i))

# 2

number = input('Введите цифры: ')
list_1 = [int(a) for a in str(number)] #делаем список из введенных цифр
print(list_1)
for i in range(0, len(list_1)-1, 2): #перебираем список с шагом 2
    list_1[i], list_1[i+1] = list_1[i+1], list_1[i] #меняем цифры местами
print(list_1)

#3
#Не поняла как месяца вставить в сезоны
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
seson_list = ['зима', 'весна', 'лето', 'осень']
if month in month_list:
    print(f'{month} - {month_list[month-1]}')
else:
    print('Введите корректные данные')

#Со словарем не смогла даже алгоритм придумать
#seson_dict = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}
#month_dict = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август',9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12:'декабрь' }

#if month in month_dict:
    #print(f'Вы ввели {month} - это {month_dict[month]}')
#else:
    #print('Введите корректные данные в виде целого числа от 1 до 12')

#4

user_str = input('Введите слова через пробел: ').split()

for n, i in enumerate(user_str, 1):
    print(f'{n} {i:.10}')

#5

#Зачем нужны две переменные i и n? Как понять, что нужно использовать две переменные?
#Я сравниваю введенное число со списком и ввожу его в список, если оно <=  элемента списка - n
my_list = [7, 5, 3, 3, 2]
i = 0       #зачем нужна вспомогательная переменная?
number = int(input('Введите число: '))
for n in my_list:      #n это элемент списка
    if number <= n:
        i += 1
    else:
        break
my_list.insert(i, number) #почему i, а не n?
print(my_list)

#6

products = []
i = 0
while i <= 1:
    i += 1
    name = input('\n Введите название товара: ')
    price = int(input('Введите цену товара: '))
    sum = int(input('Введите кол-во товара: '))
    unit = input('Введите еденицы измерения товара: ')

    products.append((i, {'name': name, 'price': price, 'sum': sum, 'unit': unit}))
print(products)
#for i in range(0, len(products), 2: #не знаю как такой список разбить на отдельные товары c новой строки
    #print(products)

#как список преобразовать в словарь? Запуталась в индексах
#my_dict = {products[i][0] : products[i][1]}
#for i in products:
    #print(my_dict)

















