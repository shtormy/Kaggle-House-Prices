#ДЗ к уроку №5
#Попова Светлана

#1
with open('my_file.txt', 'w+', encoding='utf-8') as f_obj:
    while True:
        a = input('Введите строку: ')
        if a == "":
            break
        f_obj.writelines(a+'\n')

#2

lines = 0
words = 0
with open('my_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split()
        lines += 1
        words += len(word)
print(f'В данном файле: {lines} строки и {words} слов.\n')

#3
#Не работает!!!
with open(r'C:\Users\USER\PycharmProjects\geekbrains\1\text_3.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    for line in f:
        name = line.split()[0]
        salary = float(line.split()[1])
        my_dict = {name: salary}
        average_salary = sum(my_dict.values()) / len(my_dict) #Проблема
        min_salary = [i[0] for i in my_dict.items() if i[1] < 20000]

        print(f'Меньше 20000 руб. получают: {min_salary}')  # выводит все значения!!
        print(f'Средняя заработная плата составляет {average_salary} рублей.')  # выводит все значения!!!
                                                                                # не считает сумму

#4

my_list = ['один', 'два', 'три', 'четыре', 'пять']
new_list = []
with open(r'C:\Users\USER\PycharmProjects\geekbrains\1\text_4.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    j = 0
    for i in a:
        c = i.find(' ')
        d = i[:c]
        r = i.replace(d, my_list[j])
        j = j + 1
        new_list.append(r)
        #print(r, end="")
with open(r'my_file1.txt', 'w+', encoding='utf-8') as f2:
    f2.seek(0)
    f2.writelines(new_list)

#5

with open('my_file.txt', 'w+', encoding='utf-8') as f:
    my_numbers = list(map(int, input('Введите числа через пробел: ').split()))
    total = 1
    for i in my_numbers:
        total *= i
        number = str(sum(my_numbers))
    print(my_numbers)
    print(number)
    f.writelines(rf'Сумма введенных чисел {my_numbers} равна: {number}')

#6

#Не работает!!!
my_dict = {}
with open(r'C:\Users\USER\PycharmProjects\geekbrains\1\text_6.txt', 'r', encoding='utf-8') as f:
   my_file = f.readlines()
   for line in my_file:
       subject, hours = line.split(':')
       for i in hours:
           if i == ' ' or '9' >= i >= '0':
               our_hours = sum(map(int, " ". join(i).split())) #не суммирует
               my_dict[subject] = our_hours
print(my_dict)

#7
#Пока не поняла как делать



