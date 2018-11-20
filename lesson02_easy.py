__author__ = 'Арминэ Мороз'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
print('Task 1')
fruit_list = ["яблоко", "банан", "киви", "арбуз"]

for fruit in fruit_list:
    print('{}. {:>6}'.format(fruit_list.index(fruit) + 1,fruit))
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print('Task 2')
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.
random_list1 = [7, 9.6, 'word', 86, 'smth', 1.8, 'dunno', 7, 53, 7, 7.6, 'oh7']
random_list2 = ['look', 'string', 7, 'stock', 90, 1.8, 'smth']

for el_2 in random_list2:
    for el_1 in random_list1:
        if el_1 == el_2:
            random_list1.remove(el_1)
        else:
            continue

print(random_list1)

print('Task 3')
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

integer_list = [7, 96, 80, 7, -53, 6, 41, -22]
integer_new_list = []

for i in integer_list:
    if i%2 == 0:
        i = i/4
        integer_new_list.append(i)
    else:
        i = i*2
        integer_new_list.append(i)

print(integer_new_list)