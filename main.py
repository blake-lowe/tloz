from player import Player
from enemies import Moblin

def play():
    link = Player("Zelda", 6)
    mob1 = Moblin(1)
    output = mob1.attack(link)
    print(output)
    print(link.hp)
    link.target(mob1)
    output = mob1.attack(link)
    print(output)
    print(link.hp)
    

if __name__ == "__main__":
    play()
