from random import randrange
from random import random

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

def play(f, s):
    fi = randrange(0, 2)
    pl = [f, s]
    print(f"{pl[fi]} is first player")
    cand = 2021
    def cycle(players, first, cand):
        if cand > 0:
            print('')
            print(f'You have {cand} candies')
            try:
                st = int(input(f'{players[first]}, Input the quantity of candies: '))
                if st > 28 or st < 0:
                    raise Exception('Wrong quantity')
                else:
                    cand -= st
                    cycle(players, 1, cand) if not first%2 else cycle(players, 0, cand)
            except:
                print('Input wrong quantity of candies')
                cycle(players, 0, cand) if not first%2 else cycle(players, 1, cand)
        else:
            print(f'{players[first-1]} win')
    cycle(pl, fi, cand)

player1 = input('Player1, input your name: ')
player2 = input('Player2, input your name: ')
play(player1, player2)

# a) Добавьте игру против бота

def play_b(f):
    fi = randrange(0, 2)
    b = 'Bot'
    pl = [f, b]
    print(f"{pl[fi]} is first player")
    cand = 121
    def cycle(players, first, cand):
        if cand > 0:
            print('')
            print(f'You have {cand} candies')
            if players[first] == 'Bot':
                b_st = randrange(0, 29)
                print(f'Bot takes {b_st} candies')
                cand -= b_st
                cycle(players, 0, cand)
            else:
                try:
                    st = int(input(f'{players[first]}, Input the quantity of candies: '))
                    if st > 28 or st < 0:
                        raise Exception('Wrong quantity')
                    else:
                        cand -= st
                        cycle(players, 1, cand)
                except:
                    print('Input wrong quantity of candies')
                    cycle(players, 0, cand)
        else:
            print(f'{players[first-1]} win')
    cycle(pl, fi, cand)

play_b(input('Input your name: '))

# b) Подумайте как наделить бота ""интеллектом""

def play_ib(f):
    fi = randrange(0, 2)
    b = 'Bot'
    pl = [f, b]
    print(f"{pl[fi]} is first player")
    cand = 121
    def cycle(players, first, cand):
        if cand > 0:
            print(f'\nYou have {cand} candies')
            if players[first] == 'Bot':
                if cand > 28 and cand < 57 and random() > 0.5:
                    b_st = cand - 29
                elif cand < 29 and random() > 0.25:
                    b_st = cand
                else:
                    b_st = randrange(0, 29)
                print(f'Bot take {b_st} candies')
                cand -= b_st
                cycle(players, 0, cand)
            else:
                try:
                    st = int(input(f'{players[first]}, Input the quantity of candies: '))
                    if st > 28 or st < 0:
                        raise Exception('Wrong quantity')
                    else:
                        cand -= st
                        cycle(players, 1, cand)
                except:
                    print('Input wrong quantity of candies')
                    cycle(players, 0, cand)
        else:
            print(f'{players[first-1]} win')
    cycle(pl, fi, cand)

play_ib(input('Input your name: '))
