"""
###Notes###
This is the main file for the Eng Phys Text Adventure (EPTA). This game utilizes some poorly done OOP (sorry Mitch), it has it's strengths though!
The comments, organization, and optimization are bad but generally:
this file = the setup, main loop, and ending. Run this to run the game.
GameFunctions.py = The main mechanics of the game and the quests. All non-class functions. 
GameClasses.py = Class definitions and their coresponding functions.
Startup.py = All the map locations, items, npcs (called enemies), and interactables. Also creates the dictionaries of them.
Setup.py = Py2exe file used to compile into an exe. Run using "python setup.py py2exe" in command prompt.

In general try to keep this structure and put any other long ascii or modules into another file.
"""
from GameFunctions import * #this imports the code and all the code dependancies (functions imported in that)
import StartUp
import Opening    #don't import * from these b.c. these pull global variables from game functions and doing a recursive import creates errors
import CreativeMode #don't import * from these b.c. these pull global variables from game functions and doing a recursive import creates errors
import Quests


#If there was a title screen it would go here
GAMEINFO['version'] = "0.28.2"
GAMEINFO['versionname'] = "Alpha v0.28 - Major overhall"
#Updated: Mar 25, 2019

LINEBREAK = "========================================================================" #standard display width breaker, 72 characters

#begining section of the game (not in the main loop), seperated for nested game
def Setup():
    global PLAYER
    global GAMEINFO
    Opening.StartScreen() #Startscreen loop where you can play new game, loadgame, choose settings, or exit
    

    if not(GAMESETTINGS['DisableOpening'] or GAMESETTINGS['SpeedRun']): Opening.Opening() #plays the opening if disable opening is set to False
    
    print LINEBREAK

    GAMEINFO['playername'] = raw_input("First, what is your name?\n")
    
    PLAYER.name = GAMEINFO['playername']
    NameChange() #changes the name of all name related things in the game
       
    x = 2
    y = 3
    z = 1
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z

    CurrentPlace = MAPS[x][y][z]
    
    print CurrentPlace.lore +"\n\n" + CurrentPlace.info + CurrentPlace.search()
    
    GAMEINFO['gamestart'] = time.time() #Gives the local start date of the game in seconds since epoch of 1970
    CreativeMode.saveGame("basegame") #Use this to get a base state newgame, keep it in each time so don't have to worry about updating
    #This tyler Kashak has to be after the basegame save or else it will always revert the base game to you spawning as Tyler
    if PLAYER.name == "Tyler Kashak": #He realizes he's the main character and can do anything he wants
        AsciiArt.One()
        print "\nHe is beginning to believe\n\nYOU are the One\n"
        PLAYER.__dict__ = Tyler.__dict__ #sets him to the initial Tyler character for strating inventory
        PLAYER.maxhealth = 999
        PLAYER.basestats = [420,420,420]
        PLAYER.updateStats()
    CurrentPlace.travelled = 0 #so that it says it's been travelled, I moved it down so that it wouldn't effect the basegame save
   
    GAMEINFO['timestart'] = GAMEINFO['gamestart']   #runtime counter of the start of each main loop session. Needs to be global. Is equal to gamestart at the session start but will change as the user saves, loads, restarts, or does a nested game
    print "Your time starts now!"
    
                                                                        #this time.ctime(seconds) converts to a nice readable time to be output to the log
    GAMEINFO['log'] = [GAMEINFO['versionname'],  GAMEINFO['playername'], time.ctime(GAMEINFO['gamestart']), "--LOG START--"] #log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
    

def Main():
    #These are all the global dictionaries/objects in the game
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    #global SETTINGS #TODO will import the settings later
    #global keyword brings in a global variable into a function and allows it to be altered
    KEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys()) #keys used for the spellchecking function
    VERBS =['search','stats','inventory','equip','drop','attack','talk','inspect','eat','savegame','loadgame','restart','up','down','left','right','back','forward','kill','get','wear','look','drink','inhale','ingest','devour'] #acceptable game commands called 'verbs'. Need to add verb to this list for it to work in the elifs
    

  
    #Main game loop section that runs while the player is alive (player is killed in story once done)
    while(PLAYER.alive):
        if not(GAMESETTINGS['DisableMusic']): Music()#TODO make music in a non-jank way! Will only do on next command
         
        line = raw_input('What do you want to do?\n') 
        GAMEINFO['log'].append(line)
        direction = line.lower().split(" ",1)

        
        for i in range(len(direction)):
           direction[i] = direction[i].strip() #Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)


            if verb in ['u','d','l','r','f','b','up','down','left','right','back','forward']:
                CurrentPlace = Move(verb)
                GAMEINFO['stepcount'] += 1 #increments the stepcount after taking a step (whether sucessful or not)
            elif verb in ['search','look']:
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
                GAMEINFO['runtime'] += (time.time() - GAMEINFO['timestart']) #adds the runtime (initilized to zero) to the session runtime to make the total runtime
                GAMEINFO['timestart'] = time.time() #resets timestart so it's not doubly added at the end
                logGame(GAMEINFO['log']) #logs the game when you save it
                CreativeMode.saveGame(GAMEINFO['playername']) #saves all data
                print "Your game has been saved!: SaveFile " + GAMEINFO['playername']
            elif verb == 'loadgame': #this function loads the game off of the save file. Was having problems with loading
                CreativeMode.loadGame(GAMEINFO['playername']) #loads in the savefile global variables
                GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            elif verb == 'restart': #this restarts the game to the base game
                CreativeMode.loadGame("basegame") #loads in the savefile global variables
                GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            else:
               print "\nI don't understand that command!\n"

        elif (len(direction) == 2):
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)
            objectName = SpellCheck(direction[1],KEYS)

            if verb in ['equip','get','wear']:
                Equip(objectName)
                
            elif verb == 'drop':
                Drop(objectName)

            elif verb in ['attack','kill']:
                Attack(objectName)
                
            elif verb == 'talk':
                Talk(objectName)

            elif verb == 'inspect':
                Inspect(objectName)

            elif verb in ['eat','drink','inhale','ingest','devour']:
                Eat(objectName)
            else:
               print "\nI don't understand that command!\n"
    
        GAMEINFO['commandcount'] += 1 #increments the command count after every command but doesn't print
        print LINEBREAK
        Quests.Story() #runs through the story quests checks
        #TODO integrate this into game functions with a function, possibly seperate quests from game functions and import all from there to keep things global
        if PLAYER.alive == False and GAMEINFO['layersdeep'] > 0: #gets you out of the EPTA all the way down quest and back into the sublayer
            End()
            print "\n========================================================================\n\nYou finish the game and put back the laptop ready to get back to reality.\nHow long did you spend on this game?"
            log = GAMEINFO['log'] #sets up a temporary variable to pass the log back up a layer
            CreativeMode.loadGame(str(GAMEINFO['layersdeep']-1))
            GAMEINFO['log'] = log + ["--Back in layer: " + str(GAMEINFO['layersdeep']) +"---"] #overwrites it to keep a running tab and says what layer we're in 
            #Doesn't reset the GAMEINFO['timestart'] as the runtime will included the time in the nested function
            #TODO delete the save file you're coming out of
            
    End() #calls the end function in main so that the game can continue its loop structure

def End():
    global GAMEINFO
    global PLAYER
    GAMEINFO['runtime'] = GAMEINFO['runtime'] + (time.time()-GAMEINFO['timestart']) #calculates total time you've been playing by adding your loaded runtime to your instance runtime (end time - start time)
    GAMEINFO['log'] = GAMEINFO['log'] + ["--END OF LOG--", "Stepcount: "+str(GAMEINFO['stepcount']), "Command Count: " + str(GAMEINFO['commandcount']),
      "Run Time: " + str(GAMEINFO['runtime']), "--Character STATS--",str((PLAYER.location[0],PLAYER.location[1],PLAYER.location[2])),
      str((PLAYER.stats[0],PLAYER.stats[1],PLAYER.stats[2])),str(PLAYER.health),"HEAD: " + str(PLAYER.inv["head"].name),
      "BODY: " + str(PLAYER.inv["body"].name), "HAND: " + str(PLAYER.inv["hand"].name), "OFF-HAND: " + str(PLAYER.inv["off-hand"].name)
        ] #adds the final info to the log leger
    #TODO, condense this story display code
    playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","NoWorries.mp3"), False)
    if Quests.Story()== 0: #player dies 
        print LINEBREAK
        DisplayTime(GAMEINFO['runtime']) #displays the runtime for speed running
        print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
        logGame(GAMEINFO['log']) #writes the log file
        if raw_input("Thanks for playing!! Better luck next time!\nType 'R' to restart the game, anything else to exit: ").lower() =='r': #lets the player restart the game
            CreativeMode.loadGame("basegame") #loads in the savefile global variables
            GAMEINFO['timestart'] = time.time() #reset instance start time
            Main() #re-enters the main loop
        return #returns the game so you don't get the final dialog
    elif raw_input("Type 'C' to continue\n").lower() == 'c':
        Opening.Closing() #plays the closing
        GAMEINFO['log'].append("---THEY WON---") #appends they won at the end of the log file to make it easier find
        if Quests.Story() == 1: #The bad storyline ending
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
        elif Quests.Story() == 2: #The good storyline ending. 
            print "Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
        DisplayTime(GAMEINFO['runtime']) #displays the runtime then all other status
        print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
        logGame(GAMEINFO['log']) #logs the data to be submitted
        CreativeMode.saveGame(GAMEINFO['playername'] + " Winner") #saves all data to later be submited, different from the main save file
        endchoice = raw_input("Thanks for playing!!\nType 'C' to continue, 'R' to restart, anything else will exit: ").lower() #this input is to hold the screen until the player decides what to do
        if endchoice == "c":
            PLAYER.alive = True
            print LINEBREAK
            QUESTS['restored order'] = 0 #turn this off so you can continue playing the game without the quest redoing
            QUESTS['create chaos'] = 0 
            Main() #returns to the main (hopefully in the same state)
        if endchoice == "r":
            CreativeMode.loadGame("basegame") #loads in the savefile global variables
            GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            Main() #re-enters the main loop
    return

#TODO enable bug catcher before 
try: #runs the main functions (the whole game bassically)
    Setup()
    Main()
    #end function is run at the end of main loop so you can restart the game
except:
    AsciiArt.Error()
    CreativeMode.saveGame(GAMEINFO['playername']) #saves all data
    print "Your game has been saved!: SaveFile " + GAMEINFO['playername']
    print "\nSorry your game encountered some kind of bug, we're sorry.\nWe've saved your game but please contact your nearest developer to report the problem if it continues.\nThanks :D" 
    raw_input("Type anything to exit: ")