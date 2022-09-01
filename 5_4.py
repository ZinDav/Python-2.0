import json

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Origin.txt', 'w') as f:
    f.write('Hello, Ann! Do you have 100 thousands dollars? Hello, I have no even 1 thousand dollars!')

def zp(str1):
    sl = []
    for i in str1.split():
        if not (i[-1] == '.' or i[-1] == ',' or i[-1] == ':' or i[-1] == '!' or i[-1] == '?'):
            sl.append(i)
        else:
            sl.append(i[:len(i)-1])
            sl.append(i[-1])
    dsl = {}
    for n, i in enumerate(set(sl)):
        dsl[n] = i
        for l in range(len(sl)):
            if sl[l] == i:
                sl[l] = f'{n}'
    return (' '.join(sl), dsl)

def unzp(str1, enc):
    f_s = [enc[i] for i in str1.split()]
    fin_s = []
    for i in f_s:
        if not (i == '.' or i == ',' or i == ':' or i == '!' or i == '?'):
            fin_s.append(i)
        else:
            fin_s[-1] += i
    return ' '.join(fin_s)


with open('Origin.txt', 'r') as f1, open('incode.txt', 'w') as f2, open('inc.json', 'w') as f3:
    orig = f1.read()
    str1 = zp(orig)
    f2.write(str1[0])
    j = json.dump(str1[1], f3, indent="")

with open('incode.txt', 'r') as f1, open('encode.txt', 'w') as f2, open('inc.json', 'r') as f3:
    inc = f1.read()
    j = json.load(f3)
    f2.write(unzp(inc, j))
