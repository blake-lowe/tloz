class Player:
    def __init__(self, name, hp, maxhp):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.inventory = []
        self.target_name = ""
        self.target_num = ""
        self.isDodging = False
        self.dodgeDuration = 0.35
        self.stopDodgingTime = 0
        
    def is_alive(self):
        return self.hp > 0
    
    def is_engaged(self, Enemy):
        if self.target_name == Enemy.name and self.target_num == Enemy.num:
            return True
        else:
            return False

    def engage(self, Enemy):
        self.target_name = Enemy.name
        self.target_num = Enemy.num
        
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
    
