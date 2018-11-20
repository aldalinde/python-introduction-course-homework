
__author__ = 'Арминэ Мороз'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# i = float, f = number of tokens after comma to round float to
def round_number(i, f):
    round_i = 0
    res_i = i
    i = str(i)
    f_check = i.split('.')
    f_check = f_check[1]
    i = list(i)
    ind_comma = i.index('.')
    # Checking if i is long enough to round
    if len(f_check) > f:
        n = i[ind_comma + f + 1]
        n = int(n)

        i = ''.join(i[:ind_comma + f + 1])
        i = float(i)
        # Estimating the number to add: 0.6 --> 1 eg: 0.01 if f = 2
        i_changer = ["0", '.']
        i_changer[2:f] = i_changer[0] * (f-1)
        i_changer.append('1')
        i_changer = ''.join(i_changer)
        i_changer = float(i_changer)

        # Processing positives
        if res_i > 0:
            if n >= 5:
                round_i = i + i_changer
            else:
                round_i = i
        # Processing negatives
        if res_i < 0:
            if n >= 5:
                round_i = i - i_changer
            else:
                round_i = i
    # No changes to short floats
    else:
        round_i = res_i

    return round_i



a = 7.94768
b = 4.4852
c = -2.04859

print(round_number(a, 3))
print(round_number(b, 2))
print(round_number(c, 3))
print(round_number(b, 4))
print(round_number(c, 2))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_number(a):
    a_1 = a[:3]
    a_2 = a[3:]

    def summ_el(n):
        b = int(n[0])
        c = int(n[1])
        d = int(n[2])
        sum = b + c + d
        return(sum)

    if summ_el(a_1) == summ_el(a_2):
        return(True)
    else:
        return(False)

def message(boolean):
    if boolean == True:
        print("Congratulations! Lucky number!")
    else:
        print("Try again")

message(lucky_number('547853'))

message(lucky_number('341792'))

message(lucky_number(input('Enter a 6-digit number')))
