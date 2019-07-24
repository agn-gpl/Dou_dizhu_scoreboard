#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C) 2019  AGN

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
p=[0]*4
game_count=0
losers=set()

def reset_game(point):
    global p,game_count,losers
    p[1],p[2],p[3],game_count=point,point,point,0
    losers.clear()
    print(f'Reset everything...\nEach player has {point} point(s) now.')

def print_status():
    global p,game_count
    print(f'Game {game_count} :')
    for i in range(1,4):
        print(f'player {i} : {p[i]:8} point(s)')

def game_end(landlord,point,boom=0):
    global p,game_count
    game_count+=1
    pt=point*2**(boom)
    if landlord==1:
        p[1]+=pt*2
        p[2]-=pt
        p[3]-=pt
    elif landlord==2:
        p[1]-=pt
        p[2]+=pt*2
        p[3]-=pt
    elif landlord==3:
        p[1]-=pt
        p[2]-=pt
        p[3]+=pt*2

def check_losers():
    global p,losers
    for i in range(1,4):
        if p[i]<=0:
            losers.add(f'player{i}')
    if len(losers)==0:
        return False
    else:
        return True

def start():
    global p
    p[0]=int(input('Welcom to Dou dizhu!\nPlease input initial points:\n> '))
    p[1],p[2],p[3]=p[0],p[0],p[0]
    print('Game start! Good luck!')
    return p[0]
    
def print_help():
    print('no help message yet...')

def set_point(num,point):
    global p
    p[num]=point
    if num==0:
        print(f'Set initial point to {point}.')
    else:
        print(f"Ser player{num}'s point to {point}.")
    return p[0]
    
def main():
    default=start()
    while True:
        npt=input('> ').strip()
        if npt=='':
            continue
        tok=npt.split()
        if (tok[0]=='1' or tok[0]=='2' or tok[0]=='3') and len(tok)==2:
            game_end(int(tok[0]),int(tok[1]))
        elif (tok[0]=='1' or tok[0]=='2' or tok[0]=='3') and len(tok)>2:
            game_end(int(tok[0]),int(tok[1]),int(tok[2]))
        elif tok[0]=='0' and len(tok)>=2:
            reset_game(int(tok[1]))
        elif tok[0]=='status' or tok[0]=='s':
            print_status()
        elif tok[0]=='help' or tok[0]=='h':
            print_help()
        elif tok[0]=='set' and len(tok)>=3:
            default=set_point(int(tok[1]),int(tok[2]))
        elif (tok[0]=='reset' or tok[0]=='r') and len(tok)==1:
            reset_game(default)
        elif (tok[0]=='reset' or tok[0]=='r') and len(tok)>1:
            reset_game(int(tok[1]))
        elif tok[0]=='q' or tok[0]=='quit':
            print_status()
            break
        else:
            print('ERROR: Unknown command')
        if check_losers():
            print_status()
            for loser in losers:
                print(f'{loser} is bankrupt. What a loser!')
            again=input('If you want to exit, input "quit" or "q". Otherwise a new game will start.\n> ')
            if again=='q' or again=='quit':
                break
            else:
                reset_game(default)

if __name__ == '__main__':
    main()
