from player import Player
from enemies import Moblin
import tiles
import asyncio
import tkinter as tk
import tkinter.scrolledtext as ScrolledText

def play():
    '''
    link = Player("Zelda", 6)
    mob1 = Moblin(1)
    output = mob1.attack(link)
    print(output)
    print(link.hp)
    link.target(mob1)
    output = mob1.attack(link)
    print(output)
    print(link.hp)
    '''
    '''
    overworld = tiles.getOverworldTiles()
    currentTile = overworld[0][0][1]
    currentTile.intro_text()
    '''

async def userInput():
    while True:
        x = input(">")

async def enemyActions():
    while True:
        await asyncio.sleep(1)
        print("oof")

if __name__ == "__main__":
    #play()
    #asyncio.run(enemyActions())
    #asyncio.run(userInput())
    root = tk.Tk()
    root.resizable(False, False)
    canvas1 = tk.Canvas(root)
    root.geometry("1000x500")
    #canvas1.pack_propagate(0)
    #canvas1.pack()

    inputBox = tk.Entry(root)
    inputBox.pack()
    inputBox.place(bordermode=tk.OUTSIDE, height=20, width=1000, y = 480)
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=480, width=1000, y = 0)
    
    tk.mainloop()
    
