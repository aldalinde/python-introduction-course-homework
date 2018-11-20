__author__ = 'Арминэ Мороз'
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]

import random

list_1 = [random.randint(-20, 20) for el in range(8)]
print(list_1)

sqr_list = [el**2 for el in list_1]
print(sqr_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ['peach', 'orange', 'apple','banana', 'grapes', 'plum']
fruits_2 = ['grapes', 'banana', 'mango', 'orange']
#fruits_same = [(fr1, fr2) for fr1 in fruits_1 for fr2 in fruits_2 if fr1 == fr2]
#[('orange', 'orange'), ('banana', 'banana'), ('grapes', 'grapes')]

fruits_same = [fr1 for fr1 in fruits_1 for fr2 in fruits_2 if fr1 == fr2]
print(fruits_same)
# Задание-3
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3

list_num = [random.randint(-100, 100) for el in range(20)]
print(list_num)

list_num_new = [el_num for el_num in list_num if el_num%2 == 0 if el_num > 2 if el_num%3 != 0]
print(list_num_new)