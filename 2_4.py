from random import shuffle

# 4. 
# 1) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

try:
    N = int(input('Input integer number: '))
except ValueError:
    print('Input non integer number')
else:
    ran = list(range(-N, N+1))
    ind = []

    with open('file.txt', 'w') as file:
        file.write('4\n1\n6')

    with open('file.txt', 'r') as file:
        ind = list(map(int, list(file.read().split('\n'))))

    print(f'Sequence: {ran}')
    print(f'Positions: {ind}')
    mult = 1
    for i in ind:
        mult *= ran[i]
    print(f'Multiplication: {mult}')

# 2) Реализуйте алгоритм перемешивания списка.

r = list(range(0, 15))
shuffle(r)
print(r)
