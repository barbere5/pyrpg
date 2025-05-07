import random as rd
import sys
import os 

colors = { 
    'fgbrown' : '\033[38;2;189;93;58m',
    'fgreset' : '\033[39m',
    'fggrey' : '\033[38;2;131;131;131m',
    'fgblue' : '\033[38;2;0;0;255m',
    'fggreen' : '\033[38;2;0;255;0m',
    'fgred' : '\033[38;2;255;0;0m'
}

def spacing(sentence: str):
    return " " * (int((41 - len(sentence)) / 2))

class StatusBars:
    status_remaining: str = '█'
    status_lost: str = '_'
    sides: str = '|'
    colors: dict = colors

    def __init__(self, entity, health_color: str= 'fgred', mana_color: str= 'fgblue', prayer_color: str= 'fggreen', length: int = 15):
        self.entity = entity
        self.length = length

        # Health vars
        self.maxval_health = entity.max_health
        self.curval_health = entity.current_health
        self.color_health = colors.get(health_color)

        # Mana vars
        self.maxval_mana = entity.max_mana
        self.curval_mana = entity.current_mana
        self.color_mana = colors.get(mana_color)

        # Prayer vars
        self.maxval_prayer = entity.max_prayer
        self.curval_prayer = entity.current_prayer
        self.color_prayer = colors.get(prayer_color)

        # Update all stats when called
    def update(self) -> None:
        self.curval_health = self.entity.current_health
        self.curval_mana = self.entity.current_mana
        self.curval_prayer = self.entity.current_prayer

    def draw(self) -> None:
        # Health 
        remaining_bars_health = round(self.curval_health / self.maxval_health * self.length)
        lost_bars_health = self.length - remaining_bars_health
        # Mana
        remaining_bars_mana = round(self.curval_mana / self.maxval_mana * self.length)
        lost_bars_mana = self.length - remaining_bars_mana
        # Prayer
        remaining_bars_prayer = round(self.curval_prayer / self.maxval_prayer * self.length)
        lost_bars_prayer = self.length - remaining_bars_prayer

        # Print status bars
        print(spacing(f'Health:{self.entity.current_health}/{self.entity.max_health} Mana:{self.entity.current_mana}/{self.entity.max_mana} Prayer:{self.entity.current_prayer}/{self.entity.max_prayer}') + f'Health:{self.entity.current_health}/{self.entity.max_health} Mana:{self.entity.current_mana}/{self.entity.max_mana} Prayer:{self.entity.current_prayer}/{self.entity.max_prayer}')
        print(f'{self.sides}'
              f'{self.color_health}'
              f'{remaining_bars_health * self.status_remaining}'
              f'{lost_bars_health * self.status_lost}'
              f'{colors["fgreset"]}'
              f'{self.sides}'
              f'{self.sides}'
              f'{self.color_mana}'
              f'{remaining_bars_mana * self.status_remaining}'
              f'{lost_bars_mana * self.status_lost}'
              f'{colors["fgreset"]}'
              f'{self.sides}'
              f'{self.sides}'
              f'{self.color_prayer}'
              f'{remaining_bars_prayer * self.status_remaining}'
              f'{lost_bars_prayer * self.status_lost}'
              f'{colors["fgreset"]}'
              f'{self.sides}')

class Player:
    def __init__(self, name: str, species: str, religion: str, strength: int, dexterity: int, mind: int):
        self.name = name
        self.species = species
        self.religion = religion

        self.strength = strength
        self.dexterity = dexterity
        self.mind = mind

        self.max_health = strength * 5
        self.current_health = self.max_health
        self.max_mana = mind * 5
        self.current_mana = self.max_mana
        self.max_prayer = 10
        self.current_prayer = self.max_prayer

        self.stat_bars = StatusBars(self)



character: Player = Player(name="Joe", species="Goblin", religion='The Black Star', strength= 10, dexterity= 12, mind= 20)



character.stat_bars.draw()
print("Updated status bars:")
character.current_health -= 5
character.current_mana -= 50
character.current_prayer - 0
character.stat_bars.update()
character.stat_bars.draw()