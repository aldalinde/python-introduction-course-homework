
__author__ = 'Арминэ Мороз'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
number = list(input("Enter an integer that is > 0 "))
# Вывести самую большую цифру этого числа.
d_max = 0
for d in number:
    d = int(d)
    if d > d_max:
        d_max = d

print(d_max)

# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Число приходит в виде целого беззнакового.


# Задача-2: Запросить у пользователя два целых числа, связать их с переменными.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
a = input("Enter integer a ")
b = input("Enter integer b ")
a,b = b,a
print("Swapping a & b. a = ", a, "b = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input("Enter integer a "))
b = int(input("Enter integer b "))
c = int(input("Enter integer c "))
x1 = 0
x2 = 0

D = b**2 - 4 * a * c
print(D)

if D > 0:
    D = float(D)
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("root x1 = ", x1,"root x2 = ", x2 )
elif D == 0:
    x1 = -b / (2 * a)
    print("root x = ", x1)
else:
    print("no result for x")


