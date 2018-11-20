__author__ = 'Арминэ Мороз'

import math

import random

import datetime

import locale

print('Task 1')
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь. Вывести результат
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


integer_list = [2, -5, 8, 9, -25, 25, 4]
integer_new_list = []

for i in integer_list:
    if i >= 0:
        if math.sqrt(i) == int(math.sqrt(i)):
            i = math.sqrt(i)
            integer_new_list.append(i)
        else:
            continue
    else:
        continue

integer_new_list = [round(i) for i in integer_new_list]

print(integer_new_list)

print('Task 2')
# Задача-2: Дана дата в формате dd.mm.yyyy, например:
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

locale.setlocale(locale.LC_ALL, "ru")

my_date = input("Enter a date in dd.mm.yyyy format")

my_date = my_date.split('.')

my_date = [int(day)for day in my_date]

my_date = datetime.date(my_date[2], my_date[1], my_date[0])

string_date = my_date.strftime('%d %B %Y')

print(string_date, "года")


print('Task 3')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
# выведите созданный список
number_list = []
n = int(input('Choose list length by writing an integer'))
i = 0

while i < n:
    number_list.append(random.randint(-100, 100))
    i += 1

print(number_list)


print('Task 4')
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
# выведите результаты

# a)
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = []

for num in lst:
    marker = 0
    for num2 in lst2:
        if num == num2:
            marker = 1
            break
    if marker == 0:
        lst2.append(num)

print(lst2)

lst3 = []
for num in lst:
    if lst.count(num) == 1:
        lst3.append(num)

print(lst3)
