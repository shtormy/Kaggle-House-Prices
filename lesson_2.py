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

month_dict = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август',9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12:'декабрь' }
seasons = {'зиме': [12, 1, 2], 'весне': [3, 4, 5], 'лету': [6, 7, 8], 'осени': [9, 10, 11]}
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month in month_dict:
    print(f'Вы ввели {month} - это {month_dict[month]}')
else:
    print('Введите корректные данные в виде целого числа от 1 до 12')
if month in sum(seasons.values(),[]):
    for i in seasons.items():
        if month in i[1]:
            print(f'Этот месяц относится к {i[0]}')
            break
#Не поняла как сделать тоже со списками и как месяца вставить в сезоны
#month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
#month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#season_list = ['зима', 'весна', 'лето', 'осень']
#if month in month_list:
    #print(f'{month} - {month_list[month-1]}')
#else:
    #print('Введите корректные данные')

#4

user_str = input('Введите слова через пробел: ').split()

for n, i in enumerate(user_str, 1):
    print(f'{n} {i:.10}')

#5

#Без разбора ДЗ сама не додумалась, у меня была только i, запуталась в i и n
my_list = [7, 5, 3, 3, 2]
i = 0       #перебор от 0
number = int(input('Введите число: '))
for n in my_list:      #n это элемент списка
    if number <= n:
        i += 1
    else:
        break
my_list.insert(i, number)
print(my_list)

#6

products = []
i = 0

while i <= 2: # ввод только 3 видов товара
    i += 1
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    sum = int(input('Введите кол-во товара: '))
    unit = input('Введите еденицы измерения товара: ')
    products.append((i, {'name': name, 'price': price, 'sum': sum, 'unit': unit}))
print(products)
my_dict = {'name': name, 'price': price, 'sum': sum, 'unit': unit}
for key, value in my_dict.items():
    print(f'{key}:{value}') #выводит только последний товар!!!!

#по разбору ДЗ на уроке, повторила

#products = []
#my_dict = {'название': '', 'цена': '', 'количество': '', 'еденица измерения': '', }
#analitics = {'название': [], 'цена': [], 'количество': [], 'еденица измерения': [], }
#number_product = 0
#while number_product <= 2:
    #number_product += 1
    #copy_my_dict = my_dict.copy()
    #for i in my_dict:
        #my_value = input(f'Введите значение  "{i}": ')
        #copy_my_dict[i] = my_value
        #analitics[i].append(copy_my_dict[i])
        #products.append((number_product, copy_my_dict))
#for key, value in analitics.items():
    #print(f'{key}:{value}')














