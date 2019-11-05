class Enemy:
    def __init__(self, name, num, hp):
        self.name = name
        self.num = num
        self.hp = hp

    def is_alive(self):
        return self.hp > 0
    def damage(self, damage):
        hp -= damage
        output = f"{name} {num} took {damage} damage."
        if(not is_alive(self)):
            output += f"\n{name} {num} is dead.
        return output

class Moblin(Enemy):
    def __init__(self, num):
        super().__init__(name="Moblin", num, hp = 2)

    def attack(player):
        if(player.is_targeting(self)):
            return 0, f"Moblin {num} throws a spear at you! Your shield blocks it."
        else:
            return 0.5, f"Moblin {num} throws a spear at you! You lose 0.5 hearts"
        
