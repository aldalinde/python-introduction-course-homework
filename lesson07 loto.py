#!/usr/bin/python3
__author__ = 'Armine Moroz'

import re

import random
# Определяем родительский класс  заполнение случайными неповторяющимися числами от 1 до 90
class RandomNumber():
    def __init__(self, a):
        self.rand_num = random.randint(1, 90)
        self.numbers = []
        self.length = a
        self.index = self.length - len(self.numbers)
    def __iter__(self):
        return self
# Итератор с методом next. следующий элемент списка - случайное число от 1 -90
    def __next__(self):
        if len(self.numbers) > self.length:
            raise StopIteration
        else:
            self.rand_num = random.randint(1, 90)
# Исключение числа, если оно уже выпадало
            if self.rand_num in self.numbers:
                pass
            else:
                self.numbers.append(self.rand_num)
                return self.rand_num

# Получение количества оставшихся из 90 итераций для его последующего выведения
    def get_iters_left(self):
        nums_left = self.index
        return nums_left


# Класс "бочки" - случайного числа от 1-90
class NewBarrel(RandomNumber):
    def __init__(self, a):
        RandomNumber.__init__(self, a)

# Класс карточки, формируемой из строк из случайных чисел от 1-90
class NewCard(RandomNumber):
    def __init__(self, a):
        RandomNumber.__init__(self, a)
# получение строки для карточки
    def get_line1(self):
# Получение 5 чисел для строки и их сортировка
        line_1 = [next(self) for _ in range(self.length)]
        line_1.sort()
# Вставка четырех пробелов в случайные положения
        [line_1.insert(random.randint(0,8), '  ') for _ in range(4)]
        return line_1
#Внешний вид карточки. Предполагалось из трех строк путем проставления после format
    # трех аргументов self.get_line1(), а не одного.
    def view_card(self):
        return r'{}'.format(self.get_line1())



barrel = NewBarrel(89)

your_card = NewCard(5)

comp_card = NewCard(5)


# while answer != 'N':
#     answer = input('Поиграем в лото? Нет - N, да - любая клавиша')

print("Новый бочонок: {} (осталось {})".format(next(barrel), barrel.get_iters_left()))
print('-------------- Ваша карточка ---------------')
#print(your_card.get_line1())

print(your_card.view_card())
print('--------------------------------------------')

# print('----------- Карточка компьютера---------------')
# print(comp_card.view_card())
# print('--------------------------------------------')
# answer = ''
#
# # один ход
# pattern = next(barrel)
# if pattern in comp_card.get_line1():
#     comp_card.get_line1()[your_card.get_line1().index(pattern)] = ''
#
#
# if pattern in your_card.get_line1():
#     choice = input('Зачеркнуть цифру? (y/n)')
#     if choice == 'y':
#         your_card.get_line1()[your_card.get_line1().index(pattern)] = ''
#     elif choice == 'n':
#         print("Вы проиграли")



"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
