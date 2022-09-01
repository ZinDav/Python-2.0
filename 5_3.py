from random import randrange

# 3. Создайте программу для игры в ""Крестики-нолики"".

fi = input('Player1, input your name: ')
se = input('Player2, input your name: ')
cross = randrange(0, 2)
pl = [fi, se]
print(f"{pl[cross]} plays by cross and goes first")
print(f"{pl[cross-1]} plays by zero and goes second")
rp = ['   ', '   ', '   ']
kn = [rp[:] for i in range(3)]
def cycle(players, first, kn):
    print(' 0 ', ' 1 ', ' 2 ', ' 3 ', ' x ', sep='|', end='')
    print('\n----------------')
    for num, m in enumerate(kn, 1):
        print(f' {num} ', end='|')
        [print(i, end='|') for i in m]
        print('\n----------------')
    print(' y ')
    if not [True for i in range(len(kn)) if '   ' in kn[i]]:
        print('Nobody win')
        return 'Draw'
    for i in range(len(kn)):
        if kn[i][0] == kn[i][1] == kn[i][2] == ' x ' or kn[i][0] == kn[i][1] == kn[i][2] == ' o ':
            print(f'{players[first-1]} win')
            return players[first-1]
        elif kn[0][i] == kn[1][i] == kn[2][i] == ' x ' or kn[0][i] == kn[1][i] == kn[2][i] == ' o ':
            print(f'{players[first-1]} win')
            return players[first-1]
    if kn[0][0] == kn[1][1] == kn[2][2] == ' x ' or kn[0][2] == kn[1][1] == kn[2][0] == ' x ' \
        or kn[0][0] == kn[1][1] == kn[2][2] == ' o ' or kn[0][2] == kn[1][1] == kn[2][0] == ' o ':
        print(f'{players[first-1]} win')
        return players[first-1]
    try:
        x, y = [int(i)-1 for i in input(f'{players[first]}, Input the coordinates(x, y): ').split(', ')]
        if x > 2 or y > 2 or x < 0 or y < 0:
            raise Exception('Non coordinates')
        elif players[first] == players[cross]:
            kn[y][x] = ' x '
        elif players[first] == players[cross-1]:
            kn[y][x] = ' o '
        cycle(players, 1, kn) if not first%2 else cycle(players, 0, kn)
    except:
        print('Input wrong coordinates')
        cycle(players, 0, kn) if not first%2 else cycle(players, 1, kn)

cycle(pl, cross, kn)
