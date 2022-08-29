from random import randrange

# 1. Вычислить число c заданной точностью d.

d = input('Input the precision: ')
num = input('Input the number: ')

def td(d: str, num: str):
    d = len(d.split('.')[1])
    num = list(num.split('.'))
    if int(num[1][d]) < 5:
        num[1] = num[1][:d]
        return float('.'.join(num))
    else:
        num[1] = num[1][:d-1] + str(int(num[1][d-1]) + 1)
        return float('.'.join(num))

print(td(d, num))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Input the natural number: '))
s = [2]

def compare(i, s):
    while i > 1:
        for m in s:
            if not i%m:
                return compare(int(i/m), s)
        if i not in s:
            s.append(i)
            return i

for i in range(3, 101):
    compare(i, s)

def simple_m(i, s, simp_m):
    while i > 1:
        for m in s:
            if not i%m:
                simp_m.append(m)
                return simple_m(int(i/m), s, simp_m)
        if i not in s:
            return f'{i} not in s'
    return simp_m

simp_m = []
print(simple_m(num, s, simp_m))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

seq = [45, 156, 16.66, 65, 156, 2, 1, -14, 78, 16.66, -175, 15, 5]
print((lambda l: list(set(l)))(seq))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

k = int(input('Input the natural number: '))

strings = []
for i in range(k, -1, -1):
    if i > 1:
        m = randrange(0, 101)
        strings.append(f'{m}*x^{i}') if m else m
    elif i == 1:
        m = randrange(0, 101)
        strings.append(f'{m}*x') if m else m
    else:
        m = randrange(0, 101)
        strings.append(f'{m}') if m else m

with open('expr.txt', 'w') as f:
    f.write(f"{' + '.join(strings)} = 0")

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('expr2.txt', 'w') as f:
    f.write('11*x^2 + 67 = 0')

summ = []
for i in ['expr.txt', 'expr2.txt']:
    with open(i, 'r') as file:
        f = file.read().split(' = 0')[0].split(' + ')
        [summ.append(m) for m in f]

multip = []
s = []
for i in summ:
    k = i.split('x')
    multip.append(int(k[0].split('*')[0]))
    if len(k) > 1:
        s.append(int(k[1].split('^')[-1])) if k[1].split('^')[-1] else s.append(1)
    else:
        s.append(0)

count = {}
for i in set(s):
    for k in range(len(s)):
        if i == s[k] and s.index(i) is not k:
            count[i] = multip[s.index(i)] + multip[k]
        elif i == s[k] and s.index(i) is k:
            count[i] = multip[k]
        else:
            pass

st = []
for k, v in count.items():
    if k > 1:
        st.insert(0, f'{v}*x^{k}')
    elif k == 1:
        st.insert(0, f'{v}*x')
    else:
        st.insert(0, f'{v}')

with open('new_file.txt', 'w') as nf:
    nf.write(f'{" + ".join(st)} = 0')
