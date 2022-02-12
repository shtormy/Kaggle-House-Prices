#ДЗ к уроку №4
#Попова Светлана

#1

from sys import argv

_, output, rate, premium = argv

def my_wage():
    total = (int(output) * int(rate)) + int(premium)
    return total


print(my_wage())

#2-1

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list_1 = [num for i, num in enumerate(my_list) if i > 0 and my_list[i] > my_list[i - 1]]

print(new_list_1)

#2-2

new_list_2 = [num1 for num1, num2 in zip(my_list[1:], my_list[:-1]) if num1 > num2]

print(new_list_2)

#3

my_new_list = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]

print(my_new_list)

#4

my_list_3 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list_3 = [num for num in my_list_3 if my_list_3.count(num) == 1]

print(my_new_list_3)

#5

from functools import reduce

def my_func(num1, num2):
    return num1 * num2

new_list = [num for num in range(100, 1001, 2)]


print(reduce(my_func, new_list))

#или

my_new_list = [num for num in range(100, 1001, 2)]

print(reduce(lambda x, y: x * y, my_new_list[:]))

#6

import itertools
for i in itertools.count(10, 5):
    if i == 50:
        break
    else:
        print(i, end=" ")

temp = 0
for i in itertools.cycle('abc'):
    if temp > 10:
        break
    else:
        print(i, end=" ")
        temp = temp+1

#7

#Выводит все результаты, а надо только последний.

n = int(input('Введите число: '))

def fuct(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
        yield f
for el in fuct(n):

    print(f'Факториал числа от 1 до {n} равен: {el}')


