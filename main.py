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
        self.religion = ''

        self.hp = 0 # Health
        self.sp = 0 # stamina
        self.mp = 0 # mana
        self.fp = 0 # faith

        self.buffsdebuffs = []

        self.pos = 'b2' # Player position

curplayer = player()

# func for centering text
def fspacing(s):
    return " " * (int((41 - len(s)) / 2)) # spacing to center species name


# Dict of ANSI escape codes for 24bit color
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences more info
ANSI = { 
    'fgbrown' : '\033[38;2;189;93;58m',
    'fgreset' : '\033[39m',
    'fggrey' : '\033[38;2;131;131;131m',
    'fgblue' : '\033[38;2;0;0;255m',
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
        speciesmenu()
    
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
        
def speciesmenu():
    # Dictonary for species info 
    speciesdic = {
        1: {'species': 'human', 'description': 'Adaptable and well-rounded.', 'stats': { 'hp' : 10, 'sp' : 10, 'mp' : 10

        },},
        2: {'species': 'elf', 'description': 'Magically gifted.', 'stats': { 'hp' : 7, 'sp' : 7, 'mp' : 15

        },},
        3: {'species': 'dwarf', 'description': 'Gifted with a strong constitution.', 'stats': { 'hp' : 15, 'sp' : 7, 'mp' : 7

        },}
    }

    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print("           -Character Creation-")
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(' Select a species for more info:')
    print(ANSI['fggreen']+ " 1)" + ANSI['fgreset'] + " Human")
    print(ANSI['fggreen']+ " 2)" + ANSI['fgreset'] + " Elf")
    print(ANSI['fggreen']+ " 3)" + ANSI['fgreset'] + " Dwarf")
    
    # Selected Species
    choice = int(input('-> '))

    if choice not in speciesdic:
        os.system('cls')
        print('Not an option, Try again.')
        speciesmenu() #recurse
    else:
        spacing = " " * int((41 - len(speciesdic[choice]['species'])) / 2) # spacing to center species name
        os.system('cls')
        print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
        print( spacing + "-" + speciesdic[choice]['species'] + "-" + spacing)
        print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
        print(fspacing(speciesdic[choice]['description']) + " " + speciesdic[choice]['description'] + ' ' + fspacing(speciesdic[choice]['description']))

        print(ANSI['fgred'] + " Health: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['hp']))
        print(ANSI['fggreen'] + " Stamina: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['sp']))
        print(ANSI['fgblue'] + " Mana: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['mp']))
        print(fspacing(" Select species?") + " Select species?" + fspacing(" Select species?") )
        print(' 1) Yes 2) No')

        # It works don't touch :o
        confirm = input('-> ')
        while confirm != '1' and confirm != '2':
            print('Not an option, Try again.')
            confirm = input('-> ') # needs to be fixed to solve edgecase but it works well enough rn.
        if confirm == '1':
            curplayer.species = speciesdic[choice]['species']
            curplayer.hp = speciesdic[choice]['stats']['hp']
            curplayer.sp = speciesdic[choice]['stats']['sp']
            curplayer.mp = speciesdic[choice]['stats']['mp']
            os.system('cls')
            print( speciesdic[choice]['species'] + ' Selected', end='')
            time.sleep(0.5)
            print('.', end='', flush=True)
            time.sleep(0.5)
            print('.', end='', flush=True)
            time.sleep(0.5)
            print('.', end='', flush=True)
            time.sleep(0.5)
            religionmenu()

        if confirm == '2':
            os.system('cls')
            print("returning to selection menu.")
            speciesmenu() #recurse


def religionmenu():
        
        descript = ['adorable', 'adventurous', 'aggressive', 'Formless', 'alert', 'alive', 'amused', 'angry',
    'annoyed', 'annoying', 'anxious', 'arrogant', 'ashamed', 'Rotting', 'awful',
    'bad', 'Blind', 'black', 'bloody', 'blue', 'blue-eyed', 'blushing',
    'bored', 'brave', 'breakable', 'bright', 'busy', 'calm', 'careful', 'cautious',
    'charming', 'cheerful', 'Corrupt', 'clear', 'clever', 'cloudy', 'clumsy', 'colorful', 'combative',
    'comfortable', 'concerned', 'condemned', 'confused', 'Bloody', 'courageous', 'crazy',
    'Dead', 'cruel', 'curious', 'dangerous', 'dark', 'dead', 'defeated',
    'defiant', 'delightful', 'depressed', 'determined', 'different', 'difficult', 'disgusted',
    'Bloody', 'disturbed', 'dizzy', 'doubtful', 'dull', 'baleful', 'cursed', 'Skinless']
        
        
        
        noun = ['Egg', 'Beast', 'Star', 'Sun', 'Moon', 'Mountain' ]
        shrine_features = ['barbed', 'ominous', '']
        shrine_materials = ["copper", "wood", "iron", "black", "white", "marble", "stone", "blue", "azure", "glass", "dirt"]
        shrine_forms = ["obelisk", "menhir", "monolith", "dolmen"]

        religion_names = []
        shrine_list = []
        while len(religion_names) <= 3:
            religion_name = "The " + descript[random.randint(0, (len(descript)-1))] + " " + noun[random.randint(0, (len(noun)-1))]
            religion_names.append(religion_name)
            shrine_description = "A " + shrine_materials[random.randint(0, len(shrine_materials) - 1)] + ' ' + shrine_forms[random.randint(0, len(shrine_forms) - 1)]
            shrine_list.append(shrine_description)

        def rmenu2():    
            os.system('cls')
            print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
            print("           -religion selection-")
            print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
            print(' Select a religion for more info:')
            print(ANSI['fgblue']+ " 1) " + ANSI['fgreset'] + religion_names[0])
            print(ANSI['fgblue']+ " 2) " + ANSI['fgreset'] + religion_names[1])
            print(ANSI['fgblue']+ " 3) " + ANSI['fgreset'] + religion_names[2])

            confirm = input('-> ')
            while confirm != '1' and confirm != '2' and confirm != '3' and confirm != '4':
                print('Not an option, Try again.')
                confirm = input('-> ') 
            if confirm == '1':
                pass

            if confirm == '2':
                pass


        rmenu2()


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


def wandering():
    pass

# call funcs
menu()
#print(mountain)
#worldgen()

