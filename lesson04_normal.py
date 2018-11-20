__author__ = 'Арминэ Мороз'
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

print('Task 1')
# Without re
string_1 = "mtMmEZUOmcq"

string_1 = list(string_1)
# Replacing capitals with comma to split by it
for let in string_1:
    if let.isupper():
        string_1[string_1.index(let)] = "."
# Cast list to string
string_1 = ''.join(string_1)
string_1 = string_1.split(".")
# New list made of lower letters only
lower_let = [letter_lo for letter_lo in string_1 if letter_lo.islower()]
print(lower_let)

# With re

string_2 = "mtMmEZUOmcq"
low_string = re.findall(r'([a-z]+)', string_2)

print(low_string)
#
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print('Task 2')
# Without re

str_1 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
str_1 = list(str_1)

# str_1_new = []
# # Проверка элементов строки на соблюдение последовательности
# ind = 0
# print(len(str_1))
# while ind < len(str_1) - 5: # last ind 67 + 4
#     if str_1[ind].islower():
#         if str_1[ind+1].islower():
#             marker = 0
#             while marker < len(str_1) - 8 and str_1[ind+3 + marker].isupper() and str_1[ind+4 + marker].isupper():
#                 if str_1[ind+2 + marker].isupper():
#                     marker += 1
#                     str_1_new.append(str_1[ind + 2 + marker])
#                     print(str_1_new)
#                     ind += 1
#                 else:
#                     ind += 1
#                     break
#             ind += 1
#         else:
#             ind += 1
#     else:
#         ind += 1




#str_1_new = list(str_1_new)

# Вариант с re

str_2 = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"

str_2 = re.findall(r'[a-z][a-z]([A-Z]+)[A-Z][A-Z]', str_2)
# str_2 = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', str_2)

print(str_2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print('Task 3')

import random

# Создание файла в текущем директории
f = open('numbers.txt', 'w', encoding = 'UTF-8')
# Генерация и запись чисел в файл
i = 1
while i <= 2500:
    a = str(random.randint(0,9))
    f.write(a)
    i += 1
# Завершение работы с файлом
f.close()
# Открытие файла для чтения
f = open('numbers.txt','r')

for line in f:
    # Берется ранее созданный цифровой рад. Создание списка из цифр, повторяемых более двух раз
    num_seq = re.findall(r'(0{2,}|1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,})', line)
    #     num_seq = re.findall(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)', line)
    # Выборка максимального элемента из списка по значению длина
    num_seq = max(num_seq, key = len)

    print("The longest numeric sequence ", num_seq)

f.close()
