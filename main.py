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

def msgLog(text):
    msgBox.config(state=tk.NORMAL)
    msgBox.insert(tk.END, text)
    msgBox.config(state=tk.DISABLED)
    lo = msgBox.vbar.get()[0]
    hi = msgBox.vbar.get()[1]
    barSize = hi-lo
    print(barSize)
    #msgBox.vbar.set(1.0-barSize, 1.0)
    msgBox.yview_moveto(hi)
    msgBox.vbar.update()
    print(msgBox.vbar.get())

def key(event):
    #print("pressed return")
    parseInput(inputBox.get())
    inputBox.delete(0, 'end')

def parseInput(userInput):
    #print(userInput)
    msgLog(userInput+"\n")


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    canvas1 = tk.Canvas(root)
    
    root.geometry("1000x500")
    root.title("The Legend of Zelda")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
    inputBox = tk.Entry(root)
    inputBox.pack()
    inputBox.place(bordermode=tk.OUTSIDE, height=20, width=1000, y = 480)
    inputBox.bind("<Return>", key)
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=480, width=1000, y = 0)
    msgBox.config(state=tk.DISABLED)
    #play()
    
    tk.mainloop()
    
