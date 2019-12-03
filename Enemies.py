import random
import time

class Enemy:
    def __init__(self, num, name, hp, actionSpeed):
        self.name = name
        self.num = num
        self.hp = hp
        self.drops = []
        self.actionSpeed = actionSpeed#seconds per action
        self.nextActionTime = actionSpeed*random.random()

    def is_alive(self):
        return self.hp > 0
    def damage(self, damage):
        hp -= damage
        output = f"{name} {num} took {damage} damage."
        if(not is_alive(self)):
            output += f"\n{name} {num} is dead."
        return output

class Moblin(Enemy):
    def __init__(self, number):
        super().__init__(number, "moblin", 2, 4)
        self.drops = [None, None, None, None, None, "heart", "heart", "heart", "heart", "fairy"]

    def action(self, player):
        accuracy = 50#percent chance of throwing spear on target
        i = random.randint(0, 100)
        if i < accuracy:
            if not player.isDodging:
                if(player.is_engaged(self)):
                    return f"Moblin {self.num} throws a spear at you! Your shield blocks it."
                else:
                    player.hp-=0.5
                    return f"Moblin {self.num} throws a spear at you! You lose 0.5 hearts.\nYou have {player.hp} hearts remaining."
            else:
                return f"Moblin {self.num} throws a spear at you! You dodge out of the way."
        elif i > accuracy:
            return f"Moblin {self.num} throws a spear at you! It misses."

class Tektite(Enemy):
    def __init__(self, number):
        super().__init__(number, "Tektite", 0.5, 4)
        self.drops = [None, "heart"]        
        
