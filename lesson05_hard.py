__author__ = 'Арминэ Мороз'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.



# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp < file_name > - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <dir_name> - меняет текущую директорию на одну из внутренних")
    print("ls - отображение полного пути текущей директории")

def change_dir():
    path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(path):
        os.chdir(path)
        if path == os.getcwd():
            print("Успешный переход ")
        else:
            print("Переход не удался")

def make_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_file():
    abs_filename = os.path.join(os.getcwd(), file_name)
    os.path.exists(abs_filename)
    if os.path.isfile(abs_filename):
        newfile = file_name + '.copy'
        shutil.copy(abs_filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def abs_path():
    print(os.path.abspath(os.getcwd()))

def remove_file():
    abs_filename = os.path.join(os.getcwd(), file_name)
    os.path.exists(abs_filename)
    if os.path.isfile(abs_filename):
        os.remove(file_name)
        if os.path.exists(file_name):
            print("Файл не удален")
        else:
            print("Файл успешно удален")

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cd": change_dir,
    "cp": copy_file,
    "rm": remove_file,
    "ls": abs_path,
}

try:
    name = sys.argv[2]
    dir_name = name
    file_name = name

except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
