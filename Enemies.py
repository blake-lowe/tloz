'''
===============================================================================
ENGR 133 Program Description 
	Enemies class, which handles instancing of enemies and control of their 
    actions.

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
import random
import time

class Enemy:
    def __init__(self, num, name, hp, actionSpeed, actionDelay):
        self.name = name
        self.num = str(num)
        self.hp = hp
        self.drops = [None]
        self.actionSpeed = actionSpeed#seconds per action
        self.nextActionTime = actionSpeed*random.random()
        self.actionDelay = actionDelay
        self.isAttackable = True

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
        super().__init__(number, "Moblin", 2, 4, 4)
        self.drops = ["rupy", "rupy", "rupy", "rupy", "rupy", "heart", "heart", "heart", "heart", "fairy"]

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
        super().__init__(number, "Tektite", 0.5, 4, 1)
        self.drops = ["rupy", "rupy", "rupy", "rupy", "rupy", "heart", "heart", "heart", "heart", "fairy"]
        self.isJumpAttack = False

    def action(self, player):
        if self.isJumpAttack:
            self.isJumpAttack = False
            self.nextActionTime += self.actionSpeed
            if player.isDodging:
                return f"You dodged Tektite {self.num}."
            else:
                player.hp -= 0.5
                return f"Tektite {self.num} bites you! You lose 0.5 hearts\nYou have {player.hp} hearts remaining."
        i = random.randint(0, 100)
        if i < 33:
            self.nextActionTime += 1.75
            self.isJumpAttack = True
            return f"Tektite {self.num} jumps toward you. DODGE to avoid it's attack!"
        else:
            self.nextActionTime += self.actionSpeed
            if player.isEngaged(self):
                player.target_name = ""
                player.target_num = ""
                return f"Tektite {self.num} jumps away. You are no longer engaged with Tektite {self.num}"
            else:
                return f"Tektite {self.num} jumps around."


class Leever(Enemy):
    def __init__(self, number):
        super().__init__(number, "Leever", 4, 4, 4)
        self.drops = ["rupy", "rupy", "rupy", "rupy", "rupy", "5 rupies", "5 rupies", "clock", "heart", "heart"]
        self.isAttackable = True

    def burrow(self, player):
        self.isAttackable = False
        if player.isEngaged(self):
            player.target_name = ""
            player.target_num = ""
            return f"Leever {self.num} burrows into the ground. You are no longer engaged with Leever {self.num}"
        else:
            return f"Leever {self.num} burrows into the ground."

    def action(self, player):
        self.nextActionTime += self.actionSpeed
        if not self.isAttackable:
            if random.random() < .5:
                player.target_name = self.name
                player.target_num = self.num
                self.isAttackable = True
                return f"Leever {self.num} surfaces in front of you. You are now engaged with Leever {self.num}."
            else:
                self.isAttackable = True
                return f"Leever {self.num} surfaces."
        else:
            if player.isEngaged(self):
                if random.random() < .5:
                    if not player.isDodging:
                        player.hp -= 1
                        return f"Leever {self.num} attacks you! You lose 1 heart.\nYou have {player.hp} hearts remaining."
                    else:
                        return f"You dodged Leever {self.num}."
                else:
                    return self.burrow(player)
            else:
                return self.burrow(player)
