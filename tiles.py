import point
import items
import enemies

class MapTile:
    def __init__(self, pos, description, exitsPos, enemies, items, objects, secretPos, isSecretRevealed, secretDescription):
        self.pos = pos
        self.exits = exits#[North, East, South, West]
        self.enemies = enemies
        self.items = items
        self.objects = objects
        self.secretPos = secretPos
        self.isSecretRevealed = isSecretRevealed
        self.secretDescription = secretDescription
    def intro_text(self):
        print("description")
        if isSecretRevealed:
            print(secretDescription)
    def modify_player(self, player):
        return
    def secretRevealedCheck():
        if secretPos != None:
            raise NotImplementedError

def getOverworldTiles():
    tileList = [2][2]
    tileList[0][0] = MapTile(
        Point(0,0),
        "You find yourself in a clearing in the forest. A path through the trees leads to the north.",
        [Point(0,1), None, None, None],
        [],
        [],
        [],
        Point(0,0),
        True,
        "A cave entrance is cut into the hill to the northwest."
        )
    return tileList

def getLvl1Tiles():
    tileList = [6][6]
    return tileList

def getSecretTiles():
    tileList = [5][5]
    tileList[0][0] = None
    return tileList

    
