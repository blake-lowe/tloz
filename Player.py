'''
===============================================================================
ENGR 133 Program Description 
	Player class, used to contain information regarding player health, inventory
    and to handle player attacks.

Assignment Information
	Assignment:     Individual Project
	Author:         Blake Lowe, lowe77@purdue.edu
	Team ID:        002-10
===============================================================================
'''


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
class Player:
    def __init__(self, name, hp, maxhp):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.rupies = 0
        self.inventory = []
        self.target_name = ""
        self.target_num = ""
        self.isDodging = False
        self.dodgeDuration = 0.5
        self.stopDodgingTime = 0
        
    def isAlive(self):
        return self.hp > 0
    
    def isEngaged(self, Enemy):
        if self.target_name.lower() == Enemy.name.lower() and self.target_num.lower() == Enemy.num.lower():
            return True
        else:
            return False

    def engage(self, Enemy):
        self.target_name = Enemy.name.lower()
        self.target_num = Enemy.num.lower()
        
    def attack(self, Enemy):
        if "magical sword" in self.inventory:
            Enemy.hp -= 4
            return f"Your magical sword deals 4 damage to {Enemy.name} {Enemy.num}"
        elif "white sword" in self.inventory:
            Enemy.hp -= 2
            return f"Your whte sword deals 2 damage to {Enemy.name} {Enemy.num}"
        elif "sword" in self.inventory:
            Enemy.hp -= 1
            return f"Your sword deals 1 damage to {Enemy.name} {Enemy.num}"
        else:
            return "You can't attack without a sword"


    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
