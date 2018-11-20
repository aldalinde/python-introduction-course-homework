__author__ = 'Moroz Armine'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3):
        self.point_1 = {'x': x_1, 'y': y_1}
        self.point_2 = {'x': x_2, 'y': y_2}
        self.point_3 = {'x': x_3, 'y': y_3}

    def get_side_1_2_length(self):
        return math.sqrt(abs((self.point_2['x']-self.point_1['x'])**2 + (self.point_2['y']-self.point_1['y'])**2))

    def get_side_2_3_length(self):
        return math.sqrt(abs((self.point_3['x']-self.point_2['x'])**2 + (self.point_3['y']-self.point_2['y'])**2))

    def get_side_1_3_length(self):
        return math.sqrt(abs((self.point_3['x']-self.point_1['x'])**2 + (self.point_3['y']-self.point_1['y'])**2))

    def get_square(self):
        return abs((self.point_1['x']-self.point_3['x']) * (self.point_2['y']-self.point_3['y']) -
                          (self.point_2['x']-self.point_3['x']) * (self.point_1['y']-self.point_3['y']) /2)

    def get_altitude_1(self):
        return self.get_square() * 2 / self.get_side_2_3_length()

    def get_altitude_2(self):
        return self.get_square() * 2 / self.get_side_1_3_length()

    def get_altitude_3(self):
        return self.get_square() * 2 / self.get_side_1_2_length()

    def get_perim(self):
        return self.get_side_1_2_length() + self.get_side_2_3_length() + self.get_side_1_3_length()



triangle_1 = Triangle(3, 5, 8, 2, 1, 1)

print("Периметр первого треугольника равен {} см".format(triangle_1.get_perim()))

print("Площадь первого треугольника равна {} см кв".format(triangle_1.get_square()))

print("Длины высот первого треугольника от угла 1: {} см, от угла 2: {} см, от угла 3: "
      "{} см" .format(triangle_1.get_altitude_1(), triangle_1.get_altitude_2(), triangle_1.get_altitude_3()))

triangle_2 = Triangle(4, 6, 6, 2, 2, 2)

print("Периметр второго треугольника равен {} см".format(triangle_2.get_perim()))

print("Площадь второго треугольника равна {} см кв".format(triangle_2.get_square()))

print("Длины высот второго треугольника от угла 1: {} см, от угла 2: {} см, от угла 3: "
      "{} см" .format(triangle_2.get_altitude_1(), triangle_2.get_altitude_2(), triangle_2.get_altitude_3()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    def __init__(self, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
        self.point_1 = {'x': x_1, 'y': y_1}
        self.point_2 = {'x': x_2, 'y': y_2}
        self.point_3 = {'x': x_3, 'y': y_3}
        self.point_4 = {'x': x_4, 'y': y_4}

    def get_base_3_4_length(self):
        return math.sqrt(abs((self.point_4['x']-self.point_3['x'])**2 + (self.point_4['y']-self.point_3['y'])**2))

    def get_base_1_2_length(self):
        return math.sqrt(abs((self.point_2['x']-self.point_1['x'])**2 + (self.point_2['y']-self.point_1['y'])**2))

    def get_side_2_4_length(self):
        return math.sqrt(abs((self.point_4['x']-self.point_2['x'])**2 + (self.point_4['y']-self.point_2['y'])**2))

    def get_side_1_3_length(self):
        return math.sqrt(abs((self.point_3['x']-self.point_1['x'])**2 + (self.point_3['y']-self.point_1['y'])**2))

# Площадь треугольника с вершинами 1,2,3, составляющего одну часть трапеции
    def get_square_1_triangle(self):
        return abs((self.point_1['x']-self.point_3['x']) * (self.point_2['y']-self.point_3['y']) -
                          (self.point_2['x']-self.point_3['x']) * (self.point_1['y']-self.point_3['y']) / 2)

# Площадь треугольника с вершинами 2,3,4 составляющего вторую часть трапеции
    def get_square_2_triangle(self):
        return abs((self.point_2['x']-self.point_4['x']) * (self.point_3['y']-self.point_4['y']) -
                          (self.point_3['x']-self.point_4['x']) * (self.point_2['y']-self.point_4['y']) / 2)

# Площадь трапеции (суммированием площадей треугольников 1,2,3 и 2,3,4)
    def get_square_trapez(self):
        return self.get_square_1_triangle() + self.get_square_2_triangle()

# Площадь треугольника с вершинами 1,3,4 для вычисления высоты
    def get_square_3_triangle(self):
        return abs((self.point_1['x'] - self.point_4['x']) * (self.point_3['y'] - self.point_4['y']) -
                       (self.point_3['x'] - self.point_4['x']) * (self.point_1['y'] - self.point_4['y']) / 2)

#
    def get_perim(self):
        return self.get_base_3_4_length() + self.get_base_1_2_length() + self.get_base_2_4_length()\
               + self.get_base_1_3_length()

# Длина высоты с вершиной в точке 2
    def get_altitude_2(self):
        return self.get_square_2_triangle() * 2 / self.get_base_3_4_length()

# Длина высоты с вершиной в точке 1
    def get_altitude_1(self):
        return self.get_square_3_triangle() * 2 / self.get_base_3_4_length()

# Проверка на то, что трапеция(параллельные основания)
    def is_trapez(self):
        if self.get_altitude_1() == self.get_altitude_2():
            return " трапеция"
        else:
            return " не является трапецией"

# Проверка трапеции на равнобедренность
    def is_isolesces(self):
        if self.get_side_1_3_length() == self.get_side_2_4_length():
            return " является равнобедренной"
        else:
            return " не является равнобедренной трапецией"



isosc_trapez_1 = IsoscelesTrapezoid(4, 6, 9, 6, 2, 1, 11, 1)

print("Фигура 1 - {} и {}".format(isosc_trapez_1.is_trapez(), isosc_trapez_1.is_isolesces()))


isosc_trapez_2 = IsoscelesTrapezoid(4, 8, 9, 9, 7, 4, 13, 5)

print("Фигура 2 - {} и {} ".format(isosc_trapez_2.is_trapez(), isosc_trapez_2.is_isolesces()))

#print("Периметр первого треугольника равен {} см".format(triangle_1.perim))
#
# print("Площадь первого треугольника равна {} см кв".format(triangle_1.square))
#
# print("Длины высот первого треугольника от угла 1: {} см, от угла 2: {} см,"
#       " от угла 3: {} см" .format(triangle_1.altitude_1, triangle_1.altitude_2, triangle_1.altitude_3,))
