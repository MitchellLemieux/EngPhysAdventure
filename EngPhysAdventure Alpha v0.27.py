#Notes
#This is the main file for the Eng Phys Text Adventure (EPTA). This game utilizes some poorly done OOP (sorry Mitch), it has it's strengths though!
#The comments, organization, and optimization are bad but generally:
#this file = the setup, main loop, and ending. Run this to run the game.
#GameFunctions.py = The main mechanics of the game and the quests. All non-class functions. 
#GameClasses.py = Class definitions and their coresponding functions.
#Startup.py = All the map locations, items, npcs (called enemies), and interactables. Also creates the dictionaries of them.
#Setup.py = Py2exe file used to compile into an exe. Run using "python setup.py py2exe" in command prompt.

#In general try to keep this structure and put any other long ascii display or mode into another file.

from GameFunctions import *
import StartUp
from Opening import * #this imports the code and all the code dependancies (functions imported in that)
import CreativeMode

#If there was a title screen it would go here
GAMEINFO['version'] = 0.27
GAMEINFO['versionname'] = "Alpha v0.27 - Dev Update"
#Updated: Dec 15, 2018

#TODO uncomment that guy
#Opening()

GAMEINFO['playername'] = raw_input("First, what is your name?\n")
print GAMEINFO['playername']


print "========================================================================" #standard display width breaker, 72 characters

def Main():
    #TODO always have to have global variables defined in function for scoping? I forget and need to look this up
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    #global keyword brings in a global variable into a function and allows it to be altered
    KEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys()) #keys used for the spellchecking function
    VERBS =['search','stats','inventory','equip','drop','attack','talk','inspect','eat','savegame','loadgame'] #acceptable game commands called 'verbs'. Need to add verb to this list for it to work in the elifs
    
    PLAYER.name = GAMEINFO['playername']
    if PLAYER.name == "Tyler Kashak": #He realizes he's the main character and can do anything he wants
        AsciiArt.One()
        print "\nHe is beginning to believe\n\nYOU are the One\n"
        PLAYER.__dict__ = Tyler.__dict__ #sets him to the initial Tyler character for strating inventory
        PLAYER.maxhealth = 999
        PLAYER.basestats = [420,420,420]
        PLAYER.updateStats()
       
    x = 2
    y = 3
    z = 1
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z

    CurrentPlace = MAPS[x][y][z]
    print CurrentPlace.lore +"\n\n" + CurrentPlace.info + CurrentPlace.search()
    CurrentPlace.travelled = 0
    
    timestart = time.time()   #local speedrun time counter. time.time() makes the time start variable (in seconds from 1970)
    print "Your time starts now!"
  
    log = [GAMEINFO['versionname'],  GAMEINFO['playername'], timestart, "--LOG START--"] #log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
    
    while(PLAYER.alive): #main game loop that runs while the player is alive (player is killed in story once done)
 
        line = raw_input('What do you want to do?\n') 
        log.append(line)
        direction = line.lower().split(" ",1)

        
        for i in range(len(direction)):
           direction[i] = direction[i].strip() #Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)


            if verb in ['u','d','l','r','f','b']:
                CurrentPlace = Move(verb)
                GAMEINFO['stepcount'] += 1 #increments the stepcount after taking a step (whether sucessful or not)
            elif (verb == 'search'):
                x = PLAYER.location[0]
                y = PLAYER.location[1]
                z = PLAYER.location[2]
                print MAPS[x][y][z].search()

            elif (verb == 'stats'):
                Stats()
            elif (verb == 'inventory'):
                Inventory()
            elif verb == 'savegame':
                #TODO add: computer name, words and characters per minute, # enemies killed, # items eaten, # items equiped, # enemies talked, # quantum relecs found
                if GAMEINFO['runtime'] == 0: #if game hasn't run set the start time and the runtime
                    GAMEINFO['gamestart'] = timestart
                    GAMEINFO['runtime'] = (time.time() - timestart)
                else: #If this is a loaded game it adds the spent time to the runtime
                    GAMEINFO['runtime'] += (time.time() - timestart)
                savename = raw_input('What do you want to name the save file?: ')
                logGame(log,0) #logs the game when you save it
                GAMEINFO['log'] = log #only writes log to game info when being saved
                CreativeMode.saveGame(savename, PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS,GAMEINFO) #saves all data
            elif verb == 'loadgame': #this function loads the game off of the save file. Was having problems with loading
                #TODO if I can move this loadgame to creativemode that would be good
                #TODO Make it still able to load with updates
                #TODO make it name the file automatically with player name or you put it in
                loadname = raw_input('What is the name of the save file?: ')
                save = CreativeMode.loadGame(loadname)
                #seperates the list
                loadplayer = save[0]
                loaditems = save[1]
                loadmap = save[2]
                loadenemy = save[3]
                loadinter = save[4]
                loadquest = save[5]
                loadinfo = save[6]
                
                
                for info in GAMEINFO: #when itterating through list the itterating variable is the string of the key
                    GAMEINFO[info] = loadinfo[info]                   
                PLAYER.__dict__ = loadplayer.__dict__
                for item in ITEMS:
                    ITEMS[item] = loaditems[item] #assignment better when no subitems? .__dict for when there is
                for enemy in ENEMIES:  #.__dict__ removed on these and it works?
                    ENEMIES[enemy] = loadenemy[enemy]
                for inter in INTERACT:
                    INTERACT[inter] = loadinter[inter]
                for quest in QUESTS:
                    QUESTS[quest] = loadquest[quest]
                #for some reason putting maps below these other ones fixed a bunch of bugs
                for x in range(7): #TODO make this not hard coded by range
                    for y in range(9):
                        for z in range(4):
                            if MAPS[x][y][z]: #There are different objects in 1 vs the other so need to replace object in each list with the new one of reference
                                MAPS[x][y][z].__dict__ = loadmap[x][y][z].__dict__

                GAMEINFO['commandcount'] += 1 #+1 command to load the game because it doesn't count the loadgame command
                log = loadinfo['log'] #loads in the load log to the local log
                log.append("loadgame") #adds the load game command to the log
                timestart = time.time() #reset local variable starttime to current time

                #Displayes the current place info again to show it's been loaded
                CurrentPlace = MAPS[PLAYER.location[0]][PLAYER.location[1]][PLAYER.location[2]]
                print "========================================================================"
                print CurrentPlace.info + CurrentPlace.search()

                #YOU HAVE TO USE THIS DARN .__dict___ thing to copy the object atributes https://stackoverflow.com/questions/36243488/how-can-i-overwrite-an-object-in-python
                #This is ineffecient but works. I think main problem I had is loading where the loaded objects are a new memory location but the game still references old locations
                #It's best to reference things by name  
                #Acording to this lists make new functions: http://interactivepython.org/runestone/static/CS152f17/Lists/ObjectsandReferences.html
                #use (a is b) to see if a and b refer to the same memory location
                
            else:
               print "\nI don't understand that command!\n"

        elif (len(direction) == 2):
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)
            objectName = SpellCheck(direction[1],KEYS)

            if verb == 'equip':
                Equip(objectName)
                
            elif verb == 'drop':
                Drop(objectName)

            elif verb == 'attack':
                Attack(objectName)
                
            elif verb == 'talk':
                Talk(objectName)

            elif verb == 'inspect':
                Inspect(objectName)

            elif verb == 'eat':
                Eat(objectName)
            else:
               print "\nI don't understand that command!\n"

        GAMEINFO['commandcount'] += 1 #increments the command count after every command but doesn't print
        print "========================================================================"
        Story() #runs through the story quests checks

        
    GAMEINFO['runtime'] = GAMEINFO['runtime'] + (time.time()-timestart) #calculates total time you've been playing by adding your loaded runtime to your instance runtime (end time - start time)
    log = log + ["--END OF LOG--", "Stepcount: "+str(GAMEINFO['stepcount']), "Command Count: " + str(GAMEINFO['commandcount']),
                 "Run Time: " + str(GAMEINFO['runtime']), "--Character STATS--"]
    GAMEINFO['log'] = log #saving the log to the global variable for the save file

    if Story()== 0: #once the player dies
        print "========================================================================"
        DisplayTime(GAMEINFO['runtime']) #displays the runtime for speed running
        print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
        logGame(log,1) #writes the log file, 1 indicates to write the player stats because the game ended
        raw_input("Thanks for playing!! Better luck next time!")
        
    elif Story() == 1: #The bad storyline ending
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing() #plays the closing
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
            DisplayTime(GAMEINFO['runtime']) #displays the runtime then all other status
            print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
            logGame(log,1)
            raw_input("Thanks for playing!!") #this input is to hold the screen until the player leaves
    elif Story() == 2: #The good storyline ending. Exact same in structure as Story()==1
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing()
            print "Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
            DisplayTime(GAMEINFO['runtime'])
            print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
            logGame(log,1)
            raw_input("Thanks for playing!!")
Main() #runs the main function (the whole game bassically) 
