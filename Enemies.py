import random
import time

class Enemy:
    def __init__(self, num, name, hp, actionSpeed):
        self.name = name
        self.num = num
        self.hp = hp
        self.actionSpeed = actionSpeed
        self.r = random.seed(time.time())
        self.nextActionTime = actionSpeed*r.random()

    def is_alive(self):
        return self.hp > 0
    def damage(self, damage):
        hp -= damage
        output = f"{name} {num} took {damage} damage."
        if(not is_alive(self)):
            output += f"\n{name} {num} is dead."
        return output

class Moblin(Enemy):
    def __init__(self, num):
        super().__init__(self, num, name="Moblin", hp = 2, actionSpeed = 1)

    def attack(self, player):
        accuracy = 50#percent chance of throwing spear on target
        i = self.r.randint(0, 100)
        if i < accuracy:
            if(player.is_engaged(self)):
                return f"Moblin {self.num} throws a spear at you! Your shield blocks it."
            else:
                player.hp-=0.5
                return f"Moblin {self.num} throws a spear at you! You lose 0.5 hearts."
        elif i > accuracy:
            return f"Moblin {self.num} throws a spear at you! It misses."
        
