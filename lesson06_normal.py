# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

<<<<<<< Updated upstream
=======
class Person():
    def __init__(self, surname, first_name, fathers_name):
        self.surname = surname
        self.first_name = first_name
        self.fathers_name = fathers_name
# Краткое имя
    def get_abbr_name(self):
        return self.surname + ' ' + self.first_name[0] + '.' + self.fathers_name[0] + '.'

class Student(Person):
    def __init__(self, surname, first_name, fathers_name, grade, mother, father, subjects):
        Person.__init__(self, surname, first_name, fathers_name)
        self.grade = grade
        self.mother = mother
        self.father = father
        self.subjects = subjects
    def grade_num_let(self):
        return {"grade" : re.findall(r'[0-9]+', self.grade),
               "letter": re.findall(r'[A-Z]', self.grade)}

class Teacher(Person):
    def __init__(self, surname, first_name, fathers_name, subject):
        Person.__init__(self, surname, first_name, fathers_name)
        self.subject = subject


subject = ['русский язык', 'математика', 'химия']
teachers_list = []
teacher_1 = Teacher("Козлова", "Елена", "Геннадьевна", 0)
teachers_list.append(teacher_1)
teacher_2 = Teacher("Сидоров", "Николай", "Иванович", 1)
teachers_list.append(teacher_2)
teacher_3 = Teacher("Шпак", "Виктор", "Федорович", 2)
teachers_list.append(teacher_3)


mother_1 = Person("Иванова", "Мария", "Петровна")
mother_2 = Person("Смирнова", "Елена", "Олеговна")
father_1 = Person("Иванов", "Иван", "Иванович")
father_2 = Person("Смирнов", "Сергей", "Иванович")

students_list = []
student_1 = Student('Иванов', 'Петр', 'Иванович', '5B', mother_1, father_1, (0, 1))
students_list.append(student_1)
student_2 = Student('Иванова', 'Ольга', 'Ивановна', '10A', mother_1, father_1, (0, 1, 2))
students_list.append(student_2)
student_3 = Student('Смирнов', 'Андрей', 'Сергеевич', '8B', mother_2, father_2, (0, 1, 2))
students_list.append(student_3)
student_4 = Student('Смирнов', 'Николай', 'Сергеевич', '3A', mother_1, father_1, (0, 1))
students_list.append(student_4)

students_list_copy = students_list.copy()
students_onegrade = []
def all_students_names():
    for student in students_list:
        for student_copy in students_list_copy:
            if students_list[3] == students_list_copy[3]:
                students_onegrade.append(student_copy.get_abbr_name())
    return students_onegrade


# def get_all_grades:
#     for
>>>>>>> Stashed changes
# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
print(all_students_names())


<<<<<<< Updated upstream
=======
print(teacher_1.surname + " - " + subject[teacher_1.subject])
print(teacher_1.surname + " - " + subject[teacher_1.subject])
print(teacher_2.surname + " - " + subject[teacher_2.subject])
>>>>>>> Stashed changes
