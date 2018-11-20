__author__ = 'Арминэ Мороз'

import datetime
#
print('Task 1')
# # Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# # Определить координату y точки с заданной координатой x.
# # вычислите и выведите y
# #
# # equation = 'y = -12x + 11111140.2121'
# # x = 2.5
# # подсказка: x у вас уже есть, остается с помощью срезов получить значения k и b,
# # а затем вевести итоговый результат: print('y = {}'.format(k * x + b))

equation = 'y = -12x + 11111140.2121'
x = 2.5

equation = equation.split(' ')
i_b = equation.index('11111140.2121')
b = float(equation[i_b])

i_arg = equation.index('-12x')
arg = equation[i_arg]
k = list(arg)
k = (k[:3])
k = int(''.join(k))
print(k)

print('y = {}'.format(k * x + b))


print('Task 2')
#  # Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# # Проверить, корректно ли введена дата.
# # Условия корректности:
#  # 1. Длина исходной строки для частей должна быть в соответствии с форматом
# #  (т.е. 2 символа (числа) для дня, 2 - для месяца, 4 - для года)
#  # 2. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
# #  (в зависимости от месяца, февраль не учитываем)
# # 3. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# # 4. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
#
# # The first approach

my_date = input("Enter a date in dd.mm.yyyy format")

my_date = my_date.split('.')

my_date = [int(day)for day in my_date]

my_date = datetime.date(my_date[2], my_date[1], my_date[0])

# Here the interpreter informs us if there was en error e.g. ValueError: year -340 is out of range

# The second approach operating with integers without date/time or any other imported modules
# Presumably we don't know || &&

my_new_date = input("Enter a new date in dd.mm.yyyy format")

my_new_date = my_new_date.split('.')

day = my_new_date[0]
month = my_new_date[1]
year = my_new_date[2]

if len(day) != 2:
    print("The day must contain two numeric figures")
    exit()
if len(month) != 2:
    print("The month must contain two numeric figures")
    exit()
if len(year) != 4:
    print("The month must contain two numeric figures")
    exit()

if day[0] == 0:
    day.remove[0]

day = int(day)

if month[0] == 0:
    month.remove[0]

month = int(month)

if year[0] == 0:
    year.remove[0]
    if year[0] == 0:
        year.remove[0]
        if year[0] == 0:
            year.remove[0]

year = int(year)

if month < 12:
    if month < 0:
        print("The month must be within range 01:12")
        exit()
    elif month <= 7:
        if month %2 == 0:
            if day > 30:
                print("The days of given month must be within range 01:30 ")
                exit()
            elif day < 1:
                print("The days of given month must be within range 01:30 ")
                exit()
            else:
                pass
        else:
            if day > 31:
                print("The days of given month must be within range 01:31 ")
                exit()
            elif day < 1:
                print("The days of given month must be within range 01:31 ")
                exit()
            else:
                pass
    else:
        if month %2 == 0:
            if day > 31:
                print("The days of given month must be within range 01:31 ")
                exit()
            elif day < 1:
                print("The days of given month must be within range 01:31 ")
                exit()
            else:
                pass
        else:
            if day > 30:
                print("The days of given month must be within range 01:30 ")
                exit()
            elif day < 1:
                print("The days of given month must be within range 01:30 ")
                exit()
            else:
                pass

else:
    print("The month must be within range 01:12")
    exit()


if year > 9999:
    print("The year must be within range 0001:9999")
    exit()
elif year < 1:
    print("The year must be within range 0001:9999")
    exit()
else:
    print("Your date has a correct format")

# Пример корректной даты
# date = '01.11.1985'
# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'