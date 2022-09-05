# 7 Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.

with open('jack.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

t = text.replace(',', '').replace('.', '').split()
word_counter = {}

for i in t:
    if i in word_counter.keys():
        word_counter[i] += 1
    else:
        word_counter[i] = 1
print(word_counter)
