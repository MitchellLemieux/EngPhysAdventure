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
version = 0.27
versionname = "Alpha v0.27 - Dev Update"
#Updated: Dec 15, 2018

#TODO uncomment that guy
#Opening()

playername = raw_input("First, what is your name?\n")

print "========================================================================" #standard display width breaker, 72 characters

def Main():
    #TODO always have to have global variables defined in function for scoping? I forget and need to look this up
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    #global playername #the players name, TODO tak
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    KEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys()) #keys used for the spellchecking function
    VERBS =['search','stats','inventory','equip','drop','attack','talk','inspect','eat','savegame','loadgame'] #acceptable game commands called 'verbs'. Need to add verb to this list for it to work in the elifs
    
    PLAYER.name = playername
    if playername == "Tyler Kashak":
        print "\nYou are now playing as: THE MAN\n"
        PLAYER.health = 999
       
    x = 2
    y = 3
    z = 1
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z

    CurrentPlace = MAPS[x][y][z]
    print CurrentPlace.lore +"\n\n" + CurrentPlace.info + CurrentPlace.search()
    CurrentPlace.travelled = 0
    
    stepcount, commandcount, runtime = 0   #these are speedrunning counters
    timestart = time.time() #makes the time start variable (in seconds from 1970)
    print "Your time starts now!"
  
    log = [versionname + '\n',  playername + '\n', str(time.time()) + '\n')] #initialize the log function with certain variables
        
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
                stepcount += 1 #increments the stepcount and then displays after you take a step
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
                #TODO work on correcting the runtime adding and all this other extrainfo
                #runtime = runtime + (time.time() - timestart)
                #TODO add: computer name, words and characters per minute, enemies killed, items eaten, items equiped, enemies talked, quantum relecs found
                extrainfo = [version, versionname, timestart, stepcount, commandcount]
                CreativeMode.saveGame(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS,extrainfo)
            elif verb == 'loadgame':
                #this function loads the game off of the save file
                save = CreativeMode.loadGame()
                loadplayer = save[0]
                loaditems = save[1]
                loadmap = save[2]
                loadenemy = save[3]
                loadinter = save[4]
                loadquest = save[5]
                loadextra = save[6]

                
                PLAYER.__dict__ = loadplayer.__dict__ #YOU HAVE TO USE THIS DARN .__dict___ thing to copy the object atributes https://stackoverflow.com/questions/36243488/how-can-i-overwrite-an-object-in-python
                for item in ITEMS:
                    ITEMS[item] = loaditems[item] #assignment better when no subitems? .__dict for when there is
                for enemy in ENEMIES:  #.__dict__ removed on these and it works?
                    ENEMIES[enemy] = loadenemy[enemy]
                for inter in INTERACT:
                    INTERACT[inter] = loadinter[inter]
                for quest in QUESTS:
                    QUESTS[quest] = loadquest[quest]
                #for some reason putting maps below these other ones fixed a killing bug?
                for x in range(7): #TODO make this not hard coded
                    for y in range(9):
                        for z in range(4):
                            if MAPS[x][y][z]: #There are different objects in 1 vs the other so need to replace object in each list with the new one of reference
                                MAPS[x][y][z].__dict__ = loadmap[x][y][z].__dict__
                
                #this whole load function may have problems with adding items and going between version of savefiles (may need an updater)
                #so one when you do this "load" it saves all the object variables to new/different locations
                #as a quick fix get around this we can reference the name of the things in all functions instead of the object
                #however figuring out how to "overwrite"/reindex the loaded objects so we don't just keep leaking memory
                #even with 'overwriting' all the attributes it still 'remembers' the old object list
                #game me troubles with removing items... everything else works but needs a full play test for bugs and someone who knows what they're doing
                #'old' objects and 'new' objects are different by instance location
                #with this load function it's best to reference things by name until I can figure out the object overwriting. Ineffecient but works
                #acording to this lists make new functions: http://interactivepython.org/runestone/static/CS152f17/Lists/ObjectsandReferences.html
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

        commandcount += 1 #increments the command count after every command but doesn't print
        print "========================================================================"
        Story() #runs through the story quests checks

        
    timeend = time.time()
    runtime = timeend-timestart
    #dumb save file stuff
    log.append("Player Stats")
    log.append(stepcount)
    log.append(commandcount)
    log.append(runtime)
 
    if Story()== 0: #once the player dies
        print "========================================================================"
        DisplayTime(runtime) #displays the runtime for speed running
        print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
        logGame(log)
        raw_input("Thanks for playing!! Better luck next time!")
        
    elif Story() == 1: #The bad storyline ending
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing() #plays the closing
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
            DisplayTime(runtime) #displays the runtime
            print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
            logGame(log)
            raw_input("Thanks for playing!!") #this input is to hold the screen until the player leaves
    elif Story() == 2: #The good storyline ending. Exact same in structure as Story()==1
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing()
            print "Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
            DisplayTime(runtime)
            print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
            logGame(log)
            raw_input("Thanks for playing!!")
Main() #runs the main function (the whole game bassically) 
