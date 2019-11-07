import items, enemies

class MapTile:
    def __init__(self, x, y, description, exits, enemies, items):
        self.x = x
        self.y = y
        self.exits = exits
        self.enemies = enemies
        self.items = items
    def intro_text(self):
        raise NotImplementedError()
    def modify_player(self, player):
        return

def getOverworldTiles():
    tileList = [2][2]
    tileList[0][0] = MapTile(
        0,0,
        "You find yourself in a clearing in the forest. A cave entrance is cut into the hill to northwest.",
        ["north"],
        []
        []
        )
    return tileList

def getLvl1Tiles():
    tileList = [6][6]
    return tileList

def getSecretTiles():
    tileList = [5][5]
    tileList[0][0] = None
    return tileList

    
