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

########### SCROLL TO BOTTOM FOR MAIN METHOD ##################

#list of planned commands
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

#connector words(removed from input): from, on, at, around

global link
global map
global currentTile
global startTime
global currentTime
global isIntroFinished
global isLinkDead

def msgLog(text):
    msgBox.config(state=tk.NORMAL)#make text box editable
    msgBox.insert(tk.END, text)#add text to box
    msgBox.insert(tk.END, "\n")#add escape character
    msgBox.config(state=tk.DISABLED)#make text box uneditable
    #scroll to bottom of box
    hi = msgBox.vbar.get()[1]
    msgBox.yview_moveto(hi)
    msgBox.vbar.update()

def key(event):#when the enter key is pressed
    parseInput(link, inputBox.get(), currentTile)#pass input to function below
    inputBox.delete(0, 'end')

def escape(event):
    inputBox.delete(0, 'end')

def parseInput(link, userInputz, currentTile):
    if isLinkDead:
        msgLog(f"{link.name} is dead. Darkness covers the land.")
        return
    msgLog(">"+userInputz)
    #define item descriptions
    itemDescriptions = {
        "wooden shield":"A simple round shield with a cross emblazoned on it.",
        "sword":"A simple weapon with a rusted blade and a green and gold handle.",
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
    if len(inputWords) > 3:
        msgLog("# Phrase contained more than 3 words. #")
        return
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
        #move player based on objectWord TODO###########
    elif actionWord in ["engage", "eng", "approach", "app"]:
        try:
            enemy = currentTile.enemySearch(objectWord, targetWord)
            if enemy:
                link.engage(enemy)
                msgLog(f"Engaged {objectWord} {targetWord}.")
            else:
                msgLog(f"# {objectWord} {targetWord} is not present. #")
        except:
            msgLog("## Input error. ##")
    elif actionWord in ["disengage", "dis", "run"]:
        link.engage("", "")
        msgLog("Disengaged from all enemies.")
    elif actionWord in ["attack"]:
        enemy = currentTile.enemySearch(objectWord, targetWord)
        if enemy:
            msgLog(link.attack(enemy))
        else:
            msgLog(f"# {objectWord} {targetWord} is not present. #")
    elif actionWord in ["look"]:
        msgLog(currentTile.intro_text())
        if objectWord:
            msgLog("Use examine to get a description of an object.")
    elif actionWord in ["examine"]:
        item = ""
        if targetWord:
            item = objectWord + ' ' + targetWord
        else:
            item = objectWord
        if  item in link.inventory:
            try:
                msgLog(itemDescriptions[item])
            except:
                msgLog(f"## Description for {item} not found. ##")
        else:
            msgLog(f"# {item} is not in your inventory. #")

    elif actionWord in ["inventory"]:
        msgLog(link.inventory)

    elif actionWord in ["xyzzy"]:
        item = ""
        if targetWord:
            item = objectWord + ' ' + targetWord
        else:
            item = objectWord
        link.inventory.append(item)
        msgLog(f"{item} added to inventory.")

    elif actionWord in ["suicide"]:
        link.hp = 0
        isLinkDead = True
        endGame()
    else:
        msgLog("## Command not recognised. ##")

def endGame():
    msgLog("===============")
    msgLog("   GAME OVER   ")
    msgLog("===============")
    PlaySound(None, SND_FILENAME)
    PlaySound('audio/GameOver.wav', SND_FILENAME)



def gameloop():
    global currentTime
    global isIntroFinished
    currentTime = time.time()-startTime
    #msgLog(currentTime)
    

    if (currentTime > 6.798) and (not isIntroFinished):
        isIntroFinished = True
        if isLinkDead:
            PlaySound('audio/OverworldLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
        else:
            PlaySound('audio/GameOverLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
    root.after(50, gameloop)




############ MAIN METHOD #############
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
    #get player name
    input("< Press enter to continue >")
    playerName = input("REGISTER YOUR NAME\n")
    link = Player(playerName, 3)
    #import map
    map = tiles.getOverworldTiles()
    currentTile = map[0][0][1]
    #set starting inventory
    link.inventory.append("wooden shield")
    #stop title screen music
    PlaySound(None, SND_FILENAME)
    #specify window details
    root = tk.Tk()
    root.resizable(False, False)
    canvas1 = tk.Canvas(root)
    #set dimensions
    root.geometry("1000x500")
    #change window title and icon
    root.title("The Legend of Zelda")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
    #add input field
    inputBox = tk.Entry(root)
    inputBox.pack()
    inputBox.place(bordermode=tk.OUTSIDE, height=20, width=1000, y = 480)
    inputBox.bind("<Return>", key)
    inputBox.bind("<Escape>", escape)
    #add output box with scroll bar
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=480, width=1000, y = 0)
    msgBox.config(state=tk.DISABLED)
    #bring window to front
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    #initialize global variables
    startTime = time.time()
    currentTime = 0
    isLinkDead = False
    #start main game music
    PlaySound('audio/Overworld.wav', SND_FILENAME|SND_ASYNC)
    global isIntroFinished
    isIntroFinished = False
    #start gameloop
    root.after(0, gameloop)
    #open window
    tk.mainloop()
    ## END MAIN ##