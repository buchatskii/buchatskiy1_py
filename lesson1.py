# Задача 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

from distutils.command.build_scripts import first_line_re

# a = int(input("Введите число: "))

# if 1 <= a <= 5:
#     print ("Да, иди работай!")
# elif 6 <= a <= 7:
#     print ("Да, но лучше поспать)")
# else:
#     print("Нет")

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             print((not (x or y or z)) == (not x and not y and not z))

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))

# if x > 0 and x <= 100 and y > 0 and y <= 100:
#     print("Четверть 1")
# elif x < 0 and x >= -100 and y > 0 and y <= 100:
#     print("Четверть 2")
# elif x < 0 and x >= -100 and y < 0 and y >= -100:
#     print("Четверть 3")
# elif x > 0 and x <= 100 and y < 0 and y >= -100:
#     print("Четверть 4")
# else:
#     print("Нельзя определить четверть(")

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# i = int(input("Введите искомую четверть: "))

# if i == 1:
#     print("Диапозон возможно x(0,100); y(0,100)")
# elif i == 2:
#     print("Диапозон возможно x(0,-100); y(0,100)")
# elif i == 3:
#     print("Диапозон возможно x(0,-100); y(0,-100)")
# elif i == 4:
#     print("Диапозон возможно x(0,100); y(0,-100)")
# else:
#     print("Недопустимый номер четверти")


# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from math import sqrt


# x1 = int(input("Введите число x1: "))
# y1 = int(input("Введите число y1: "))
# x2 = int(input("Введите число x2: "))
# y2 = int(input("Введите число y2: "))

# d = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
# print(round(d, 3))


