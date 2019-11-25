from point import Point
import items
import enemies

class MapTile:
    def __init__(self, pos, description, exitsPos, exitsDescriptions, hiddenExitsPos, hiddenExitsDescriptions, hiddenExitRevealed, enemies, items, objects):
        self.pos = pos
        self.description = description
        self.exitsPos = exitsPos#[North, East, South, West, Up, Down]
        self.exitsDescriptions = exitsDescriptions
        self.hiddenExitsPos = hiddenExitsPos
        self.hiddenExitsDescriptions = hiddenExitsDescriptions
        self.hiddenExitRevealed = hiddenExitRevealed
        self.enemies = enemies
        self.items = items
        self.objects = objects
    def intro_text(self):
        print(self.description)
        for exit in self.exitsDescriptions:
            if exit:
                print(exit)
        for i in range(0, 6):
            if self.hiddenExitRevealed[i]:
                print(self.hiddenExitsDescriptions[i])
    #def modify_player(self, player):
        #return

def getOverworldTiles():
    w, d, h = 2, 2, 2
    tileList = [[[None for x in range(w)] for y in range(h)] for z in range(d)]
    tileList[0][0][1] = MapTile(
        Point(0,0,1),
        "You find yourself in a clearing in the forest.",
        [Point(0,1,1), None, None, None, None, None],
        ["A path through the trees leads to the north.", None, None, None, None, None],
        [None, None, None, None, None, Point(0,0,0)],
        [None, None, None, None, None, "A cave entrance is cut into the hill leading down."],
        [False, False, False, False, False, True],
        [],
        [],
        []
        )
    return tileList

def getLvl1Tiles():
    tileList = [6][6]
    return tileList