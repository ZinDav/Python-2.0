from random import randint
from math import sqrt

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

try:
    a = int(input('Input the day of week: '))
    if a in [6, 7]:
        print('Да')
    elif a > 7:
        print('There is no this day of week')
    else:
        print('Нет')
except ValueError:
    print('Input non integer')

# 2.
# 1)
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений
#  предикат.

def check(a: int, b: int, c: int):
    print(a, b, c)
    if not (a or b or c) is (not a and not b and not c):
        print('True')
    else:
        print('False')

x = randint(0, 1)
y = randint(0, 1)
z = randint(0, 1)

check(x, y, z)

# 2) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def quarter_axis(x: int, y: int):
    if x == 0 and y == 0:
        return 'Point is in the center'
    elif x == 0:
        return 'Point is on the y-axis'
    elif y == 0:
        return 'Point is on the x-axis'
    elif x < 0:
        if y < 0:
            return '3 quarter'
        else:
            return '2 quarter'
    else:
        if y < 0:
            return '4 quarter'
        else:
            return '1 quarter'

try:
    w, r = map(int, input('Input coordinates: ').split(', '))
    print(quarter_axis(w, r))
except ValueError:
    print('Input non coordinate')

# 3.
# 1) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

def span(r: int):
    if r == 1:
        return 'x ∈ (0, +∞), y ∈ (0, +∞)'
    elif r == 2:
        return 'x ∈ (-∞, 0), y ∈ (0, +∞)'
    elif r == 3:
        return 'x ∈ (-∞, 0), y ∈ (-∞, 0)'
    elif r == 4:
        return 'x ∈ (0, +∞), y ∈ (-∞, 0)'
    else:
        return 'There is no such quarter'

try:
    print(span(int(input('Input quarter number: '))))
except ValueError:
    print('Input non integer')


# 2) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

def distance(x: list, y: list):
    return abs(sqrt((y[0] - x[0])**2 + (y[-1] - x[-1])**2))

try:
    s = list(map(int, input('Input coordinates: ').split(', ')))
    p = list(map(int, input('Input coordinates: ').split(', ')))
    print(distance(s, p))
except ValueError:
    print('Input non coordinate')
