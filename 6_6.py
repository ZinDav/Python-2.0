# 6 Дана строка:
# 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
# Необходимо получить словарь, в котором ключи – слова, значения – количество слов в
# строке:
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}

str1 = 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
lst = str1.split(', ')
word_counter = {}

for i in lst:
    if i in word_counter.keys():
        word_counter[i] += 1
    else:
        word_counter[i] = 1
print(word_counter)
