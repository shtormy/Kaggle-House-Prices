# Попова Светлана
#Урок №1

#1

print('Привет, как тебя зовут?')
name = input('Введите ваше имя: ')
print(f'Сколько тебе лет, {name}')
age = int(input('Введите ваш возраст: '))
print(f'Чем ты, {name}, любишь заниматься?')
hobby = input('Введите ваше хобби: ')
print(f'Поздравляю! Тебя зовут {name}, тебе {age} года(лет), ты любишь {hobby}.')

#2

seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
second = (seconds - (hours * 3600)) - (minutes * 60)
print('{:02}:{:02}:{:02}'.format(hours, minutes, second))

#3

number = int(input('Введите число: '))
number2 = str(number) + str(number)
number3 = str(number) + str(number) + str(number)
print(number + int(number2) + int(number3))

#4

max_number = numbers % 10 #находим последнюю цифру (остаток при делении)
numbers = numbers//10     #остальные цифры записываем в переменную, без последней, она есть в max_number
while numbers > 0:        #создаем цикл с условием если цифра > 0
    if numbers % 10 > max_number:  # перебираем каждую цифру с пом.остатка от деления с конца
        max_number = numbers % 10  # если цифра соотв.условию, то перезаписываем переменную в max_number
    numbers = numbers//10          # избавляемся от последней цифры
print(max_number)

#5-6

revenue = int(input('Введите данные: выручка предприятия, руб.: '))
costs = int(input('Введите данные: издержки предприятия, руб.: '))
number_of_employees = int(input('Введите данные: численность предприятия, чел.: '))

profit = revenue - costs
loss = costs - revenue

if profit > 0:
    print('Поздравляем! Вы богаты!')
    profitability = profit / revenue * 100
    profit_of_employees = profit // number_of_employees
    print(f'Рентабельность равна {profitability:.2f} %, прибыль на одного сотрудника составляет {profit_of_employees} руб.')
elif loss > 0:
    print('Увы! Идите работать!')

#7

today = int(input('Сколько км. вы сегодня пробежали? Введите число: '))
future = int(input('Сколько км. вы хотите пробежать? Введите число: '))
day = 1
while today < future:
    today = today * 1.1
    day += 1
print(f'На {day} день вы достигните цели!')