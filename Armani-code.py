import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.strength = self.calculate_strength()
        self.dexterity = self.calculate_dexterity()
        self.intelligence = self.calculate_intelligence()
        self.luck = self.calculate_luck()
        self.health = self.calculate_health()
        self.magic = self.calculate_magic()
        self.inventory = []

    def calculate_health(self):
        if self.character_class == "Mercenary":
            return 100
        elif self.character_class == "Mage":
            return 80
        elif self.character_class == "Knight": 
            return 120
        elif self.character_class == "Bandit":
            return 90
        else:
            return 100
    def calculate_luck(self):
        if self.character_class == "Mercenary":
            return 85
        elif self.character_class == "Mage":
            return 100
        elif self.character_class == "Knight":
            return 95
        elif self.character_class == "Bandit":
            return 110
        else:
            return 100
    def calculate_intelligence(self):
        if self.character_class == "Mercenary":
            return 90
        elif self.character_class == "Mage":
            return 130
        elif self.character_class == "Knight":
            return 110
        elif self.character_class == "Bandit":
            return 85
        else:
            return 100
    def calculate_dexterity(self):
        if self.character_class == "Mercenary":
            return 105
        elif self.character_class == "Mage":
            return 95
        elif self.character_class == "Knight":
            return 90
        elif self.character_class == "Bandit":
            return 130
        else:
            return 100
    def calculate_strength(self):
        if self.character_class == "Mercenary":
            return 100
        elif self.character_class == "Mage":
            return 70
        elif self.character_class == "Knight":
            return 120
        elif self.character_class == "Bandit":
            return 90
        else:
            return 100
    def calculate_magic(self):
        if self.character_class == "Mercenary":
            return 25
        elif self.character_class == "Mage":
            return 150
        elif self.character_class == "Knight":
            return 50
        elif self.character_class == "Bandit":
            return 0
        else:
            return 100
    def display_character(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Health: {self.health}")
        print(f"Magic: {self.magic}")


def create_character():
    print("Welcome to my personal hell (i did not like making this)")
    name = input("Enter your character's name: ")
    

    
    while True:
     try:
         character_class = str(input("Choose your character class (Mercenary, Mage, Knight, Bandit): "))
         list1d = ['Mercenary', 'Mage', 'Knight', 'Bandit']
         if character_class not in list1d:
            print("bruh\nPick a class")
         else:
            break
     except ValueError:
        print("bruh\nPick a class")
        break



    
    

    character = Character(name, character_class)

    print("\nCharacter Created Successfully!")
    character.display_character()
    
    return character

if __name__ == "__main__":
    create_character()



class goblin:
    def __init__(self):
        self.name = goblin
        self.strength = 50
        self.dexterity = 10
        self.intelligence = 10
        self.luck = 10
        self.health = 10
        self.magic = 0

def attack_goblin(Character, goblin):
    damage = Character.strength
    if damage > 0:
        goblin.health -= damage
        print(f"{Character.name} attacks {goblin.name} for {damage} damage!")
    if goblin.health <= 0:
        print("goblin is defeated")

def fight_goblin():
    while Character.health > 0 or goblin.health <= 0:
     try:
        choice = int(input("You are fighting a goblin\nPick (1) to attack"))
        break
     except ValueError:
        print("Pick a number") 
    if choice == 1:
        attack_goblin()


if True:
    fight_goblin()