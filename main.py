import random
import sys
import textwrap
import time
import math
import os


class player:
    def __init__(self):
        self.name = ''
        self.species = ''
        self.role = ''
        self.religion = ''

        self.str = 0 # Strength
        self.dex = 0 # Dexterity
        self.int = 0 # Intelligence
        self.fp = 0 # faith

        self.buffsdebuffs = []

        self.posx = 0 # Player position
        self.posy = 0

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
    os.system('cls') # 'cls' instead of 'cls' for windows terminal 'cls' is for linux(probally mac also).
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
        '1': {'species': 'human', 'description': 'Adaptable and well-rounded.', 'stats': { 'str' : 10, 'dex' : 10, 'int' : 10

        },},
        '2': {'species': 'elf', 'description': 'Magically gifted.', 'stats': { 'str' : 7, 'dex' : 7, 'int' : 15

        },},
        '3': {'species': 'dwarf', 'description': 'Gifted with a strong constitution.', 'stats': { 'str' : 15, 'dex' : 7, 'int' : 7

        },}
    }

    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print("           -Character Creation-")
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(' Select a species for more info:')
    print(ANSI['fggreen']+ " 1)" + ANSI['fgreset'] + " Human")
    print(ANSI['fggreen']+ " 2)" + ANSI['fgreset'] + " Elf")
    print(ANSI['fggreen']+ " 3)" + ANSI['fgreset'] + " Dwarf")
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    
    # Selected species
    choice = input('-> ')

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

        print(ANSI['fgred'] + " Strength: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['str']))
        print(ANSI['fggreen'] + " Dexterity: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['dex']))
        print(ANSI['fgblue'] + " Intelligence: " + ANSI['fgreset'] + str(speciesdic[choice]['stats']['int']))
        print(fspacing(" Select species?") + " Select species?" + fspacing(" Select species?") )
        print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
        print(' 1) Yes 2) No')

        # It works don't touch :o
        confirm = input('-> ')
        while confirm != '1' and confirm != '2':
            print('Not an option, Try again.')
            confirm = input('-> ') # needs to be fixed to solve edgecase but it works well enough rn.
        if confirm == '1':
            curplayer.species = speciesdic[choice]['species']
            curplayer.str = speciesdic[choice]['stats']['str']
            curplayer.dex = speciesdic[choice]['stats']['dex']
            curplayer.int = speciesdic[choice]['stats']['int']
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
            speciesmenu() #recurse


def religionmenu():
        
        descript = ['Nameless', 'Infernal', 'Stygian', 'Abyssal', 'Adorable', 'Aggressive', 'Formless', 'Alert', 'Alive', 'Amused', 'Angry',
 'Annoyed', 'Annoying', 'Anxious', 'Arrogant', 'Ashamed', 'Rotting', 'Awful', 'Blind', 'Black', 'Bloody', 'Blue', 'Blue-Eyed', 'Blushing',
 'Bored', 'Brave', 'Bright', 'Busy', 'Calm', 'Careful', 'Cautious',
 'Charming', 'Cheerful', 'Corrupt', 'Clever', 'Cloudy', 'Clumsy', 'Colorful', 'Combative',
 'Comfortable', 'Concerned', 'Condemned', 'Confused', 'Bloody', 'Courageous',
 'Dead', 'Cruel', 'Curious', 'Dangerous', 'Dark', 'Dead', 'Defeated',
 'Defiant', 'Delightful', 'Depressed', 'Determined', 'Different', 'Difficult', 'Disgusted',
 'Bloody', 'Disturbed', 'Dizzy', 'Doubtful', 'Dull', 'Baleful', 'Cursed', 'Skinless', 'Barbed', 'Ominous', 'Blood-Black']

        
        
        
        noun = ['Egg', 'Beast', 'Star', 'Sun', 'Moon', 'Mountain', 'Storm', 'Planet']
        shrine_features = ['Barbed', 'Ominous', '']
        shrine_materials = ['Copper', 'Wood', 'Iron', 'Black', 'White', 'Marble', 'Stone', 'Blue', 'Azure', 'Glass', 'Dirt']
        shrine_forms = ['Obelisk', 'Menhir', 'Monolith', 'Dolmen']

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
            print(' Select a religion:')
            print(ANSI['fgblue']+ " 1) " + ANSI['fgreset'] + religion_names[0])
            print(ANSI['fgblue']+ " 2) " + ANSI['fgreset'] + religion_names[1])
            print(ANSI['fgblue']+ " 3) " + ANSI['fgreset'] + religion_names[2])
            print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
            print('  ' + ANSI["fgreset"] + "- Enter " + ANSI['fgred'] + "[4]" + ANSI['fgreset'] + " to generate new religions -")

            # There is a better way to do this that is not repetitive dexaghetti but I am losing my mind and it works.
            confirm = input('-> ')
            while confirm != '1' and confirm != '2' and confirm != '3' and confirm != '4':
                print('Not an option, Try again.')
                confirm = input('-> ') 
            if confirm == '1':
                os.system('cls')
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(fspacing('select ' + religion_names[0] + '?') + 'select ' + religion_names[0] + '?' + fspacing('select ' + religion_names[0] + '?'))
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(' 1) Yes 2) No')
                confirm2 = input('-> ')

                while confirm2 != '1' and confirm2 != '2':
                    print('Not an option, Try again.')
                    confirm2 = input('-> ') 
                if confirm2 == '1':
                    curplayer.religion = religion_names[int(confirm) - 1]
                    os.system('cls')
                    print(religion_names[0] + ' Selected', end='')
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    charname()
                elif confirm2 == '2':
                    rmenu2()

                

            if confirm == '2':
                os.system('cls')
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(fspacing('select ' + religion_names[1] + '?') + 'select ' + religion_names[1] + '?' + fspacing('select ' + religion_names[1] + '?'))
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(' 1) Yes 2) No')
                confirm2 = input('-> ')

                while confirm2 != '1' and confirm2 != '2':
                    print('Not an option, Try again.')
                    confirm2 = input('-> ') 
                if confirm2 == '1':
                    curplayer.religion = religion_names[int(confirm) - 1]
                    os.system('cls')
                    print(religion_names[1] + ' Selected', end='')
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    charname()
                elif confirm2 == '2':
                    rmenu2()

            if confirm == '3':
                os.system('cls')
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(fspacing('select ' + religion_names[2] + '?') + 'select ' + religion_names[2] + '?' + fspacing('select ' + religion_names[2] + '?'))
                print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
                print(' 1) Yes 2) No')
                confirm2 = input('-> ')

                while confirm2 != '1' and confirm2 != '2':
                    print('Not an option, Try again.')
                    confirm2 = input('-> ') 
                if confirm2 == '1':
                    curplayer.religion = religion_names[int(confirm) - 1]
                    os.system('cls')
                    print(religion_names[2] + ' Selected', end='')
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    print('.', end='', flush=True)
                    time.sleep(0.5)
                    charname()
                elif confirm2 == '2':
                    rmenu2()
                

            if confirm == '4':
                religionmenu() # recurse


        rmenu2()


def charname():
    os.system('cls')
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(fspacing('-Character Name-') + "-Character Name-" + fspacing('-Character Name-'))
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])

    name = input(' Enter a Name: ')
    os.system('cls')
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(fspacing(" Keep " + name + " as your name?") + " Keep " + name + " as your name?" + fspacing(" Keep " + name + " as your name?"))
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(' 1) Yes 2) No')
    confirm = input('-> ')
    while confirm != '1' and confirm != '2':
        print('Not an option, Try again.')
        confirm = input('-> ') 
    if confirm == '1':
        os.system('cls')
        curplayer.name = name
        print(name + ' Selected', end='')
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        gamestart()

    if confirm == '2':
        charname()


def gamestart():
        

    os.system('cls')
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print("               -Character-")
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(" The " + ANSI['fggreen'] + curplayer.species + ANSI['fgreset'] + " " + curplayer.name)
    print(" follower of " + ANSI['fgblue'] + curplayer.religion + ANSI['fgreset']+ '.')
    print(ANSI['fgbrown'] + " +---------------------------------------+" + ANSI['fgreset'])
    print(" Confirm Character?")
    print(' 1) Yes 2) No')
    confirm = input('-> ')
    while confirm != '1' and confirm != '2':
        print('Not an option, Try again.')
        confirm = input('-> ') 
    if confirm == '1':
        os.system('cls')
        print('World generating', end='')
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        wandering()
    if confirm == '2':
        os.system('cls')
        print('Returning to Character creation menu', end='')
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('.', end='', flush=True)
        time.sleep(0.5)
        os.system('cls')
        speciesmenu()


def wandering():
    os.system('cls')
    world()
    visualizemap()


# cool func but not using rn.
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


def world():
    # 8X8 matrix world map base
    matrix = []
    for i in range(8):
        x = []
        for k in range(8):
            x.append(str(random.randint(0,3)))
        matrix.append(x)
    return matrix
    # Turn matrix into str map 

def visualizemap():
    hill = ANSI['fgbrown']+ '∩' + ANSI['fgreset']
    mountain = ANSI['fggrey'] + '▲' + ANSI['fgreset']
    water = ANSI['fgblue']+ '≈' + ANSI['fgreset']
    plains = ANSI['fggreen']+ '≡' + ANSI['fgreset']
    town =  ANSI['fgbrown']+ '♦' + ANSI['fgreset']

    mapkey = [hill, mountain, plains, water]
    for i in world(): # Prints +---+---+---+---+---+---+---+---+
        print('\n' + '+---' * 8 + '+')
        for x in i:
            print('| {} '.format(mapkey[int(x)]), end='')
        print('|', end='')
    print('\n' + '+---' * 8 + '+')
    print(ANSI['fgbrown'] + "+-------------------------------+" + ANSI['fgreset'])
    print(' Map Key: Hills = {} Mountains = {} \n Plains = {} Water = {}'.format(mapkey[0], mapkey[1], mapkey[2], mapkey[3]))
    print(ANSI['fgbrown'] + "+-------------------------------+" + ANSI['fgreset'])
visualizemap()

# call funcs
menu()