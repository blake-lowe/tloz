from player import Player
from enemies import Moblin
import tiles
import asyncio
import tkinter as tk
import tkinter.scrolledtext as ScrolledText

#list of commands
#go(move player) ex. go north, go n, n, s, e, w, u, d
#engage/approach (move toward enemy) ex. engage moblin 1, eng moblin 1, approach moblin 1, app moblin 1
#disengage/run (move away from enemy) ex. disengage moblin 1, dis moblin 1, run from moblin 1, run moblin 1
#attack(sword attack on engaged enemy) ex. attack moblin 1, atk moblin 1
#use ex. use life potion
#shoot(use bow) ex. shoot moblin 1
#equip(equip item and auto unequip the one in the slot) ex. equip bow, equip bomb
#look(print description of room again) ex. look
#examine(give description of object or item) ex. examine bow, 
#take ex. take bow, take rupy
#inventory ex. inventory, i

#connector words: from, on, at, around

def play():
    return

def msgLog(text):
    msgBox.config(state=tk.NORMAL)
    msgBox.insert(tk.END, text)
    msgBox.config(state=tk.DISABLED)
    hi = msgBox.vbar.get()[1]
    msgBox.yview_moveto(hi)
    msgBox.vbar.update()

def key(event):
    parseInput(inputBox.get())
    inputBox.delete(0, 'end')

def escape(event):
    inputBox.delete(0, 'end')

def parseInput(userInput):
    userInput = userInput.lower()
    #remove prepositions
    removeWords = ["from", "on", "at", "around"]
    inputWords = userInput.split()
    for word in inputWords:
        if word in removeWords:
            inputWords.remove(word)
    #assign words to variables
    try:
        actionWord = inputWords[0]
    except:
        actionWord = None
    try:
        objectWord = inputWords[1]
    except:
        objectWord = None
    try:
        targetWord = inputWords[2]
    except:
        targetWord = None

    #switch to correct command
    if actionWord in ["go"]:
        return
        #move player based on ojbectWord
    elif actionWord in ["engage"]:
        return


    #msgLog(userInput+"\n")


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
    inputBox.bind("<Escape>", escape)
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=480, width=1000, y = 0)
    msgBox.config(state=tk.DISABLED)
    #play()
    
    tk.mainloop()
    
