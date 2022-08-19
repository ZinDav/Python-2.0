from math import factorial

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

try:
    a = tuple(map(int, tuple(input('Input number: ').replace(',', '').replace('.', ''))))
    print(sum(a))
except ValueError:
    print('Input non number')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# try:
    N = int(input('Input integer number: '))
    fl = []
    for i in range(1, N+1):
        fl.append(factorial(i))
    print(fl)
except ValueError:
    print('Input non integer number')

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

try:
    n = int(input('Input integer number: '))
except ValueError:
    print('Input non integer number')
else:
    nums = []
    for i in range(1, n+1):
        nums.append((1 + 1/i)**i)
    print(sum(nums))
