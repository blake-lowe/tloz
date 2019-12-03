import random
import time

class Enemy:
    def __init__(self, num, name, hp, actionSpeed):
        self.name = name
        self.num = num
        self.hp = hp
        self.drops = [None]
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
        super().__init__(number, "Moblin", 2, 4)
        self.drops = [None, None, None, None, None, "heart", "heart", "heart", "heart", "fairy"]

    def action(self, player):
        self.nextActionTime += self.actionSpeed
        accuracy = 50#percent chance of throwing spear on target
        i = random.randint(0, 100)
        if i < accuracy:
            if not player.isDodging:
                if(player.isEngaged(self)):
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
        self.drops = [None, None, None, None, None, "heart", "heart", "heart", "heart", "fairy"]
        self.isJumpAttack = False

    def action(self, player):
        if self.isJumpAttack:
            self.isJumpAttack = False
            self.nextActionTime += self.actionSpeed
            if player.isDodging:
                return f"You dodged Tektite {self.num}."
            else:
                player.hp -= 0.5
                return f"Tektite {self.num} bites you. You lose 0.5 hearts\nYou have {player.hp} hearts remaining."
        i = random.randint(0, 100)
        if i < 33:
            self.nextActionTime += 1.6
            self.isJumpAttack = True
            return f"Tektite {self.num} jumps toward you. Dodge to avoid it's attack!"
        else:
            self.nextActionTime += self.actionSpeed
            if player.isEngaged(self):
                player.target_name = ""
                player.target_num = ""
                return f"Tektite {self.num} jumps away. You are no longer engaged with Tektite {self.num}"
            else:
                return f"Tektite {self.num} jumps through the air."


class Leever(Enemy):
    def __init__(self, number):
        super().__init__(number, "Leever", 0.5, 4)
        self.drops = [None, None, None, None, None, "heart", "heart", "heart", "heart", "fairy"]
        
