'''
===============================================================================
ENGR 133 Program Description 
	Main method, handle the gameloop, user input, and conditions for the end of the game

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

from player import Player
from enemies import Moblin
import tiles
from point import Point
import random
import tkinter as tk
import time
import tkinter.scrolledtext as ScrolledText
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from colorama import Fore, Back, Style
import os

########### SCROLL TO BOTTOM FOR MAIN METHOD ##################

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

#connector words(removed from input): from, on, at, around

global link
global map
global currentTile
global startTime
global currentTime
global isIntroFinished
global isLinkDead
global isGameWon

#log messages to the ouput window
def msgLog(text):
    msgBox.config(state=tk.NORMAL)#make text box editable
    msgBox.insert(tk.END, text)#add text to box
    if not (text.endswith("\n")):
        msgBox.insert(tk.END, "\n")#add escape character if there's not already one
    msgBox.config(state=tk.DISABLED)#make text box uneditable
    #scroll to bottom of box
    hi = msgBox.vbar.get()[1]
    msgBox.yview_moveto(hi)
    msgBox.vbar.update()

#triggered when the enter key is pressed
def key(event):
    temp = inputBox.get()
    inputBox.delete(0, 'end')
    parseInput(temp)#pass input to function below


#triggered when the escape key is pressed
def escape(event):
    inputBox.delete(0, 'end')

## handle commands input to entry box ##
def parseInput(userInputz):
    global isLinkDead
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
    #check fo reasons to not run command
    if isLinkDead:
        msgLog(f"{link.name} is dead. Darkness covers the land.")
        if not actionWord in ["quit", "exit"]:
            return
    if isGameWon:
        msgLog(f"Thanks '{link.name}', you're the hero of Hyrule.")
        msgLog(f"Finally peace returns to Hyrule.")
        msgLog(f"This ends the story.")
        if not actionWord in ["quit", "exit"]:
            return
    if len(inputWords) > 3:
        msgLog("# Phrase contained more than 3 words. #")
        return
    #switch to correct command
    #go
    if actionWord in ["go"]:
        global currentTile
        directions = {
            "north":0,
            "east":1, 
            "south":2, 
            "west":3, 
            "up":4, 
            "down":5
        }
        try:
            direction = directions[objectWord]
        except:
            msgLog("# Specified direction is invalid. Try North, East, South, West, Up, or Down. #")
            return
        
        if currentTile.exitsPos[direction]:
            for enemy in currentTile.enemiez:
                enemy.action(link)
            newPos = currentTile.exitsPos[direction]
            currentTile = map[newPos.x][newPos.y][newPos.z]
            initTile()
        else:
            if currentTile.hiddenExitsPos[direction] and currentTile.hiddenExitRevealed[direction]:
                for enemy in currentTile.enemiez:
                    enemy.action(link)
                newPos = currentTile.hiddenExitsPos[direction]
                currentTile = map[newPos.x][newPos.y][newPos.z]
                initTile()
            else:
                msgLog("# You can't go that way. #")
    #engage
    elif actionWord in ["engage", "eng", "approach", "app"]:
        try:
            enemy = currentTile.enemySearch(objectWord, targetWord)
            if enemy:
                if enemy.isAttackable:
                    link.engage(enemy)
                    msgLog(f"Engaged {objectWord} {targetWord}.")
                else:
                    msgLog(f"# {enemy.name} {enemy.num} is not reachable. #")
            else:
                msgLog(f"# {objectWord} {targetWord} is not present. #")
        except:
            msgLog("## Input error. ##")
    #disengage
    elif actionWord in ["disengage", "dis", "run"]:
        link.target_name = ""
        link.target_num = ""
        msgLog("Disengaged from all enemies.")
    #attack
    elif actionWord in ["attack"]:
        if not(("sword" in link.inventory) or ("white sword" in link.inventory) or ("magical sword" in link.inventory)):
            msgLog("# You cannot attack without a sword. #")
            return
        if not objectWord:
            msgLog("# Must specify enemy type #")
            return
        enemy = currentTile.enemySearch(objectWord, targetWord)
        if enemy:
            if not enemy.isAttackable:
                msgLog(f"# {enemy.name} {enemy.num} is not reachable. #")
                return
            if link.hp == link.maxhp:
                msgLog(f"An image of your sword flies toward {objectWord} {targetWord}")
                swordBeamDmg = 1
                enemy.hp -= swordBeamDmg
                msgLog(f"Your sword beam deals {swordBeamDmg} damage to {objectWord} {targetWord}")
                if enemy.hp > 0:
                    msgLog(f"{objectWord} {targetWord} has {enemy.hp} health.")
            if link.isEngaged(enemy):
                msgLog(link.attack(enemy))
                if enemy.hp > 0:
                    msgLog(f"{objectWord} {targetWord} has {enemy.hp} health.")
            else:
                msgLog(f"You must be engaged with {objectWord} {targetWord} to hit it with your sword.")
        else:
            if objectWord in ["old"] and currentTile.pos.z == 0:
                msgLog("The flames beside the old man flare up and shoot fireballs at you!")
                link.hp -= 1
                msgLog(f"You lose 1 heart. You have {link.hp} hearts remaining.")
            else:
                msgLog(f"# {objectWord} {targetWord} is not present. #")
                #dodge
    elif actionWord in ["dodge"]:
        link.isDodging = True
        link.stopDodgingTime = currentTime + link.dodgeDuration
    #take
    elif actionWord in ["take", "get"]:
        item = ""
        if targetWord:
            item = objectWord + ' ' + targetWord
        else:
            item = objectWord
        if item in currentTile.items:
            if item == "heart container":
                link.maxhp += 1
                link.hp += 1
                msgLog(f"Heart container used. Your maximum hearts has been increased to {link.maxhp}. You currently have {link.hp} hearts.\nThe life potion disappeared.")
                if "life potion" in currentTile.items:
                    currentTile.items.remove("life potion")
            elif item == "life potion":
                link.hp = link.maxhp
                msgLog(f"All hearts recovered. You currently have {link.hp} hearts.\nThe heart container disappeared.")
                if "heart container" in currentTile.items:
                    currentTile.items.remove("heart container")
            elif item == "heart":
                link.hp += 1
                if link.hp > link.maxhp:
                    link.hp = link.maxhp
                msgLog(f"One heart recovered. You currently have {link.hp} hearts.")
            elif item == "fairy":
                link.hp = link.maxhp
                msgLog(f"All hearts recovered. You currently have {link.hp} hearts.")
            elif item == "rupy":
                link.rupies += 1
                msgLog(f"One rupy added. You currently have {link.rupies} rupies.")
            elif item == "5 rupies":
                link.rupies += 5
                msgLog(f"5 rupies added. You currently have {link.rupies} rupies.")
            elif item == "clock":
                for enemy in currentTile.enemiez:
                    enemy.nextActionTime += 100000
                msgLog("All enemies have been frozen in place.")
            else:
                msgLog(f"{item} added to your inventory.")
                link.inventory.append(item)
                PlaySound('audio/Item.wav', SND_FILENAME)
                PlaySound('audio/OverworldLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
            currentTile.items.remove(item)
        else:
            msgLog(f"# {item} is not present. #")
    #use
    elif actionWord in ["use"]:
        item = ""
        if targetWord:
            item = objectWord + ' ' + targetWord
        else:
            item = objectWord
        if item in link.inventory:
            if item == "heart container":
                link.maxhp += 1
                link.hp += 1
                msgLog(f"Heart container used. Your maximum hearts has been increased to {link.maxhp}. You currently have {link.hp} hearts.")
                link.inventory.remove(item)
            elif item == "life potion":
                link.hp = link.maxhp
                msgLog(f"Hearts increased to maximum of {link.hp}.")
                link.inventory.remove(item)
            elif item == "fairy":
                link.hp = link.maxhp
                msgLog(f"All hearts recovered. You currently have {link.hp} hearts.")
            elif item == "heart":
                link.hp += 1
                if link.hp > link.maxhp:
                    link.hp = link.maxhp
                msgLog(f"One heart recovered. You currently have {link.hp} hearts.")
            elif item == "rupy":
                link.rupies += 1
                msgLog(f"One rupy added. You currently have {link.rupies} rupies.")
            elif item == "5 rupies":
                link.rupies += 5
                msgLog(f"5 rupies added. You currently have {link.rupies} rupies.")
            elif item == "clock":
                for enemy in currentTile.enemiez:
                    enemy.nextActionTime += 100000
                msgLog("All enemies have been frozen in place.")
            else:
                msgLog(f"# {item} is not useable. #")
        else:
            msgLog(f"# {item} is not in your inventory. #")
    #status
    elif actionWord in ["status", "hp", "health", "rupies"]:
        msgLog(f"You currently have {link.hp} hearts out of {link.maxhp} maximum hearts, and {link.rupies} rupies.")
    #look
    elif actionWord in ["look"]:
        msgLog(currentTile.intro_text())
        if objectWord:
            msgLog("Use examine to get a description of an object.")
    #examine
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
    #inventory
    elif actionWord in ["inventory"]:
        link.inventory.sort()
        msgLog("You have the following items in your inventory:")
        for item in link.inventory:
            msgLog(item)
    #give
    elif actionWord in ["xyzzy"]:
        item = ""
        if targetWord:
            item = objectWord + ' ' + targetWord
        else:
            item = objectWord
        link.inventory.append(item)
        msgLog(f"{item} added to inventory.")
    #teleport
    elif actionWord in ["warp"]:
        x = int(objectWord[0])
        y = int(objectWord[1])
        z = int(objectWord[2])
        newTile = map[x][y][z]
        if newTile:
            msgLog(f"Warped to {x} {y} {z}.")
            currentTile = newTile
            initTile()
        else:
            msgLog(f"{x} {y} {z} not found.")

    #debug coordinates
    elif actionWord in ["coords"]:
        msgLog(f"{currentTile.pos.x},{currentTile.pos.y},{currentTile.pos.z}")
    #selfdamage
    elif actionWord in ["selfdamage"]:
        try:
            damage = int(objectWord)
            if damage:
                link.hp -= damage
                msgLog(f"Lost {damage} hearts. You currently have {link.hp} hearts.")
                
        except:
            msgLog("## Input Error ##")
    #selfheal
    elif actionWord in ["selfheal"]:
        try:
            damage = int(objectWord)
            if damage:
                link.hp += damage
                if link.hp > link.maxhp:
                    link.hp = link.maxhp
                msgLog(f"Recovered {damage} hearts. You currently have {link.hp} hearts.")
        except:
            msgLog("## Input Error ##")
    #suicide
    elif actionWord in ["killplayer"]:
        #link.hp = 0
        isLinkDead = True
        endGame()
    elif actionWord in ["ping"]:
        msgLog("pong")
    #help
    elif actionWord in ["help"]:
        msgLog("# Refer to the user manual for a list of commands. #")
    #quit
    elif actionWord in ["quit", "exit"]:
        msgLog("Quitting...")
        quit()
    #not recognised
    else:
        msgLog("## Command not recognised. ##")

#display game over message and change music
def endGame():
    inputBox.delete(0, 'end')
    msgLog("===============")
    msgLog("   GAME OVER   ")
    msgLog("===============")
    PlaySound(None, SND_FILENAME)
    PlaySound('audio/GameOver.wav', SND_FILENAME)

def winGame():#method called upon successful completion of game
    inputBox.delete(0, 'end')
    msgLog("")
    msgLog(f"Thanks '{link.name}', you're the hero of Hyrule.")
    msgLog(f"Finally peace returns to Hyrule.")
    msgLog(f"This ends the story.")
    msgLog(
        '''
 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
/ .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\
\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/ /
 \\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /
 / /\\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\\/ /\\
/ /\\ \\/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\ \\/\\ \\
\\ \\/\\ \\                                                                            /\\ \\/ /
 \\/ /\\ \\                      ___________________________                         / /\\/ /
 / /\\/ /              THE LEGEND OF ——————————————————  /                        \\ \\/ /\\
/ /\\ \\/                   ____\\_\\    ______  _   ____/ / __                        \\ \\/\\ \\
\\ \\/\\ \\                  /___  / \\  / ____/ / / |  __ \\ |  \\                       /\\ \\/ /
 \\/ /\\ \\                    / / \\ \\/ /__   / /  | |/ | ||   \\                     / /\\/ /
 / /\\/ /                   / /   \\/ ___/  / /   | | |  || |\\ \\                    \\ \\/ /\\
/ /\\ \\/                   / /___ / //___ / /___ | |/_| || ___ \\                    \\ \\/\\ \\
\\ \\/\\ \\                  /_____//______//_____/ |_____/ |_|  \\_\\                   /\\ \\/ /
 \\/ /\\ \\                            \\ \\        / /                                / /\\/ /
 / /\\/ /     ________________________\\_\\______/_/________________________/^^^^|   \\ \\/ /\\
/ /\\ \\/       ---_____________________________________________________|-&\\\\\\\\||    \\ \\/\\ \\
\\ \\/\\ \\                                \\ \\  / /                          \\___/     /\\ \\/ /
 \\/ /\\ \\                                \\ \\/ /                                    / /\\/ /
 / /\\/ /                                 \\  /                                     \\ \\/ /\\
/ /\\ \\/                                   \\/                                       \\ \\/\\ \\
\\ \\/\\ \\                                                                            /\\ \\/ /
 \\/ /\\/\\--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--/ /\\/ /
 / /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\
/ /\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\bl/\\ \\
\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `'\\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'

'''
    )
    PlaySound('audio/Ending.wav', SND_FILENAME|SND_ASYNC)

#get a tile ready for player entry
def initTile():
    msgLog(currentTile.intro_text())
    for enemy in currentTile.enemiez:
        enemy.nextActionTime = currentTime + random.random()*enemy.actionSpeed + enemy.actionDelay
    return

## This loop is repeatedly called with tkinter libraries to allow game logic to occur ##
def gameloop():
    global isLinkDead
    global isGameWon
    #update time
    global currentTime
    global isIntroFinished
    currentTime = time.time()-startTime
    #check if enemies dead
    for enemy in currentTile.enemiez:
        if enemy.hp <= 0:
            msgLog(f"{enemy.name} {enemy.num} is dead.")
            currentTile.enemiez.remove(enemy)
            drop = enemy.drops[random.randint(0, len(enemy.drops)-1)]
            if drop and random.random()<0.5:
                currentTile.items.append(drop)
                msgLog(f"{enemy.name} {enemy.num} dropped \"{drop}\".")
                currentTile.items.sort()
    #let enemies do actions
    if not isLinkDead:
        for enemy in currentTile.enemiez:
            if currentTime > enemy.nextActionTime:
                strToLog = enemy.action(link)
                if strToLog:
                    msgLog(strToLog)
    
    if currentTile.pos.x == 2 and currentTile.pos.y == 3 and currentTile.pos.z == 1 and not isGameWon:
        isGameWon = True
        winGame()
    
    #check for player death
    if link.hp <=0 and not isLinkDead:
        msgLog(f"{link.name} is dead.")
        isLinkDead = True
        endGame()
    
    if link.stopDodgingTime < currentTime:
        link.isDodging = False
    
    #change the music
    if (currentTime > 6.798) and not isIntroFinished:
        isIntroFinished = True
        if not isLinkDead:
            PlaySound('audio/OverworldLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
        else:
            PlaySound('audio/GameOverLoop.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
    #call this function in 25 ms (so it loops)
    root.after(25, gameloop)




############ MAIN METHOD #############
if __name__ == "__main__":
    
    #play title screen music
    PlaySound('audio/Intro.wav', SND_FILENAME|SND_ASYNC|SND_LOOP)
    #print title ascii text
    os.system('color')
    print(f'''
{Fore.GREEN} .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
{Fore.GREEN}/ .. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\.. \\
{Fore.GREEN}\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/\\ \\/ /
{Fore.GREEN} \\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /\\/ /
{Fore.GREEN} / /\\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /\\/ /\\
{Fore.GREEN}/ /\\ \\/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\\ \\/\\ \\
{Fore.GREEN}\\ \\/\\ \\                                                                            /\\ \\/ /
{Fore.GREEN} \\/ /\\ \\{Fore.WHITE}                      ___________________________                       {Fore.GREEN}  / /\\/ /
{Fore.GREEN} / /\\/ /{Fore.WHITE}              THE LEGEND OF ——————————————————  /                        {Fore.GREEN} \\ \\/ /\\
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
    link = Player(playerName, 3, 3)
    #Log starting message
    print(
        f'''
        The Legend of Zelda\n
        Many years ago prince darkenss "Gannon" stole one of the 
        Triforce with Power. Princess Zelda had one of the Triforce 
        with Wisdom. She divided it into "8" units to hide it from 
        "Gannon" before she was captured.\n
        Go find the "8" units "{link.name}" to save her.\n
        '''
    )
    input("< Press enter to continue >")
    #import map
    global map
    map = tiles.getOverworldTiles(link)
    global currentTile
    currentTile = map[3][0][1]
    #set starting inventory
    link.inventory.append("wooden shield")
    #stop title screen music
    PlaySound(None, SND_FILENAME)
    #start main game music
    PlaySound('audio/Overworld.wav', SND_FILENAME|SND_ASYNC)
    global isIntroFinished
    isIntroFinished = False
    #specify window details
    root = tk.Tk()
    root.resizable(False, False)
    canvas1 = tk.Canvas(root)
    #set dimensions
    root.geometry("1000x800")
    #change window title and icon
    root.title("The Legend of Zelda")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
    #add input field
    inputBox = tk.Entry(root)
    inputBox.pack()
    inputBox.place(bordermode=tk.OUTSIDE, height=30, width=1000, y = 770)
    inputBox.bind("<Return>", key)
    inputBox.bind("<Escape>", escape)
    inputBox.focus_set()
    #add output box with scroll bar
    msgBox = ScrolledText.ScrolledText(root)
    msgBox.pack()
    msgBox.place(bordermode=tk.OUTSIDE, height=770, width=1000, y = 0)
    msgBox.config(state=tk.DISABLED)
    #bring window to front
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.focus_force()
    root.after(1, lambda: root.focus_force())
    #initialize global variables
    startTime = time.time()
    currentTime = 0
    global isLinkDead
    isLinkDead = False
    global isGameWon
    isGameWon = False
    #log message for starting room
    msgLog(currentTile.intro_text())
    #start gameloop
    root.after(2, gameloop)
    #open window
    tk.mainloop()
    ## END MAIN ##