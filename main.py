from player import Player
from enemies import Moblin
import tiles
import asyncio
import tkinter as tk
import time
import tkinter.scrolledtext as ScrolledText
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from colorama import Fore, Back, Style
import os

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
#dodge (next attack misses)

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

def parseInput(link, userInputz, currentRoom):
    itemDescriptions = {
        "wooden shield":"A simple round shield with a cross emblazoned on it.",
        "sword":"A simple weapon with a wooden blade and a green and gold handle.",
        "white sword":"A metal sword with a blueish crossguard and handle.",
        "magical sword":"A razor-sharp blade gleaming with a luster pure enough to seal away the darkness."
    }
    userInput = userInputz.lower()
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
        #move player based on ojbectWord TODO###########
    elif actionWord in ["engage", "eng", "approach", "app"]:
        try:
            enemy = currentRoom.enemySearch(objectWord, targetWord)
            if enemy:
                link.engage(enemy)
                msgLog(f"Engaged {objectWord} {targetWord}.")
            else:
                msgLog(f"#{objectWord} {targetWord} is not present#")
        except:
            msgLog("##Input eror##")
    elif actionWord in ["disengage", "dis", "run"]:
        link.engage("", "")
        msgLog("Disengaged from all enemies.")
    elif actionWord in ["attack"]:
        enemy = currentRoom.enemySearch(objectWord, targetWord)
        if enemy:
            msgLog(link.attack(enemy))
        else:
            msgLog(f"#{objectWord} {targetWord} is not present#")
    elif actionWord in ["look"]:
        msgLog(currentRoom.intro_text())
        if objectWord:
            msgLog("Use examine to get a description of an object.")
    elif actionWord in ["examine"]:
        try:
            msgLog(itemDescriptions[objectWord])
        except:
            msgLog("#{objectWord} is not in your inventory#")
        

    elif actionWord in ["xyzzy"]:
        link.inventory.append(objectWord)
        msgLog(f"{objectWord} added to inventory.")
    else:
        msgLog("##Command not recognised##")


    msgLog(userInput+"\n")


if __name__ == "__main__":
    #play title screen music
    PlaySound('audio/Intro.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
    #print title ascii text
    os.system('color')
    print(f'''
 {Fore.GREEN}.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
{Fore.GREEN}/ .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\
{Fore.GREEN}\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/ /
{Fore.GREEN} \\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /
{Fore.GREEN} / /\\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\\/ /\\
{Fore.GREEN}/ /\\ \\/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                                                                            /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\{Fore.WHITE}                      ___________________________                       {Fore.GREEN}  / /\\/ /
 {Fore.GREEN}/ /\\/ /{Fore.WHITE}              THE LEGEND OF ——————————————————  /                        {Fore.GREEN} \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/                   {Fore.RED}____{Fore.WHITE}\\{Fore.RED}_{Fore.WHITE}\\    {Fore.RED}______  _   ____{Fore.WHITE}/ / {Fore.RED}__{Fore.GREEN}                        \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                  {Fore.RED}/___  / {Fore.WHITE}\\{Fore.RED}  / ____/ / / |  __ \\ |  \\                       {Fore.GREEN}/\\ \\/ /
{Fore.GREEN} \\/ /\\ \\                    {Fore.RED}/ / {Fore.WHITE}\\ \\{Fore.RED}/ /__   / /  | |{Fore.WHITE}/ {Fore.RED}| ||   \\                    {Fore.GREEN} / /\\/ /
{Fore.GREEN} / /\\/ /                   {Fore.RED}/ /   {Fore.WHITE}\\{Fore.RED}/ ___/  / /   | | {Fore.WHITE}/{Fore.RED}| || |\\ \\                  {Fore.GREEN}  \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/                  {Fore.RED} / /___ / //___ / /___ | |{Fore.WHITE}/{Fore.RED}_| || ___ \\                  {Fore.GREEN}  \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                  {Fore.RED}/_____//______//_____/ |_____/ |_|  \\_\\              {Fore.GREEN}     /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\ {Fore.WHITE}                           \\ \\        / /                           {Fore.GREEN}     / /\\/ /
{Fore.GREEN} / /\\/ / {Fore.WHITE}    ________________________\\_\\______/_/________________________/^^^^|  {Fore.GREEN} \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/   {Fore.WHITE}    ---_____________________________________________________|-&\\\\\\\\||  {Fore.GREEN}  \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\  {Fore.WHITE}                              \\ \\  / /                          \\___/  {Fore.GREEN}   /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\{Fore.WHITE}                                \\ \\/ /                                  {Fore.GREEN}  / /\\/ /
{Fore.GREEN} / /\\/ /  {Fore.WHITE}                               \\  /                                   {Fore.GREEN}  \\ \\/ /\\
{Fore.GREEN}/ /\\ \\/   {Fore.WHITE}                                \\/                                    {Fore.GREEN}   \\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                                                                            /\\ \\/ /
{Fore.GREEN} \\/ /\\/\\--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--/ /\\/ /
{Fore.GREEN} / /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\
{Fore.GREEN}/ /\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\bl/\\ \\
{Fore.GREEN}\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /
{Fore.GREEN} `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'{Fore.WHITE}
''')
    input("< Press enter to continue >")
    #TODO ASK player for name
    playerName = input("REGISTER YOUR NAME\n")
    PlaySound(None, SND_FILENAME)
    
    PlaySound('audio/Overworld.wav', SND_FILENAME)
    PlaySound('audio/OverworldLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
    #open window
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
    
    tk.mainloop()

    link = Player(playerName, 3)
    map = tiles.getOverworldTiles()
    currentTile = map[0][0][1]
    link.inventory.append("wooden sword")

    isPlaying = True
    while isPlaying:
        msgLog(currentTile.intro_text())
        for enemy in currentTile.enemies:
            enemy.nextActionTime+=time.time()