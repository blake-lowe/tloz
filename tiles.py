'''
===============================================================================
ENGR 133 Program Description 
	Tiles class. Used as a data structure to hold information about the map
    including descriptions of environment, items present, enemies present, 
    directions player can move, etc.

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
from point import Point
from enemies import Moblin, Tektite, Leever

class MapTile:
    def __init__(self, pos, description, exitsPos, exitsDescriptions, hiddenExitsPos, hiddenExitsDescriptions, hiddenExitRevealed, enemiez, items, objects, itemText):
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
        self.itemText = itemText
    def intro_text(self):
        outputLines = ""
        #add description
        outputLines += self.description
        if len(self.items)>0:
            outputLines += self.itemText
        outputLines += "\n"
        #add exit descriptions
        for exit in self.exitsDescriptions:
            if exit:
                outputLines += exit + "\n"
        #add hidden exit descriptions if revealed
        i = 0
        
        while i < 6:
            if self.hiddenExitRevealed[i]:
                outputLines += self.hiddenExitsDescriptions[i] + "\n"
            i += 1

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
            if enemy.name.lower() == name.lower() and enemy.num.lower() == num.lower():
                return enemy
        return None

def getOverworldTiles(link):
    w, d, h = 5, 5, 5
    tileList = [[[None for x in range(w)] for y in range(h)] for z in range(d)]#nested loop
    #starting room
    tileList[3][0][1] = MapTile(
        Point(3,0,1),#this tile position
        "You find yourself in a clearing in the forest.",#tile description
        [Point(3,1,1), None, None, None, None, None],#exits
        ["A path through the trees leads to the NORTH.", None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, Point(3,0,0)],#hidden exits
        [None, None, None, None, None, "A cave entrance is cut into the hill leading DOWN."],#hidden exit descriptions
        [False, False, False, False, False, True],#is the hidden exit revealed
        [],#enemies
        [],#items
        [],#objects
        ""
        )
    #old man room
    tileList[3][0][0] = MapTile(
        Point(3,0,0),#this tile position
        "You are in a cave lit by two flames suspended in midair. In between, stands an old man in red robes. ",#tile description
        [None, None, None, None, Point(3,0,1), None],#exits
        [None, None, None, None, "The cave's exit is back UP the way you came.", None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, None],#is the hidden exit revealed
        [],#enemies
        ["sword"],#items
        [],#objects
        "He offers you the \nhilt of a sword saying, \"It's dangerous to go alone! Take this.\""
        )
    #riverbank room (tektites)TODO
    tileList[3][1][1] = MapTile(
        Point(3,1,1),#this tile position
        "You arrive at the bank of a river, running too quickly to swim across.",#tile description
        [None, None, Point(3,0,1), Point(2,1,1), None, None],#exits
        [None, None, "The path to the forest lays to the SOUTH", "The riverbank continues to the WEST.", None, None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [Tektite("1"), Tektite("2")],#enemies
        [],#items
        [],#objects
        ""
        )
    #moblin room (bridge)
    tileList[2][1][1] = MapTile(
        Point(2,1,1),#this tile position
        "You come to a bridge.",#tile description
        [Point(2,2,1), Point(3,1,1), None, None, None, Point(2,1,0)],#exits
        ["The bridge leads to an island to the NORTH.", "The riverbank continues to the EAST.", None, None, None, "There is a cave entrance here leading DOWN."],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [Moblin("1"), Moblin("2")],#enemies
        [],#items
        [],#objects
        ""
        )
    tileList[2][1][0] = MapTile(
        Point(2,1,0),#this tile position
        "You are in a cave lit by two flames suspended in midair. In between, stands an old man in red robes. ",#tile description
        [None, None, None, None, Point(2,1,1), None],#exits
        [None, None, None, None, "The cave's exit is back UP the way you came.", None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [],#enemies
        ["heart container", "life potion"],#items
        [],#objects
        "He gestures toward a heart container and a life potion, \"Take any one you want.\""
        )
    #final fight room (leever)#TODO
    tileList[2][2][1] = MapTile(
        Point(2,2,1),#this tile position
        "The bridge connects to the island at a small sandy beach.",#tile description
        [Point(2,3,1), None, None, None, None, None],#exits
        ["You can see a castle in the distance to the NORTH", None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [Leever("1"), Tektite("1"), Tektite("2")],#enemies
        [],#items
        [],#objects
        ""
        )

    #zelda room (here's all 8 units of the triforce of wisdom. Ganon lays dead on the ground)
    tileList[2][3][1] = MapTile(
        Point(2,3,1),#this tile position
        f"Inside the castle, Princess Zelda waits for you. She says,\" '{link.name}'! You must have been asleep for a long time. I defeated \n'Gannon,' took back the Triforce with Power, and collected the units of the Triforce with Wisdom.\" ",#tile description
        [None, None, None, None, None, None],#exits
        [None, None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [],#enemies
        [],#items
        [],#objects
        ""
    )
    #test room INACCESSIBLE
    tileList[0][0][4] = MapTile(
        Point(0,0,4),#this tile position
        "##TEST ROOM##",#tile description
        [None, None, None, None, None, None],#exits
        [None, None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [Leever("1")],#enemies
        [],#items
        [],#objects
        ""
        )
    return tileList

def getLvl1Tiles():
    tileList = [6][6]
    return tileList

#template for new tiles
'''
    tileList[x][x][x] = MapTile(
        Point(x,x,x),#this tile position
        "",#tile description
        [None, None, None, None, None, None],#exits
        [None, None, None, None, None, None],#exit descriptions
        [None, None, None, None, None, None],#hidden exits
        [None, None, None, None, None, None],#hidden exit descriptions
        [False, False, False, False, False, False],#is the hidden exit revealed
        [],#enemies
        [],#items
        [],#objects
        ""
        )
'''