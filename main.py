from player import Player
from enemies import Moblin
import tiles
import asyncio
import tkinter as tk
import tkinter.scrolledtext as ScrolledText

#list of commands
#go(move player)
#attack(sword attack on engaged enemy)
#use
#shoot(use bow)
#equip(equip item and auto unequip the one in the slot)
#look(print description of room again)
#examine(give description of object or item)
#pick up/get/grab/take
#inventory

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
    #print(userInput)
    inputWords = userInput.split()

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
    inputBox.bind("<Escape>", escape)
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=480, width=1000, y = 0)
    msgBox.config(state=tk.DISABLED)
    #play()
    
    tk.mainloop()
    
