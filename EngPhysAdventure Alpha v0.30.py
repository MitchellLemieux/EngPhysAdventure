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
import Quests  # Used to separate quest/event functions
import TextParser  # Used to separate text interpretation and commands
from Colour import *

import MapDisplay  # Used to separate minim-ap display


# TODO Make sure these versions and release date are correct
#If there was a title screen it would go here
GAMEINFO['version'] = "0.30.00"
GAMEINFO['versionname'] = lightblue + "Alpha " + red +"v" + white +"0.30.00 - " + blue + 'T' + cyan + 'H' + black + 'E ' \
                            + green + 'F' + lightgreen + 'I' + lightblue + 'N' + lightcyan + 'A' + lightgreen + 'L ' \
                            + lightmagenta + 'E' + lightred + 'P' + lightwhite + 'T' + lightyellow + 'A ' + magenta \
                            + 'U' + red + 'P' + white + 'D' + yellow + 'A' + blue + 'T' + red + 'E' + textcolour
GAMEINFO['releasedate'] = "Nov 12, 2019"





magenta = Fore.MAGENTA
red = Fore.RED
reset = Fore.RESET
white = Fore.WHITE
yellow = Fore.YELLOW

LINEBREAK = "========================================================================" #standard display width breaker, 72 characters

# Begining section of the game (not in the main loop), Seperated for nested game
def Setup():
    global PLAYER
    global GAMEINFO
    global MAPS

    if GAMESETTINGS['loadgame']:  # If player loaded the game it returns out of the setup and goes to main
        GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
        GAMESETTINGS['loadgame'] = 0  # sets the parameter to 0 just so it doesn't accidentally save
        return

    if not(GAMESETTINGS['DisableOpening'] or GAMESETTINGS['SpeedRun'] or GAMEINFO['devmode']): Opening.Opening() #plays the opening if disable opening is set to False
    
    print LINEBREAK

    if GAMEINFO['devmode']: GAMEINFO['playername'] = "Doug Fallon"  # Skip name step and names your person Doug
    else:
        # - Name Selection -
        while not GAMEINFO['playername']:  # name selection can't be empty
            GAMEINFO['playername'] = raw_input("First, what is your name?\n")
            if GAMEINFO['playername'] in [""," ", "  ", "   ", ".",",", "no"]:  # not accepted names
                printT("Please enter a valid name! ")
                GAMEINFO['playername'] = ""
    
    PLAYER.name = GAMEINFO['playername']
    NameChange()  # changes the name of all name related things in the game


    x,y,z,dim = STARTLOCATION
    if GAMEINFO['devmode']: x,y,z,dim = BRENSTARTLOCATION
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z
    PLAYER.location[3] = dim

    CurrentPlace = MAPS[x][y][z][dim]

    # This prints

    printT("You wake up in " + mapcolour + CurrentPlace.name + textcolour + "(\S)")
    printT(CurrentPlace.lore)
    printT("(\S)" + mapcolour + "~" + CurrentPlace.name.upper() + "~" + textcolour + "(\S)" +   CurrentPlace.search(MAPS))


    
    GAMEINFO['gamestart'] = time.time()  # Gives the local start date of the game in seconds since epoch of 1970
    CreativeMode.saveGame("basegame")  # Use this to get a base state newgame, keep it in each time so don't have to worry about updating
    # This tyler Kashak has to be after the basegame save or else it will always revert the base game to you spawning as Tyler
    # Enables this ULTRA character is name is Tyler Kashak or in DevMode
    if PLAYER.name == "Tyler Kashak" or GAMEINFO['devmode']: #He realizes he's the main character and can do anything he wants
        # AsciiArt.One()  # TODO Enable once Dynamic Ascii Art
        print "\nHe is beginning to believe\n\nYOU are the One\n"
        # TODO Change back to Tyler
        PLAYER.__dict__ = BREN007PIE.__dict__  # sets him to the initial Tyler character for strating inventory
        PLAYER.maxhealth = 999
        PLAYER.basestats = [420,420,420]
        PLAYER.updateStats()
    CurrentPlace.travelled = 0  # so that it says it's been travelled, I moved it down so that it wouldn't effect the basegame save
   
    GAMEINFO['timestart'] = GAMEINFO['gamestart']   #runtime counter of the start of each main loop session. Needs to be global. Is equal to gamestart at the session start but will change as the user saves, loads, restarts, or does a nested game
    if GAMESETTINGS['SpeedRun']: print "Your time starts now!"
    
                                                                        #this time.ctime(seconds) converts to a nice readable time to be output to the log
    GAMEINFO['log'] = [GAMEINFO['versionname'],  GAMEINFO['playername'], time.ctime(GAMEINFO['gamestart']), "--LOG START--"] #log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
    

def Main():
    # These are all the global dictionaries/objects in the game
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    #global SETTINGS #TODO will import the settings later
    #global keyword brings in a global variable into a function and allows it to be altered



    # Main game loop section that runs while the player is alive (player is killed in story once done)
    # TODO don't have main loop based on player alive but on game being played, e.g. gameExit boolean variable instead
    while(PLAYER.alive):

        # if not(GAMESETTINGS['HardcoreMode']): MapDisplay.mini()  # Minimap display area in game


        if GAMEINFO['scriptdata']: # if there's a script loaded carry out those commands! instead of normal
            command = GAMEINFO['scriptdata'].pop(0)  # pops the first element to go through script until finished
            printT(command)
        else:
            command = raw_input('\nWhat do you want to do?\n')

        print LINEBREAK  # This linebreak helps split up each turn

        # Sends the command text to the text parser to be interpreted and action to be done
        TextParser.Parser(command,PLAYER,ITEMS,MAPS,INTERACT,QUESTS,ENEMIES,GAMEINFO,GAMESETTINGS)

        GAMEINFO['commandcount'] += 1  # increments the command count after every command but doesn't print
        #print LINEBREAK  # Got rid of this bottom linebreak to hopefully have the current situation more clear
        Quests.ebta_story()  # runs through the story quests checks and actions
        Quests.sidequests()  # runs through all the sidequest checks and actions
        Quests.events()  # runs through all the events checks and actions

        #TODO integrate this into game functions with a function, possibly seperate quests from game functions and import all from there to keep things global
        if PLAYER.alive == False and GAMEINFO['layersdeep'] > 0:  # gets you out of the EPTA all the way down quest and back into the sublayer
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
      "Run Time: " + str(GAMEINFO['runtime']), "--Character STATS--",str((PLAYER.location[0],PLAYER.location[1],PLAYER.location[2], PLAYER.location[3])),
      str((PLAYER.stats[0],PLAYER.stats[1],PLAYER.stats[2])),str(PLAYER.health),"HEAD: " + str(PLAYER.inv["head"].name),
      "BODY: " + str(PLAYER.inv["body"].name), "HAND: " + str(PLAYER.inv["hand"].name), "OFF-HAND: " + str(PLAYER.inv["off-hand"].name)
        ] #adds the final info to the log leger
    #TODO, condense this story display code
    if Quests.ebta_story()== 0:  # player dies and that's how they're out of the loop
        print LINEBREAK
        if GAMESETTINGS['SpeedRun']: DisplayTime(GAMEINFO['runtime'])  # displays the runtime for speed running
        if GAMESETTINGS['SpeedRun']: print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
        logGame(GAMEINFO['log']) # writes the log file
        if raw_input("Thanks for playing!! Better luck next time!\nType 'R' to restart the game, anything else to exit:\n").lower() =='r': #lets the player restart the game
            CreativeMode.loadGame("basegame") #loads in the savefile global variables
            GAMEINFO['timestart'] = time.time() #reset instance start time
            Main() #re-enters the main loop
        return # returns the game so you don't get the final dialog
    elif raw_input("You've won! Type 'C' to continue\n").lower() == 'c':  # If they beat either of the storylines
        GAMEINFO['log'].append("---THEY WON---") #appends they won at the end of the log file to make it easier find
        if Quests.ebta_story() == 1: #The bad storyline ending
            printT("After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END")
        elif Quests.ebta_story() == 2: #The good storyline ending.
            printT("Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END.")
        elif Quests.ebta_story() == 3: #The good storyline ending.
            printT("After defeating both Dr. Cassidy and Sir William McMaster you take a moment to think while the deed to McMaster University lies at your feet fluttering slowly in a gentle breeze. You think about what you were told. Does that piece of paper really give you immense power and control over the school? After a quick smirk and a laugh you pick up the deed begin to rip it up. The parchment resists for a moment before giving way in a spectacular display of sparks and disappearing into the wind. You go on knowing that the fate of the University now resides in the hands of no one... it resides in the hands everyone.")
        if GAMESETTINGS['SpeedRun']: DisplayTime(GAMEINFO['runtime']) #displays the runtime then all other status
        if GAMESETTINGS['SpeedRun']:print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
        logGame(GAMEINFO['log']) #logs the data to be submitted
        CreativeMode.saveGame(GAMEINFO['playername'] + " Winner") #saves all data to later be submited, different from the main save file
        Opening.Closing()  # plays the closing
        endchoice = raw_input("Thanks for playing!!\nType 'C' to continue, 'R' to restart, anything else will exit: ").lower() #this input is to hold the screen until the player decides what to do
        if endchoice == "c":
            PLAYER.alive = True
            print LINEBREAK
            QUESTS['restored order'] = 0  # turn this off so you can continue playing the game without the quest redoing
            QUESTS['create chaos'] = 0 
            Main()  # returns to the main (hopefully in the same state)
        if endchoice == "r":
            CreativeMode.loadGame("basegame") #loads in the savefile global variables
            GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            Main() #re-enters the main loop
    return


# ---------GAME STARTS HERE  ---------

# TODO Reset settings before release before release

# Reading in game settings, has to be at start of game befor anything so it reads in settings
try:  # In case settings file isn't there
    settingpath = os.path.join(GAMEINFO['datapath'], "settings.ini")
    with open(settingpath, 'r') as f:
        data = f.readlines()  # reads in data seperated by newline into a list
    f.close()
    data = [f.strip() for f in data]  # removes the \n in each list element wise (very useful for list operations)
    for i in range(0, len(data), 2):
        GAMESETTINGS[data[i]] = int(data[i+1])  # Reading in file data in attribute value order, value should be an int
except:
    #print "\n\nSomething is Wrong with the Setting.ini file!\n\n"
    print "\n\nNo Settings Detected\n\n"

# Reading in DEVMODE.ini file if devmode is set
try:  # IF DEVMODE.ini isn't there in the CWD of the game no beuno
    with open("DEVMODE.ini", 'r') as f:
        data = f.readlines()  # reads in data seperated by newline into a list
    f.close()
    if data[0] == "LOL NO U":  # contents of the dev file needs to be
        # quickly asks you want to not be in dev mode in obfuscated way
        if not raw_input("What would you like? Type in n: ") == "n":
            GAMEINFO['devmode'] = 1
            print CLEARSCREEN  # clears the screen

except:  # does nothing if no dev file there
    pass
    #raw_input("HI I'M NOT A DEV!")



# Start Screen is after reading in settings so it can skip start screen if enabled
Opening.StartScreen()  # Startscreen loop where you can play new game, loadgame, choose settings, or exit

# The Actual Start of the game when you hit Play, depending on if in Dev Mode or not
if GAMEINFO['devmode']:  # If Dev mode enabled no error catching
    Setup()
    Main()
else:  # Dev mode not enabled so error catching
    try:  # runs the main functions (the whole game bassically)
        Setup()
        Main()
    # end function is run at the end of main loop so you can restart the game
    except (KeyboardInterrupt, SystemExit):  # if keyboard pressed or x out of the game, this is so it doesn't save null data when you press teh keyboard
        raise
        #raise os._exit(0)
    except:
        # AsciiArt.Error()  # TODO Enable once Dynamic Ascii Art
        CreativeMode.saveGame(GAMEINFO['playername'] + " AutoSave") #saves all data
        logGame(GAMEINFO['log'])  # logs the game when it crashes so it can be recreated
        print "Your game has been saved!: SaveFile " + GAMEINFO['playername'] + " AutoSave"
        print "\nSorry your game encountered some kind of bug, we're sorry.\nWe've saved your game but please contact your nearest developer to report the problem if it continues.\nThanks :D"
        raw_input("Type anything to exit: ")


print "done"
