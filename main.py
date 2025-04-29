import random
import sys
import textwrap
import time
import math
import os
import keyboard


class player:
    def __init__(self):
        self.name = ''
        self.species = ''
        self.role = ''

        self.hp = 0 # Health
        self.sp = 0 # stamina
        self.mp = 0 # mana
        self.fp = 0 # faith

        self.buffsdebuffs = []

        self.pos = 'b2' # Player position

curplayer = player()


# Dict of ANSI escape codes for 24bit color
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences more info
ANSI = { 
    'fgbrown' : '\033[38;2;189;93;58m',
    'fgreset' : '\033[39m',
    'fggrey' : '\033[38;2;131;131;131m',
    'fgblue' : '\033[38;2;6;2;112m',
    'fggreen' : '\033[38;2;0;255;0m',
    'fgred' : '\033[38;2;255;0;0m'



}

def menu():
    os.system('cls') # 'cls' instead of 'clear' for windows terminal 'clear' is for linux(probally mac also).
    print(ANSI['fgbrown'] + " __________________________________________") # "" instead of '' for str because open ' in str.
    print("|" + ANSI["fgreset"] + " _____ _            ____       _   _      " + ANSI['fgbrown'] + "|")
    print("|" + ANSI["fgreset"] + "|_   _| |__   ___  |  _ \ __ _| |_| |__   " + ANSI['fgbrown'] + "|")
    print("|" + ANSI["fgreset"] + "  | | | '_ \ / _ \ | |_) / _` | __| '_ \  " + ANSI['fgbrown'] + "|") 
    print("|" + ANSI["fgreset"] + "  | | | | | |  __/ |  __/ (_| | |_| | | | " + ANSI['fgbrown'] + "|")
    print("|" + ANSI["fgreset"] + "  |_| |_| |_|\___| |_|   \__,_|\__|_| |_| " + ANSI['fgbrown'] + "|")
    print(ANSI['fgbrown'] + "|__________________________________________|")
    print("            " + ANSI["fgreset"] + "- Enter " + ANSI['fggreen'] + "[1]" + ANSI['fgreset'] + " to start -" + ANSI["fgbrown"]+ "            ")
    print("            " + ANSI["fgreset"] + "- Enter " + ANSI['fgred'] + "[2]" + ANSI['fgreset'] + " to quit -" + ANSI["fgbrown"]+ "            ")
    print(" +---------------------------------------+" + ANSI['fgreset'])
    menu_options() # Maybe should del menu_options() func and add code to menu() func.

def menu_options():
    choice = input('-> ').lower() # cleaner making input.lower() in initial var.
    if choice == '1':
        os.system('cls')
        print('Starting game', end='')
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)  
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        os.system('cls')
        worldgen()
    
    elif choice == '2':
        print('Exiting game', end='')
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        os.system('cls')
        sys.exit()
    else:
        print("Input not an option.")
        menu_options() 
        
def createchar():
    pass
 
def worldgen():
    print('How big do you want your world to be?')
    print('1) Small[8x8] 2) Medium[16x16] 3) Large[32x32]')
    choice = int(input('-> '))
    if choice > 3 or choice < 1:
        os.system('cls')
        print("Input not an option.")
        worldgen()
    else:
        size = 8 * choice
    
    # generate a list of sublists 
    arr = []
    subarr = []
    for i in range(size):
        for  n in range(size):
            subarr.append(random.randint(0,3))
        arr.append(subarr)
        subarr = []
    #1print(arr)


    hill = ANSI['fgbrown']+ '∩' + ANSI['fgreset']
    mountain = ANSI['fggrey'] + '▲' + ANSI['fgreset']
    water = ANSI['fgblue']+ '≈' + ANSI['fgreset']
    plains = ANSI['fggreen']+ '≡' + ANSI['fgreset']
    town =  ANSI['fgbrown']+ '♦' + ANSI['fgreset']

    mapkey = [hill, mountain, plains, water]
    for i in arr:
        #print(i)
        mapstr = ''
        for n in i:
            #print(n)
            mapstr += mapkey[n]
        print(mapstr)
    print("World key: water= hill= mountain= plains= ln/.;lm/")
    print("Keep world?")
    input('-> ')

    

            
        


# call funcs
menu()
#print(mountain)
#worldgen()

