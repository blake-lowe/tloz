from point import Point
import enemies

class MapTile:
    def __init__(self, pos, description, exitsPos, exitsDescriptions, hiddenExitsPos, hiddenExitsDescriptions, hiddenExitRevealed, enemiez, items, objects):
        self.pos = pos
        self.description = description
        self.exitsPos = exitsPos#[North, East, South, West, Up, Down]
        self.exitsDescriptions = exitsDescriptions
        self.hiddenExitsPos = hiddenExitsPos
        self.hiddenExitsDescriptions = hiddenExitsDescriptions
        self.hiddenExitRevealed = hiddenExitRevealed
        self.enemiez = enemiez
        self.items = items
        self.objects = objects
    def intro_text(self):
        outputLines = ""
        #add description
        outputLines += self.description + "\n"
        #add exit descriptions
        for exit in self.exitsDescriptions:
            if exit:
                outputLines += exit + "\n"
        #add hidden exit descriptions if revealed
        for i in range(0, 6):
            if self.hiddenExitRevealed[i]:
                outputLines += self.hiddenExitsDescriptions[i] + "\n"
        #add items if present
        if self.items:
            outputLines += "The following items are present:\n"
        for item in self.items:
            outputLines += item+"\n"
        #add enemies if present
        if self.enemiez:
            outputLines += "The following enemies are present:\n"
        for enemy in self.enemiez:
            outputLines += enemy.name + " " + enemy.num + "\n"
        return outputLines

    def enemySearch(self, name, num):
        for enemy in self.enemiez:
            if enemy.name == name and enemy.num == num:
                return enemy
        return None

def getOverworldTiles():
    w, d, h = 2, 2, 2
    tileList = [[[None for x in range(w)] for y in range(h)] for z in range(d)]
    #starting room
    tileList[0][0][1] = MapTile(
        Point(0,0,1),#this tile position
        "You find yourself in a clearing in the forest.",#tile description
        [Point(0,1,1), None, None, None, None, None],#exits
        ["A path through the trees leads to the north.", None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, Point(0,0,0)],#hidden exits
        [None, None, None, None, None, "A cave entrance is cut into the hill leading down."],#hidden exit descriptions
        [False, False, False, False, False, True],#is the hidden exit revealed
        [],#enemies
        [],#items
        []#objects
        )
    #old man room
    tileList[0][0][0] = MapTile(
        Point(0,0,0),#this tile position
        "You are in a cave lit by two flames suspended in midair. In between, stands an old man in red robes. He offers you the \nhilt of a sword saying, \"It's dangerous to go alone! Take this.\"",#tile description
        [None, None, None, None, Point(0,0,1), None],#exits
        [None, None, None, None, "The cave's exit is back up the way you came.", None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, None],#is the hidden exit revealed
        [],#enemies
        ["sword"],#items
        []#objects
        )
    return tileList

def getLvl1Tiles():
    tileList = [6][6]
    return tileList