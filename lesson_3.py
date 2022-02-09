#Попова Светлана
#ДЗ к 3 уроку

#1

#def my_function(num_1, num_2):
    #try:
        #result = num_1 / num_2
        #print(f'Результат деления равен: {result:.0f}')
    #except:
        #print('Делить на ноль нельзя!')


#my_function(int(input('Введите первое число: ')), int(input('Введите второе число: ')))

#2

#def person(name, surname, year, city, email, tel):
    #print(f'Вас зовут {name} {surname}, {year} года рождения, проживающий в городе {city}, тел.: {tel}, почта: {email}')


#person(name = 'Иван', surname = 'Иванов', year = 1980, city = 'Москва', email = 'yandex@yandex.ru', tel = +71234567890)


#3

#def my_func_3(num_1, num_2, num_3):
    #result = (max(num_1, num_2, num_3) - min(num_1, num_2, num_3)) + max(num_1, num_2, num_3)
    #print(result)

#my_func-3(5, 3, 2)

#4

#def my_func_4(x, y):
    #result = x ** (y * -1)
    #print(f'Итого: {round(result, 4)}')

#my_func_4(int(input('Введите первое число: ')), int(input('Введите второе число: ')))

#5
#Почему выводится второй раз сумма чисел увеличенная вдвое?
#Почему при нажатии на любую другую букву выходиш, а не только на q?
#def my_func_5():
    #total = 0
    #while True:
        #user_input = input('Введите числа через пробел или нажмите "q" для выхода: ').split()
        #for i in user_input:
            #if i == 'q':
                #return total
            #else:
                #try:
                    #total += sum(map(int, user_input))
                    #print(f'Сумма введеных вами чисел равна: {total}')
                #except ValueError:
                    #print('До скорой встречи!')
                    #break


#my_func_5()

#6-7

def int_func():
    user_word = input('Введите слова латинскими буквами: ').split()
    for word in user_word:
        if word.isalpha() and ascii(word) and word.islower():
            print(word.title())
        else:
            print(f'Эти слова не подходят: {word}')
int_func()





