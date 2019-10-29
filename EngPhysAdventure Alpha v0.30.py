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
import MapDisplay


# TODO Make sure these versions and release date are correct
#If there was a title screen it would go here
GAMEINFO['version'] = "0.30"
GAMEINFO['versionname'] = "Alpha v0.30 - Kipling Update"
GAMEINFO['releasedate'] = "July XX, 2019"


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

    if not(GAMESETTINGS['DisableOpening'] or GAMESETTINGS['SpeedRun'] or GAMESETTINGS['DevMode']): Opening.Opening() #plays the opening if disable opening is set to False
    
    print LINEBREAK

    if GAMESETTINGS['DevMode']: GAMEINFO['playername'] = "Doug Fallon"  # Skip name step and names your person Doug
    else: GAMEINFO['playername'] = raw_input("First, what is your name?\n")
    
    PLAYER.name = GAMEINFO['playername']
    NameChange()  # changes the name of all name related things in the game

    x = 2
    y = 3
    z = 1
    dim = 0  # The building or dimension the player is in
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z
    PLAYER.location[3] = dim

    CurrentPlace = MAPS[x][y][z][dim]

    # This prints
    print "You wake up in " + CurrentPlace.name + "\n"
    printT(CurrentPlace.lore)
    printT("(\S)~" + CurrentPlace.name.upper() + "~(\S)" + CurrentPlace.search(MAPS))


    
    GAMEINFO['gamestart'] = time.time()  # Gives the local start date of the game in seconds since epoch of 1970
    CreativeMode.saveGame("basegame")  # Use this to get a base state newgame, keep it in each time so don't have to worry about updating
    # This tyler Kashak has to be after the basegame save or else it will always revert the base game to you spawning as Tyler
    # Enables this ULTRA character is name is Tyler Kashak or in DevMode
    if PLAYER.name == "Tyler Kashak" or GAMESETTINGS['DevMode']: #He realizes he's the main character and can do anything he wants
        # AsciiArt.One()  # TODO Enable once Dynamic Ascii Art
        print "\nHe is beginning to believe\n\nYOU are the One\n"
        PLAYER.__dict__ = Tyler.__dict__  # sets him to the initial Tyler character for strating inventory
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
    KEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys())  # keys of all objects used for spellcheck function
    # acceptable game commands called 'verbs'. Need to add verb to this list for it to work in game decision area
    VERBS =['search', 'inventory', 'equip', 'drop', 'attack', 'talk', 'inspect', 'eat', 'up', 'down', 'left', 'right',
            'back', 'forward', 'kill', 'get', 'wear', 'look', 'drink', 'inhale', 'ingest', 'devour', 'north', 'south',
            'east', 'west', 'fight', 'examine', 'exit', 'leave', 'quit', 'speak', 'throw', 'go', 'move',
            'walk', 'run', 'turn','remember',"wait","sleep",'sit','die','pick','use','give']
    # DIRECTIONS = []  # TODO Make these direction verbs defined here
    DEVVERBS = ['/stats', '/savegame', '/loadgame', '/restart', '/']  # lists of Verbs/keywords ONLY the developer can use
    DEVVERBS.extend(VERBS)  # Combining all the normal verbs into DEVVERBS to make the extended list when in dev mode


    # Main game loop section that runs while the player is alive (player is killed in story once done)
    # TODO don't have main loop based on player alive but on game being played, e.g. gameExit boolean variable instead
    while(PLAYER.alive):

        # if not(GAMESETTINGS['HardcoreMode']): MapDisplay.mini()  # Minimap display area in game
        
        line = raw_input('\nWhat do you want to do?\n')
        GAMEINFO['log'].append(line)
        # this splits it at the first spacing making it the first verb and then the rest as the object noun
        # CURRENTLY the rest of the parser calls simply a function based on the verb and passes it the object noun name
        direction = line.lower().split(" ",1)

        print LINEBREAK  # This linebreak helps split up each turn
        
        for i in range(len(direction)):
           direction[i] = direction[i].strip() # Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]
            if len(verb)>1:
                # if dev mode enabled it accepts special verbs which allows you to use special functions
                if verb == '/420e69': pass  # Does no spell checking so someone doesn't accidentally get 420e69
                elif GAMESETTINGS['DevMode']: verb = SpellCheck(verb,DEVVERBS)
                else: verb = SpellCheck(verb,VERBS)


            if verb in ['u','d','l','r','f','b','up','down','left','right','back','forward',
                        'north','south','east','west', 'n', 's', 'e', 'w', 'ahead', 'backward']:
                CurrentPlace = Move(verb)  # TODO check if CurrentPlace is actually returned and if so, use it
                GAMEINFO['stepcount'] += 1  # increments the stepcount after taking a step (whether sucessful or not)
            elif verb in ['search','look']:
                x,y,z,dim = PLAYER.location
                printT("(\S) ~" + MAPS[x][y][z][dim].name.upper() + "~ (\S)" +MAPS[x][y][z][dim].search(MAPS),72,0.5)


            # TODO if word based description: re-enable stats and remove from DEVVERBs
            elif (verb == '/stats'):
                Stats()
            elif (verb == 'inventory'):
                Inventory()
            elif verb == '/savegame':
                #TODO add: computer name, words and characters per minute, # enemies killed, # items eaten, # items equiped, # enemies talked, # quantum relecs found
                GAMEINFO['runtime'] += (time.time() - GAMEINFO['timestart']) #adds the runtime (initilized to zero) to the session runtime to make the total runtime
                GAMEINFO['timestart'] = time.time() #resets timestart so it's not doubly added at the end
                logGame(GAMEINFO['log']) #logs the game when you save it
                CreativeMode.saveGame(GAMEINFO['playername']) #saves all data
                print "Your game has been saved!: SaveFile " + GAMEINFO['playername']
            elif verb == '/loadgame': #this function loads the game off of the save file. Was having problems with loading
                CreativeMode.loadGame(GAMEINFO['playername']) #loads in the savefile global variables
                GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            elif verb == '/restart': #this restarts the game to the base game
                CreativeMode.loadGame("basegame")  # loads in the savefile global variables
                GAMEINFO['timestart'] = time.time() #reset local variable starttime to current time
            elif verb == '/420e69':  # This toggles game to dev mode for debugging in game
                GAMESETTINGS['DevMode'] = int(not (GAMESETTINGS['DevMode']))
                # Prints throw-off style text while still giving the stat
                print "\nYou don't " + str(GAMESETTINGS['DevMode']) + "understand that command!\n"
                # This section writes devmode to settings.ini file so you can get back to the settings
                # TODO Before release comment out this section so DevMode isn't saved. DevMode in setting file is not for RELEASE
                f = open("settings.ini", "w+")
                for setting in GAMESETTINGS:
                    f.write(setting + "\n" + str(GAMESETTINGS[setting]) + "\n")
                f.close()
            # This normal function exits the game but also saves your progress so you can pick back up.
            # Now at least for normal people you can't metagame by saving and loading files
            elif verb in ['exit','leave','quit',"die"]:
                # A FULL Copy of /savegame function bassically
                if raw_input("\n\nAre you sure you want to save and quit the game?\nYour game will be saved.\nType Y if you wish to save and leave,\nanythine else to continue: \n").lower() in ["y", 'yes','yeah']:
                    GAMEINFO['runtime'] += (time.time() - GAMEINFO[
                        'timestart'])  # adds the runtime (initilized to zero) to the session runtime to make the total runtime
                    GAMEINFO['timestart'] = time.time()  # resets timestart so it's not doubly added at the end
                    logGame(GAMEINFO['log'])  # logs the game when you save it
                    CreativeMode.saveGame(GAMEINFO['playername'])  # saves all data
                    print "Your game has been saved! " + GAMEINFO['playername']  # Don't indicate the save file has save file in the name
                    raw_input("We're sad to see you go :( \nI hope whatever you're doing is more fun.\nPress anything to leave")
                    exit()
            elif verb == "remember":
                x,y,z,dim = PLAYER.location
                place = MAPS[x][y][z][dim]
                print "You entered " + place.name + "\n"
                printT(place.lore)
            elif verb in ["wait","sleep","sit"]:
                printT("Time passes.")
            else:
               print "\nI don't understand that command!\n"

        elif (len(direction) == 2):  # If the command is more than one word long
            verb = direction[0]
            if len(verb)>1:
                # if dev mode enabled it accepts special verbs which allows you to use special functions
                if GAMESETTINGS['DevMode']: verb = SpellCheck(verb, DEVVERBS)
                else: verb = SpellCheck(verb, VERBS)
            # Implemented a pass on the spellcheck for creativemode, will fix this BS later
            # TODO Fix this BS (I.E. make the spellchecker work for multi nounbased structure OR have commands be combined
            if verb == "/": objectName = direction[1]  # Doesn't do spell check if creative command
            # TODO Fix this so don't have to write move verbs in two spots
            # This is a fix so that if you type in a multiword move it doesn't spell check the second part
            elif verb in ['go', 'move', 'walk', 'run', 'turn','look','pick']: objectName = direction[1]
            else: objectName = SpellCheck(direction[1],KEYS)  # Does do spell check if normal

            if verb in ['equip','get','wear']:
                Equip(objectName)
                
            elif verb in ['drop', 'throw']:
                Drop(objectName)

            elif verb in ['attack','kill', 'fight']:
                Attack(objectName)
                
            elif verb in ['talk', 'speak']:
                Talk(objectName)

            elif verb in ['inspect', 'examine']:
                Inspect(objectName)

            elif verb in ['eat','drink','inhale','ingest','devour']:
                Eat(objectName)

            elif verb in ['go', 'move', 'walk', 'run', 'turn']:  # this may or may not work
                CurrentPlace = Move(objectName)
                GAMEINFO['stepcount'] += 1  # increments the stepcount after taking a step (whether sucessful or not)

            elif verb == "/":  # if using a CreativeMode command
                CreativeMode.creative_parser(objectName)
            elif verb == "look":
                if objectName == "around":
                    x, y, z, dim = PLAYER.location
                    printT("(\S) ~" + MAPS[x][y][z][dim].name.upper() + "~ (\S)" +MAPS[x][y][z][dim].search(MAPS),72,0.5)
            elif verb == "pick":  # Allows for pick up to be a thing
                if objectName.lstrip().startswith("up"):  # if up is the second word
                    objectName = objectName.lstrip().split("up")[1].lstrip()  # strips down to just the object name
                    Equip(objectName)  # Equipts it
            elif verb == "use":  # this makes it so you can use items if the interacble is in the area
                x, y, z, dim = PLAYER.location
                # checks all interactables in area to see if item is needed
                for interactable in MAPS[x][y][z][dim].items:  # for all itmes+interactables in the area
                    if isinstance(interactable,Interact):  # if it's in interactable
                        if interactable.need == objectName:
                            print "\nYou use the " + objectName + " with the " + interactable.name + ".\n"
                            Inspect(interactable.name.lower())
            elif verb == "give":
                x, y, z, dim = PLAYER.location
                # checks all Enemies in area to see if item is needed
                for enemy in MAPS[x][y][z][dim].ENEMY:  # for all enemy in the area
                    if enemy.need == objectName:
                        print "\nYou give the " + objectName + " to " + enemy.name + ".\n"
                        Talk(enemy.name.lower())
                Talk(objectName)
            else:
               print "\nI don't understand that command!\n"

        GAMEINFO['commandcount'] += 1  # increments the command count after every command but doesn't print
        #print LINEBREAK  # Got rid of this bottom linebreak to hopefully have the current situation more clear
        Quests.ebta_story()  # runs through the story quests checks and actions
        Quests.sidequests()  # runs through all the sidequest checks and actions
        Quests.events()  # runs through all the events checks and actions

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
    elif raw_input("Type 'C' to continue\n").lower() == 'c':  # If they beat either of the storylines
        Opening.Closing() #plays the closing
        GAMEINFO['log'].append("---THEY WON---") #appends they won at the end of the log file to make it easier find
        if Quests.ebta_story() == 1: #The bad storyline ending
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
        elif Quests.ebta_story() == 2: #The good storyline ending.
            print "Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
        if GAMESETTINGS['SpeedRun']: DisplayTime(GAMEINFO['runtime']) #displays the runtime then all other status
        if GAMESETTINGS['SpeedRun']:print "Total Step Count: ", GAMEINFO['stepcount'], "\nTotal Command Count: ", GAMEINFO['commandcount']
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


# ---------GAME STARTS HERE  ---------

# TODO Reset settings before release before release

# Reading in game settings, has to be at start of game befor anything so it reads in settings
try:  # In case settings file isn't there
    with open("settings.ini", 'r') as f:
        data = f.readlines()  # reads in data seperated by newline into a list
    f.close()
    data = [f.strip() for f in data]  # removes the \n in each list element wise (very useful for list operations)
    for i in range(0, len(data), 2):
        GAMESETTINGS[data[i]] = int(data[i+1])  # Reading in file data in attribute value order, value should be an int
except:
    #print "\n\nSomething is Wrong with the Setting.ini file!\n\n"
    print "\n\nNo Settings Detected\n\n"


# Start Screen is after reading in settings so it can skip start screen if enabled
Opening.StartScreen()  # Startscreen loop where you can play new game, loadgame, choose settings, or exit

# The Actual Start of the game when you hit Play, depending on if in Dev Mode or not
if GAMESETTINGS['DevMode']:  # If Dev mode enabled no error catching
    Setup()
    Main()
else:  # Dev mode not enabled so error catching
    try:  # runs the main functions (the whole game bassically)
        Setup()
        Main()
    # end function is run at the end of main loop so you can restart the game
    except:
        # AsciiArt.Error()  # TODO Enable once Dynamic Ascii Art
        CreativeMode.saveGame(GAMEINFO['playername']) #saves all data
        logGame(GAMEINFO['log'])  # logs the game when it crashes so it can be recreated
        print "Your game has been saved!: SaveFile " + GAMEINFO['playername']
        print "\nSorry your game encountered some kind of bug, we're sorry.\nWe've saved your game but please contact your nearest developer to report the problem if it continues.\nThanks :D"
        raw_input("Type anything to exit: ")
