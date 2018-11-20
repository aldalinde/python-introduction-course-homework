__author__ = 'Арминэ Мороз'

import sys
import re
import os
import shutil

print(sys.argv)

 # Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def help():
    print("help - справка")
    print("make_dir - создание директории dir_ с заданным номером от 1 - 9 "
          "в текущей директории.")
    print("del_dir - удаление директории dir_ с заданным номером от 1 - 9 "
          "из текущей директории.")
    print("list_dir - список папок текущей директории")
    print("dupl_file - создание копии файла, из которого запущен данный скрипт")

def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
#
    if os.path.exists(dir_name):
        print("Папка {} уже существует". format(dir_name))
    else:
        os.mkdir(dir_path)
        if os.path.exists(dir_name):
            print("Папка {} успешно создана". format(dir_name))
        else:
            print("Создание {} папки не удалось". format(dir_name))



def delete_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(dir_name):
 #       if os.path.isdir(dir_name):
        os.rmdir(dir_path)
        if os.path.exists(dir_name):
            print("Удаление {} папки не удалось". format(dir_name))
        else:
            print("Удаление {} папки прошло успешно". format(dir_name))
#        else:
 #           print("Объект {} не является папкой". format(dir_name))
    else:
        print("Папка по указанному адресу отсутствует и не может быть удалена")


def list_dir():
    print(os.listdir(os.getcwd()))


def duplicate_file():
    filename = sys.argv[0]
    newfile = filename + '.dupl'
    shutil.copy(filename, newfile)
    if os.path.exists(newfile):
        print("Файл ", newfile, " был успешно создан")
    else:
        print("Возникли проблемы копирования")

do = {
    "make_dir": make_dir,
    "del_dir": delete_dir,
}

try:
    task = sys.argv[1]
except IndexError:
    task = None


try:
    dir_num = sys.argv[2]
    dir_n = 'dir_' + dir_num
    try:
        re.match('[1-9]', dir_num)
    except IndexError:
        print("Вы не задали номер создаваемой/удаляемой папки от 1 до 9")
except IndexError:
    dir_num = None

if task:
    if do.get(task):
        do[task](dir_n)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
do_2 = {
    "list_dir" : list_dir,
    "help": help,
}

try:
    task_2 = sys.argv[1]
except IndexError:
    task_2 = None

if task_2:
    if do_2.get(task_2):
        do_2[task_2]()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

do_3 = {
    "dupl_file" : duplicate_file,
}

try:
    task_3 = sys.argv[1]
except IndexError:
    task_3 = None

if task_2:
    if do_3.get(task_3):
        do_3[task_3]()