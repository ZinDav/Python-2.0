from time import time

# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1 Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
# псевдослучайных чисел.

num = [int(i) for i in str(time()).split('.')[1]]
print(sum(num[:])*num[0]/num[-1])
