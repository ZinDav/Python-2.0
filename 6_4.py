# 4 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.

n1 = 24
n2 = 90

def sieve(num):
    sieve = set(range(2, num+1))
    prime_list = []
    while sieve:
        prime = min(sieve)
        prime_list.append(prime)
        sieve -= set(range(prime, num+1, prime))
    simp_mult = {}
    while num > 1:
        for i in prime_list:
            if not num%i and i in simp_mult.keys():
                num /= i
                simp_mult[i] += 1
            elif not num%i and i not in simp_mult.keys():
                num /= i
                simp_mult[i] = 1
    return simp_mult

m1 = sieve(n1)
m2 = sieve(n2)

common = {k1:v1 for k1, v1 in m1.items() if k1 not in m2.keys()}
common.update({k2:v2 for k2, v2 in m2.items() if k2 not in m1.keys()})

for k1, v1 in m1.items():
    common.update({k1:v1 for k2, v2 in m2.items() if k1 == k2 and v1 >= v2})
    common.update({k2:v2 for k2, v2 in m2.items() if k1 == k2 and v1 < v2})

finish_num = 1
for k, v in common.items():
    finish_num *= k**v
print(finish_num)
