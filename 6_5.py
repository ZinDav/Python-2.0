# 5 Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

str1 = input('Input math expression: ')
int_num = [int(i) for i in str1.replace('*', ' ').replace('/', ' ').replace('+', ' ').replace('-', ' ').split()]
operat = [i for i in str1 if not i.isdigit()]

def count(n, op):
    if '*' in op:
        i = op.index('*')
        n[i] *= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '/' in op:
        i = op.index('/')
        n[i] /= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '+' in op:
        i = op.index('+')
        n[i] += n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '-' in op:
        i = op.index('-')
        n[i] -= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    else:
        return n[0]

print(count(int_num, operat))

# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;

str1 = input('Input math expression: ')
int_num = [int(i) for i in str1.replace('*', ' ').replace('/', ' ').replace('+', ' ').replace('-', ' ')\
                                                    .replace('(', ' ').replace(')', ' ').split()]
operat = [i for i in str1 if not i.isdigit()]

def count(n, op):
    if '(' in op:
        start = op.index('(')
        finish = op.index(')')
        n.insert(finish, count(n[start:finish], op[start+1:finish]))
        op.pop(start)
        i = 0
        while i < len(n[start:finish]):
            n.pop(start)
            op.pop(start)
            i += 1
        return count(n, op)
    elif '*' in op:
        i = op.index('*')
        n[i] *= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '/' in op:
        i = op.index('/')
        n[i] /= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '+' in op:
        i = op.index('+')
        n[i] += n.pop(i+1)
        op.pop(i)
        return count(n, op)
    elif '-' in op:
        i = op.index('-')
        n[i] -= n.pop(i+1)
        op.pop(i)
        return count(n, op)
    else:
        return n[0]

print(count(int_num, operat))
