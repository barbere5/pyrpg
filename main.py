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


# Dict of octal escape code ANSI color sequences for terminal effects.
# 3 parameters allowed after escape code seperated by ';' link for more info/tables: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
ANSI = { 
    'fggreen': '\033[32;1m', # 1/bold or other font effect must be used else text remains default, why? 
    'reset': '\033[0;0;1m',
    'fgwhite': '\033[37;1m',
    'fggrey': '\033[90;1m',
    'fgred': '\033[31;1m',
    'fgcyan': '\033[96;1m',
    'bgred': '\033[41;1m',
    'bggrey': '\033[100;1m',
    


}

def menu():
    os.system('cls') # 'cls' instead of 'clear' for windows terminal 'clear' is for linux(probally mac also).
    print(ANSI['fgred'] + "_________________________________________"+ ANSI["reset"]) # "" instead of '' for str because open ' in str.
    print(" _____ _            ____       _   _     ")
    print("|_   _| |__   ___  |  _ \ __ _| |_| |__  ")
    print("  | | | '_ \ / _ \ | |_) / _` | __| '_ \ ") 
    print("  | | | | | |  __/ |  __/ (_| | |_| | | |")
    print("  |_| |_| |_|\___| |_|   \__,_|\__|_| |_|")
    print(ANSI['fgred'] + "_________________________________________")
    print("            " + ANSI["fgcyan"] + "- Enter 1 to start -" + ANSI["reset"]+ "            ")
    print("            " + ANSI["fgcyan"] + "- Enter 2 to quit -" + ANSI["reset"]+ "            ")
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
        createchar()
    
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
        print("input not an option.")
        menu_options() 
        
def createchar():
    pass

#### Map & movement ####
ZONENAME = ''
DESC = '1'
EXAMINE = '2'
EXPLORED = False
UP = 'w', 'north'
DOWN = 's','south'
LEFT = 'a', 'west'
RIGHT = 'd','east'

# Take this out most likley.gfndfgn
explored_loc = {'a1': False, 'a2': False,'a3': False, 'a4': False,
                'b1': False, 'b2': False,'b3': False, 'b4': False,
                'c1': False, 'c2': False,'c3': False, 'c4': False,
                'd1': False, 'd2': False,'d3': False, 'd4': False,
                }

# Not finished
zonemap = {
    'a1':{
        ZONENAME : '',
        DESC : '1',
        EXAMINE : '2',
        EXPLORED : False,
        UP : ('w', 'north'), # If issue w tuple values del one and remove tuple
        DOWN : ('s','south'),
        LEFT :('a', 'west'),
        RIGHT :('d','east')
    },
    'a2':{
        ZONENAME : '',
        DESC : '1',
        EXAMINE : '2',
        EXPLORED : False,
        UP : ('w', 'north'),
        DOWN : ('s','south'),
        LEFT :('a', 'west'),
        RIGHT :('d','east')
    },
    'a3':{
        ZONENAME : '',
        DESC : '1',
        EXAMINE : '2',
        EXPLORED : False,
        UP : ('w', 'north'),
        DOWN : ('s','south'),
        LEFT :('a', 'west'),
        RIGHT :('d','east')
    },
    'a4':{
        ZONENAME : '',
        DESC : '1',
        EXAMINE : '2',
        EXPLORED : False,
        UP : ('w', 'north'),
        DOWN : ('s','south'),
        LEFT :('a', 'west'),
        RIGHT :('d','east')
    },
    'b1':{
        ZONENAME : '',
        DESC : '1',
        EXAMINE : '2',
        EXPLORED : False,
        UP : ('w', 'north'),
        DOWN : ('s','south'),
        LEFT :('a', 'west'),
        RIGHT :('d','east')
    },
    'b2':{
        ZONENAME : 'base',
        DESC : 'This is the Start',
        EXAMINE : 'Everything is as you remember.',
        EXPLORED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3'
    },
}

# Game inter
def location():
    print('\n' + ('#' * (4 + len(zonemap[curplayer.pos][ZONENAME]))))
    print('# ' + zonemap[curplayer.pos][ZONENAME] + ' #')
    #print('# ' + zonemap[curplayer.pos][DESC] + ' #')
    print(('#' * (4 + len(zonemap[curplayer.pos][ZONENAME]))))


# call funcs
menu()
#location()
