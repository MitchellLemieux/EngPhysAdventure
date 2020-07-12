#This is the file used for most backend, interaction, startup/global variables,  functions of the game


from GameClasses import *
import StartUp
import AsciiArt
import time
import os  # used to put files in the cache folder
from printT import * #import it all
from Colour import *
from sys import platform



# This is where the global variables are instantiated and defined. Global variables used to pass info between functions
# TODO will be changed to pass by reference) and dictionaries used to store many variables/objects in one
#   place while making it clear in the code which one is being referenced

MAPS = StartUp.WorldMap()
ITEMS = StartUp.ItemDictionary()
ENEMIES = StartUp.EnemyDictionary()
INTERACT = StartUp.InteractDictionary()
DIMENSIONS = ["OverWorld", "BSB", "Capstone Room", "Green Lake", "Haunted Forest","Cabin in the Woods"]  # List of interior names with the index location being the dimension/building number
# ex) 0 is OverwWord, 1 is BSB, 2 is capstone room, etc




GAMEINFO = {'version':0,'versionname':"", 'releasedate':"",'playername':"",'gamestart':0,'timestart':0,
            'runtime': 0, 'stepcount':0,'commandcount':0,'log': [],"layersdeep":0,"savepath": "","datapath":"",
            "help": "", "devmode": 0,'scriptdata': [],'loadgame':0,'winner':0}
#this dictionary is used to store misc game info to be passed between function:
# speedrun time, start time, etc. Values are initialized to their value types
# version is version of the game, gamestart is the first start time of the game, runtime is the total second count,
# log is log of all player input, layers deep is how many layers deep in the laptop quest you are, help is help prinout,
# script is used to store script data to run through assisted
# loadgame is a flag for loading to skip the setup




GAMEINFO['help'] = "(\S)The complexities of reality have been distilled into 4 things: " + mapcolour + "~Places~" + textcolour + ", " + itemcolour + "items" + textcolour + ", " + interactcolour + "interacts" + textcolour + ", and " + personcolour + "people" + textcolour + ". The colour helps denote each." \
                    "(\S) (\S)These are the commands your brain can handle in this state:" \
                    "(\S)-(s)search (look at what's around you)" \
                    "(\S)-(l,r,f,b,u,d)go left/right/front/back/up/down (you can't turn)" \
                    "(\S)-(e)equip " +itemcolour+ "item" +textcolour+ " (picks them up into your inventory, replaces what you're wearing/holding)" \
                    "(\S)-(dr)drop " +itemcolour+ "item" +textcolour+ " (removes them from your inventory)" \
                    "(\S)-(ex)examine " +itemcolour+ "item" +textcolour+ "" \
                    "(\S)-(ea)eat " +itemcolour+ "item" +textcolour+ "" \
                    "(\S)-(i)inventory (check inventory)" \
                    "(\S)-(c)condition (Sees how you're doing)" \
                    "(\S)-(ex)examine " +interactcolour+ "interact" +textcolour+ " (uses an item on the interacable when you have the right thing) " \
                    "(\S)-(us)use " +itemcolour+ "item" +textcolour+ " (use an item on a nearby interactable)" \
                    "(\S)-(t)talk " +personcolour+ "person" +textcolour+ "  (gives them an item when you have the right thing)" \
                    "(\S)-(g)give " +itemcolour+ "item" +textcolour+ " (tries to give an object to a person around you)" \
                    "(\S)-(a)attack " +personcolour+ "person" +textcolour+ " (Force may be necessary but be careful, you're limited by what you have)" \
                    "(\S)-(r)remember (remember what you were doing here earlier)" \
                    "(\S)-exit (exit your body, " +indicatecolour+ "ALWAYS EXIT" +textcolour+ " or it " +losecolour+ "won't save" +textcolour+ "!)" \
                    "(\S)-shortcuts (gives shortcuts list)" \
                    "(\S)-(h)help (gives you this list again)" \
                    "(\S) (\S)While you may accept more commands that is up to you to discover."



QUESTS = {}  #initializing the quests global variable to be later writen into

# These settings are global and are in the settings.ini file so they don't need to be set every time you startup
GAMESETTINGS = {'DisableOpening': 0, 'SpeedRun': 0, 'HardcoreMode':0}
# disable openning, speedrun disables openning;lore read times; might disable secrets or opens them,
# hardcore for now disables eating but might make enemies harder,
# DevMode disables the main error catching + Startup Blip


STARTLOCATION = (2,3,1,0)
STARTHEALTH = 100


EMPTYHEAD = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','head',(0,0,0),-101)
EMPTYBODY = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','body',(0,0,0),-101)
EMPTYHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','hand',(0,0,0),-101)
EMPTYOFFHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','off-hand',(0,0,0),-101)
EMPTYINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
STARTINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':ITEMS["polaroid photograph"]}
#STARTINV = {'head':ITEMS['gas mask'],'body':ITEMS['okons chainmail'],'hand':ITEMS['iron ring'],'off-hand':ITEMS['green bang bong']}

# OBJECTS need to be UNIQUE so that the location doesn't get messed up when duplicate objects in the game
TYINV = {'head':ITEMS["tyler's visor glasses"],'body':ITEMS["tyler's big hits shirt"],'hand':ITEMS["tyler's hulk hands"],'off-hand':ITEMS["tyler's green bang bong"]} #gets to have the Iron Ring when he graduates
BRENSTARTLOCATION = (2,3,1,0)  # Dev start location
# (4,0,0,4)  haunted forest
# (2,3,1,0)  default location
# EACH INVENTORY HAS TO BE UNIQUE
#BRENINV = EMPTYINV  # THIS CAUSED GHOSTING AND DUPLICATION I THINK BECAUSE OF same referenced object
BRENINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}  # needs to be unique or else ghosting
#BRENINV = {'head':ITEMS["tyler's visor glasses"],'body':ITEMS["tyler's big hits shirt"],'hand':ITEMS["tyler's hulk hands"],'off-hand':ITEMS["tyler's green bang bong"]} #gets to have the Iron Ring when he graduates


# TODO Make PLAYER into PLAYERS a dictionary of playable characters objects
PLAYER = Character('Minnick',list(STARTLOCATION),STARTHEALTH,STARTINV,EMPTYINV)
Tyler = Character('Tyler Kashak',list(STARTLOCATION),999,TYINV,EMPTYINV)
BREN007PIE = Character('Brendan Fallon',list(BRENSTARTLOCATION),999,BRENINV,EMPTYINV)
# MAPS[6][1][1][0].placeItem(ITEMS["big hits shirt"]) #having these spawn the items in the map after should get rid of the wierd bug from having Tyler Kashak having them to start
# MAPS[0][3][0][0].placeItem(ITEMS["hulk hands"])


# --- Setting up Game Folder ---
# Setting up the game path for the game to the cache folder
# Using os here to get the current file path and the os.path.join to add the // or \ depending on if it's windows or linuix
# joining an empty string just gives a slash

#print os.getcwd()  # gets the CWD of the file
#print os.getenv('APPDATA')  # The app data working directory. Use this instead of CWD so can write if not admin




if platform == "win32":
    try:
        GAMEINFO['savepath'] = os.path.join(os.getenv('APPDATA'), "EngPhysTextAdventure", "", "cache",
                                            "")  # Used for hidden saves + logs
        GAMEINFO['datapath'] = os.path.join(os.getenv('APPDATA'), "EngPhysTextAdventure", "")  # Used for setting file
        os.makedirs(GAMEINFO['savepath'])  # gets the directory then makes the path if it's not there
        # CAN"T have last \ in the file path so have to use [:-1] to use all string but the last character
        # Not hiding individual files so can access and also will throw an error to access if files are hidden
        os.system("attrib +h " + GAMEINFO['savepath'][:-1])  # Makes cache file hidden

    except:
        printT(" (\S)")  # does nothing if the path is already there
elif platform == "linux" or platform == "linux2":  # Linux
    try:
        GAMEINFO['savepath'] = os.path.join(os.getcwd(), "EngPhysTextAdventure", "", "cache", "")  # Used for hidden saves + logs
        GAMEINFO['datapath'] = os.path.join(os.getcwd(), "EngPhysTextAdventure", "")  # Used for setting file
        os.makedirs(GAMEINFO['savepath'])  # gets the directory then makes the path if it's not there
    except:
        printT(" (\S)")  # does nothing if the path is already there
elif platform == "darwin":  # OS X/MAC
    try:
        GAMEINFO['savepath'] = os.path.join(os.getcwd(), "EngPhysTextAdventure", "", "cache", "")  # Used for hidden saves + logs
        GAMEINFO['datapath'] = os.path.join(os.getcwd(), "EngPhysTextAdventure", "")  # Used for setting file
        os.makedirs(GAMEINFO['savepath'])  # gets the directory then makes the path if it's not there
    except:
        printT(" (\S)")  # does nothing if the path is already there




# TODO Make these functions into class methods related to each class
def Equip(Item):  # Item is a string not an object
    global PLAYER
    global ITEMS
    global MAPS
    global INTERACT
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]
    Place = MAPS[x][y][z][dim]
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location:  # if name of Item asked for in parser is in ITEMS dictionary
        # this is different than the equip method in the Character class for some reason
        # Makes sure the item is dropped at the current location
        # TODO Redo this drop and equip structure. Is dumb and can cause duplicates/ghosting
        drop = PLAYER.equip(ITEMS[Item])  # does the equip method on the player
        Place.removeItem(ITEMS[Item])   # removes that item from the invoirnment
        Place.placeItem(drop)  # places the drop if there's something to drop
        ITEMS[Item].quest = True  # quest/inspect flag is true

    # other acceptations for weird requests
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:  # Interacts
        printT("Maybe if you were at your peak you could carry a " + str(INTERACT[Item].colouredname) + " but not with this migraine.")
    elif Item in ENEMIES and list(ENEMIES[Item].location) == PLAYER.location and ENEMIES[Item].alive: # People
        printT("You attempt to pick up " + ENEMIES[Item].colouredname + " but you're not that close... (\S)And now you're both really uncomfortable.")
    elif Item in ENEMIES and list(ENEMIES[Item].location) == PLAYER.location and not ENEMIES[Item].alive:  # Dead People
        printT("That's pretty messed up. You probably shouldn't pick up " +deadpersoncolour+ ENEMIES[Item].name + textcolour+ "'s body.")
    else:
        printT(" (\S)You can't find a " +itemcolour+ Item +textcolour+ " around here. Maybe it's your hungover brain.")


def Drop(Item):  # Item is a string not an object
    global MAPS
    global PLAYER
    global ITEMS
    global ENEMIES
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]
    Place = MAPS[x][y][z][dim]
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location:
        # TODO Redo this drop and equip structure. Is dumb and can cause duplicates/ghosting
        drop = PLAYER.drop(ITEMS[Item])  # the player drop method that will return the item dropped
        Place.placeItem(drop)  # places the drop on the ground
        # Same as equip function. 'None' passed to function if item doesn't exist

    # other acceptations for weird requests
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location: # Interacts
        printT("You probably shouldn't drop the " + str(INTERACT[Item].colouredname) + ". It might break.")
    elif Item in ENEMIES and list(ENEMIES[Item].location) == PLAYER.location and ENEMIES[Item].alive: # People
        printT("You drop " + ENEMIES[Item].colouredname + " but they were never yours, to begin with. (\S)Now you just have one less friend...")
    elif Item in ENEMIES and list(ENEMIES[Item].location) == PLAYER.location and not ENEMIES[Item].alive: # Dead People
        printT("You pick up " +deadpersoncolour+ ENEMIES[Item].name +textcolour+ "'s body and drop it. Do you get a kick out of this?")
    else:
       printT("Maybe you're still drunk?. You aren't carrying a " +itemcolour+ Item +textcolour+ ".")



def Move(direction,DIRECTIONWORDS,DIRECTIONSHORTCUTS):
    global MAPS
    global PLAYER
    global ENEMIES
    global INTERACT
    global ITEMS
    bf = ENEMIES['brendan fallon']
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]
    currentplace = MAPS[x][y][z][dim]  # Saving your current map location to a variable
    place = 0
    # Direction parsing and redefining so that it matches walls
    if direction in DIRECTIONSHORTCUTS: pass  # Don't need to parse direction if a shortcut
    elif direction == 'up': direction = 'u'
    elif direction == 'down': direction = 'd'
    elif direction in ['front', 'forward', 'ahead','west']: direction = 'f'
    elif direction in ['back', 'backward','east']: direction = 'b'
    elif direction in ['left', 'south']: direction = 'l'
    elif direction in ['right','north']: direction = 'r'
    else:  # if the direction isn't in the accepted directions
        printT("You stumble over not sure where you were trying to go. Your brain doesn't understand " + direction + ".")
        return

    if direction not in currentplace.walls:
        # TODO Make these direction additions transformations (matrix transforms) that add to a tuple
        # These are the direction parsing so it moves the desired coordinates
        if direction == 'u': z += 1
        elif direction == 'd': z -= 1
        elif direction == 'f': y += 1
        elif direction == 'b': y -= 1
        elif direction == 'l': x -= 1
        elif direction == 'r': x += 1
        else:  # This is just a catch, shouldn't happen
            printT("You stumble over not sure where you were trying to go. Something went wrong in your brain")
            return

        # TODO This is where links come in which direct into interriors

        place = MAPS[x][y][z][dim]  # place is new location requested

        # Interrior Links: If the spot has a link might be teliported/moved to that place
        for link in currentplace.links:  # if there is links in it it will loop through
            if direction in link:  # Searching all the links to see if any links refer to that direction
                if dim == 0 and link[4] != 0:
                    printT("You go inside " +mapcolour+ DIMENSIONS[link[4]] +textcolour+ ".")  # When going to non-Overworld it says going inside
                elif dim != 0 and link[4] == 0: # When going to overworld from non
                    printT("You go outside.")
                elif dim != link[4]:  # Leaving one interior and entering another
                    printT("You leave " +mapcolour+ DIMENSIONS[dim] +textcolour+ " and enter " +mapcolour+ DIMENSIONS[link[4]] +textcolour+ ".")

                x = link[1]
                y = link[2]
                z = link[3]
                dim = link[4]
                place = MAPS[x][y][z][dim]  # Overwrites place with the link location


    if place:
        PLAYER.location[0] = x
        PLAYER.location[1] = y
        PLAYER.location[2] = z
        PLAYER.location[3] = dim
        bfchance = 0.003
        if PLAYER.inv['body'] == ITEMS['tony hawk shirt']:
            bfchance += 0.007
            #bfchance += 0.50  # TODO Remove this before final build


        if bf.location != (None,None,None,None):
            MAPS[bf.location[0]][bf.location[1]][bf.location[2]][bf.location[3]].removeEnemy(bf)
        if random() <= bfchance:
            printT(" (\S)You see A " +wincolour+ "BRENDAN FALLON" +textcolour +".")
            MAPS[x][y][z][dim].placeEnemy(bf)
            # AsciiArt.Hero()  # TODO Enable once Dynamic Ascii Art

        place.search(MAPS, DIMENSIONS,GAMESETTINGS)  # searches and prints the place
        return place  # idk why but this returns place and I'm keeping it here so yeah




    else:
        PLAYER.location[0] = currentplace.location[0]
        PLAYER.location[1] = currentplace.location[1]
        PLAYER.location[2] = currentplace.location[2]
        PLAYER.location[3] = currentplace.location[3]
        printT(" (\S)Your body " +losecolour+ "can't" +textcolour+ " go that way! (\S)")
        return currentplace

#Combat System

def Combat(P,E):
     if E:
        #Speed
        PSpeed = P.stats[2]
        ESpeed = E.stats[2]

        #Determine who goes first
        if PSpeed>ESpeed:
            First = P
            Second = E
        elif PSpeed<ESpeed:
            First = E
            Second = P
        else:
            Combatants = [E,P]
            First = choice(Combatants)
            Combatants.remove(First)
            Second = Combatants[0]
        #Max damage each can deal
        FDamage = abs(First.stats[0])*First.stats[0]/(Second.stats[1]+1)
        SDamage = abs(Second.stats[0])*Second.stats[0]/(First.stats[1]+1)
        #Starting health
        FSHealth = First.health
        SSHealth = Second.health
        while (P.health and E.health):
            if First.health:
                Damage = int(uniform(0.7, 1)*FDamage)
                if GAMEINFO['devmode']: printT(First.name + " deals " + str(Damage) + " to " + Second.name)
                Second.health = max(0,Second.health - Damage)
                if GAMEINFO['devmode']: printT(Second.name + " health: " + str(Second.health))
            if Second.health:
                Damage = int(uniform(0.7, 1)*SDamage)
                if GAMEINFO['devmode']: printT(Second.name + " deals " + str(Damage) + " to " + First.name)
                First.health = max(0,First.health - Damage)
                if GAMEINFO['devmode']: printT(First.name + " health: " + str(Second.health))
     # TODO Re-implement combat and number with word ques instead of numbers. Also say: _ strikes first
     # if First == P:
     #     print "\nYou attack dealing " + str(SSHealth - Second.health) + " damage.\n" + Second.name + " deals " + str(FSHealth - First.health) + " damage.\n"
     #     print  "You have " + str(First.health) + " health remaining.\n" + Second.name + " has " + str(Second.health) + " health remaining.\n"
     # else:
     #     print "\n"+First.name + " dealt " + str(SSHealth - Second.health) + " damage.\n" + "You attack dealing " + str(FSHealth - First.health) + " damage.\n"
     #     print  "You have " + str(Second.health) + " health remaining.\n" + First.name + " has " + str(First.health) + " health remaining.\n"
     if P.health == 0:
        P.alive = False
        return 0
     if E.health == 0:
        E.alive = False
        return 1

def Attack(E):  # E is a string not an object
    global ENEMIES
    global MAPS
    global PLAYER
    global ITEMS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]
    CurrentPlace = MAPS[x][y][z][dim]
    if E in ENEMIES and (list(ENEMIES[E].location) == PLAYER.location) and (ENEMIES[E].alive):
        enemy = ENEMIES[E] #making it the object from the name
        bgchance = 0.01
        if PLAYER.inv['head'] == ITEMS['helm of orin bearclaw']:
            bgchance += 0.10
        if PLAYER.inv['body'] == ITEMS['big hits shirt']:
            bgchance += 0.05
        if PLAYER.name == "Big Hits Twofer":  # This is for testing big hits events
            bgchance = 20

        if random() <= bgchance: #bigHits feature TODO have oblivion sound effects
            # AsciiArt.BigHits()  # TODO Enable once Dynamic Ascii Art
            printT(" (\S)An oblivion gate opens and a " +lightmagenta+"purple faced hero" +textcolour +" in " +lightblack+"ebony armour" +wincolour+ " punches " +personcolour+ enemy.name +textcolour+ " to death.")
            printT(enemy.Dinfo) #slow version
            enemy.alive = False
            if enemy.drop:
               printT(" (\S)" +enemy.colouredname+ " dropped the " + ITEMS[enemy.drop].colouredname + ".")
               CurrentPlace.placeItem(ITEMS[enemy.drop])
        else:
           Outcome = Combat(PLAYER,enemy)
           if Outcome:
               printT("You " +wincolour + "defeated " + enemy.colouredname + ". (\S)")
               printT(enemy.Dinfo)
               if enemy.drop:
                   printT( enemy.colouredname + " dropped a " + ITEMS[enemy.drop].colouredname + ".")
                   CurrentPlace.placeItem(ITEMS[enemy.drop])
           else:
               printT("Oh no! " + enemy.colouredname + " " +losecolour + "defeated" + textcolour+ " you! (\S)You died, without ever finding your " +wincolour+"iron ring" + textcolour +".")

    # other acceptations for weird requests
    elif E in INTERACT and list(INTERACT[E].location) == PLAYER.location: # Interacts
        printT("You probably shouldn't attack the " + str(INTERACT[E].colouredname) + ". You might get in major trouble.")
    elif E in ITEMS and list(ITEMS[E].location) == PLAYER.location: # Items
        printT("You probably shouldn't attack the " + ITEMS[E].colouredname + " it might go badly.")
    elif E in ENEMIES and list(ENEMIES[E].location) == PLAYER.location and not ENEMIES[E].alive: # Dead People
        printT("Umm... Okay. You attack " +deadpersoncolour+ ENEMIES[E].name +textcolour+ " and they're still dead...")

    else:
        printT("(\S)" + personcolour+ str(E) + textcolour+ " doesn't appear to be here.")


def Talk(E):  # E is a string not an object
    global ENEMIES
    global MAPS
    global PLAYER
    global ITEMS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]

    if E in ENEMIES and (list(ENEMIES[E].location) == PLAYER.location) and (ENEMIES[E].alive):
        enemy = ENEMIES[E]
        if enemy.need and PLAYER.inv[ITEMS[enemy.need].worn]==ITEMS[enemy.need]and not enemy.quest:
            printT(enemy.colouredname + " took the " + ITEMS[enemy.need].colouredname+ ".")
            printT(enemy.Sinfo)  # default print speed
            ITEMS[enemy.need].location = (None, None, None)  # Brendan added this, used to clear the item location
            PLAYER.inv[ITEMS[enemy.need].worn] = PLAYER.emptyinv[ITEMS[enemy.need].worn]
            PLAYER.updateStats()
            enemy.quest = True
            if enemy.drop:
                MAPS[x][y][z][dim].placeItem(ITEMS[enemy.drop])
                printT("You see a " + ITEMS[enemy.drop].colouredname +". (\S)")
                enemy.drop = None
        elif enemy.quest and enemy.drop:
            printT(enemy.Sinfo)
            MAPS[x][y][z][dim].placeItem(ITEMS[enemy.drop])
            printT( "You see a " + ITEMS[enemy.drop].colouredname +". (\S)")
            enemy.drop = None
        elif enemy.quest:
            printT(enemy.Sinfo)
        else:
            printT(enemy.info)
        if enemy.aesthetic and not(GAMESETTINGS['HardcoreMode']):
            printT("They don't seem very helpful to you.")
        enemy.spoke = True
        if GAMEINFO['devmode']:  # If in devmode can see the stats/quest of enemies
            printT("HEALTH: " + str(ENEMIES[E].health))
            printT("ATK : " + str(ENEMIES[E].stats[0]))
            printT("DEF : " + str(ENEMIES[E].stats[1]))
            printT("SPD : " + str(ENEMIES[E].stats[2]))
            printT("NEED : " + str(ENEMIES[E].need))
            printT("DROP : " + str(ENEMIES[E].drop))
            printT("QUESTFlag : " + str(ENEMIES[E].quest))
            printT("SPOKE : " + str(ENEMIES[E].spoke))
            printT("Aesthetic : " + str(ENEMIES[E].aesthetic))


    # other acceptations for weird requests
    elif E in INTERACT and list(INTERACT[E].location) == PLAYER.location: # Interacts
        printT("You talk at the " + str(INTERACT[E].colouredname) + ". Best conversation you've had in a while.")
    elif E in ITEMS and list(ITEMS[E].location) == PLAYER.location: # Items
        printT("You talk at the " + ITEMS[E].colouredname + ". Still better than the Student Wellness Centre person.")
    elif E in ENEMIES and list(ENEMIES[E].location) == PLAYER.location and not ENEMIES[E].alive: # Dead People
        printT("Most people don't believe in talking to the dead. But you try talking to " +deadpersoncolour+ ENEMIES[E].name +textcolour+ " anyways.")

    else:
        printT("(\S)" + personcolour + str(E) + textcolour + " doesn't appear to be here.")

# TODO Re-implement stats and number with word ques instead of numbers
def Stats():
    global PLAYER
    if PLAYER.health > 99: printT("You're in perfect health.")
    elif PLAYER.health > 90: printT("You feel really great!")
    elif PLAYER.health > 80: printT("You feel a little banged up but not too bad.")
    elif PLAYER.health > 60: printT("You're pretty badly beat up but still kicking.")
    elif PLAYER.health > 40: printT("You're very injured. Probably a lot of broken bones. Should get that checked out.")
    elif PLAYER.health > 20:printT("You're EXTREMELY injured. It's a wonder you can even walk.")
    elif PLAYER.health > 10: printT("You're bleeding profusely and barely alive. Why are you not in a hospital?")
    elif PLAYER.health > 0:printT("You're on the verge of death, don't go towards the light.")

    if GAMEINFO['devmode']:  # If in devmode can see the stats/quest of enemies
        printT("\nHEALTH: " + str(PLAYER.health))
        printT("ATK: " + str(PLAYER.stats[0]))
        printT("DEF: " + str(PLAYER.stats[1]))
        printT("SPD: " + str(PLAYER.stats[2])+" (\S)")

def Inspect(Item): #Item is the inspect item string not an object
    global MAPS
    global ITEMS
    global PLAYER
    global INTERACT
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]

    #If item in location
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location: #this is for item = equipment
        printT("" + itemcolour+ ITEMS[Item].colouredname.upper() +textcolour + "",72,0)
        printT(ITEMS[Item].info,72,0)  # fast version for reading things

        ITEMS[Item].quest = True  # sets the quest/inspected flag to true
        # TODO re-implement inspecting item with words instead of numbers
        deltaATK = ITEMS[Item].stats[0]-PLAYER.inv[ITEMS[Item].worn].stats[0]  # " more powerful"
        deltaDEF = ITEMS[Item].stats[1]-PLAYER.inv[ITEMS[Item].worn].stats[1]  # " better defended"
        deltaSPD = ITEMS[Item].stats[2]-PLAYER.inv[ITEMS[Item].worn].stats[2]  # " faster"

        descriptornumbers = [5,10,25,50,100,1000]
        descriptors = ["Slightly", lightblack+"A good bit", lightblue+"A significant amount",red+"A very large amount", lightwhite+"A very very large amount", lightyellow +"AN UNGODLY amount"]
        #5 = a bit
        #10 = a lot
        #25 = a significant amount
        #50 = A TON
        #100 = a very large amount
        #1000 = AN UNGODLY amount

        if deltaATK > 4 or deltaDEF > 4 or deltaSPD > 4:  # if any of these are different
            desc = " (\S)This looks like it would make me: (\S)"
            for i in range(len(descriptors)):  # loops through descriptors
                if descriptornumbers[i] > deltaATK and deltaATK > 4:
                    desc += descriptors[i-1] +textcolour+ " more powerful. (\S)"
                    break
            for i in range(len(descriptors)):  # loops through descriptors
                if descriptornumbers[i] > deltaDEF and deltaDEF > 4:
                    desc += descriptors[i-1] +textcolour+ " better defended. (\S)"
                    break
            for i in range(len(descriptors)):  # loops through descriptors
                if descriptornumbers[i] > deltaSPD and deltaSPD > 4:
                    desc += descriptors[i-1] +textcolour+ " faster. (\S)"
                    break
            printT(desc)



        if GAMEINFO['devmode']:  # If in devmode can see the stats
            printT("ATK : " + str(ITEMS[Item].stats[0]) + " " + "("+str(ITEMS[Item].stats[0]-PLAYER.inv[ITEMS[Item].worn].stats[0])+")")
            printT("DEF : " + str(ITEMS[Item].stats[1]) + " " + "("+str(ITEMS[Item].stats[1]-PLAYER.inv[ITEMS[Item].worn].stats[1])+")")
            printT("SPD : " + str(ITEMS[Item].stats[2]) + " " + "("+str(ITEMS[Item].stats[2]-PLAYER.inv[ITEMS[Item].worn].stats[2])+")")
            printT("WORN: " + str(ITEMS[Item].worn).upper())
            printT("QUEST Flag: " + str(ITEMS[Item].quest))
            if ITEMS[Item].health: #if edible it shows that health stat plus what your final health would be if eaten
                printT( "Eaten Health: " + str(ITEMS[Item].health) + " (\S)") #+ str(ITEMS[Item].health) + " (" + str(min(100,PLAYER.health + ITEMS[Item].health))+")" +"\n"
            else:
                print("")
    # If the entered item is an intractable and is at that location
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:  # this is for item = interactable
        # TODO Have Interactables be able to use lists (to drop multiple things), tuples(to place unique objects)
        if INTERACT[Item].need and (PLAYER.inv[ITEMS[INTERACT[Item].need].worn]==ITEMS[INTERACT[Item].need] or ITEMS[INTERACT[Item].need] in MAPS[x][y][z][dim].items): #if you're wearing item.need or it's on the ground the interactable needs worn on your body
            if PLAYER.inv[ITEMS[INTERACT[Item].need].worn]==ITEMS[INTERACT[Item].need]:  # if in the players hand
                PLAYER.inv[ITEMS[INTERACT[Item].need].worn] = PLAYER.emptyinv[ITEMS[INTERACT[Item].need].worn]
            elif ITEMS[INTERACT[Item].need] in MAPS[x][y][z][dim].items:  # if around the area
                MAPS[x][y][z][dim].removeItem(ITEMS[INTERACT[Item].need])
                ITEMS[INTERACT[Item].need].location = (None,None,None,None)
            INTERACT[Item].quest = True  # this turns on the quest flag for the interactable once interacted with if you have the item
            printT("" +interactcolour+ INTERACT[Item].colouredname.upper() +textcolour+ "" ,72,0)  # Due to the upper it removes the colour
            printT(INTERACT[Item].Sinfo + "(\S)",72,0)  # special slow version
            PLAYER.updateStats()  # TODO stats should automatically update whenver player state is changed
            ITEMS[INTERACT[Item].need].location=(None,None,None) # Brendan added this, used to clear the item location
            if INTERACT[Item].drop:
                INTERACT[Item].drop_objects(Item,x,y,z,dim,MAPS,ITEMS,INTERACT,ENEMIES)  # drops the proper object


        elif INTERACT[Item].need == None or INTERACT[Item].need == "":  # Has no needed Items (I.E. it's a quest interface or a vendor or a trigger)
            INTERACT[Item].quest = True  # this turns on the quest flag so it can trigger quest events
            printT("" +interactcolour+ INTERACT[Item].colouredname.upper() +textcolour+ "" ,72,0)  # Due to the upper it removes the colour
            printT(INTERACT[Item].info,72,0)
            printT(INTERACT[Item].Sinfo,72,0)

            if INTERACT[Item].drop:
                INTERACT[Item].drop_objects(Item, x, y, z, dim, MAPS, ITEMS, INTERACT, ENEMIES)

        else:
            printT("" +interactcolour+ INTERACT[Item].colouredname.upper() +textcolour+ "" ,72,0)  # Due to the upper it removes the colour
            printT(INTERACT[Item].info,72,0.1) #fast version
        if GAMEINFO['devmode']:  # If in devmode can see the stats/quest of enemies
            printT("NEED : " + str(INTERACT[Item].need))
            printT("DROP : " + str(INTERACT[Item].drop))
            printT("QUESTFlag : " + str(INTERACT[Item].quest))
            printT("Aesthetic : " + str(INTERACT[Item].aesthetic))

        if INTERACT[Item].aesthetic and not(GAMESETTINGS['HardcoreMode']):  # if it's aesthetic and not in hardcore mode
            printT("This doesn't look very useful.")


    # other acceptations for weird requests
    # If you try to inspect a person
    elif Item in ENEMIES and ((list(ENEMIES[Item].location) == PLAYER.location)) and (ENEMIES[Item].alive):
        printT(" (\S)It's rude to stare at people!")


    else:
        printT(" (\S)You can't find " + Item + " around here. Maybe it's your hungover brain.")

def Inventory():
    global PLAYER
    # Player inventory is a dictionary of objects so can access and print them out
    printT(" (\S){1}HEAD: " + PLAYER.inv['head'].colouredname,72,0.25)
    printT("{2}BODY: " + PLAYER.inv['body'].colouredname,72,0.25)
    printT("{3}HAND: " + PLAYER.inv['hand'].colouredname,72,0.25)
    printT("{4}OFF-HAND: " + PLAYER.inv['off-hand'].colouredname + " (\S)",72,0.25)
    # This old method is more general/expandable but doesn't do them in order
    # for i in PLAYER.inv:
    #     print i.upper() + ": " + PLAYER.inv[i].name


def Eat(Item):  # Item is a string not an object
    global PLAYER
    global ITEMS
    global MAPS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    dim = PLAYER.location[3]

    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location and not(GAMESETTINGS['HardcoreMode']):
        if Item == "jar of peanut butter" and (PLAYER.name in ["Mitchell Lemieux","Erik Reimers"]):
            printT("Oh NO! You're " + PLAYER.name + " ! Don't you remember? YOU'RE" +losecolour+" ALERGIC TO PEANUT BUTTER" +textcolour+"! You "+losecolour+"DIE" +textcolour+" due to your lack of responsibility.")
            PLAYER.health = 0
            PLAYER.alive = False
        elif ITEMS[Item].health:
            PLAYER.health = PLAYER.health + ITEMS[Item].health
            PLAYER.health = min(PLAYER.maxhealth, PLAYER.health) #made the minimum of your added health and food so players health doesn't clip over
            PLAYER.health = max(PLAYER.health, 0)  # prevents clipping bellow 0
            printT(" (\S)You've eaten the " + ITEMS[Item].colouredname + ".")
            # TODO Reimplement health/food indicators with words
            if GAMEINFO['devmode']: printT(" (\S)HEALTH: "+ str(PLAYER.health)+ " (\S)")  # if in DevMode can see stats
            if PLAYER.health == 0:
                PLAYER.alive = False
            ITEMS[Item].location = (None, None, None) #used to clear the item location
            if ITEMS[Item] == PLAYER.inv[ITEMS[Item].worn]:
                PLAYER.inv[ITEMS[Item].worn] = PLAYER.emptyinv[ITEMS[Item].worn]
                ITEMS[Item].location = (None, None, None)
                PLAYER.updateStats()
                printT("The " + ITEMS[Item].colouredname + " has been removed from your inventory. (\S)")
            else:
                MAPS[x][y][z][dim].removeItem(ITEMS[Item])
        else:
            printT("You can't eat a " + ITEMS[Item].colouredname + "!")


    # other acceptations for weird requests
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:  # Interacts
        printT("Hmm... You don't think a " + str(INTERACT[Item].colouredname) + " would taste good. Let alone be edible.")
    elif Item in ENEMIES and (list(ENEMIES[Item].location) == PLAYER.location):  # If you attempt to eat someone
        if (ENEMIES[Item].alive):
            printT("You attempt to eat " + ENEMIES[Item].colouredname + "'s arm...(\S) (\S)They pull away ask you to politely 'Not'.")
        else:
            printT("OMG, WHAT'S WRONG WITH YOU. (\S)I know you're hungry but please find a more vegan option.")

    else:
        printT(" (\S)You can't find a " +itemcolour+ Item +textcolour+ " around here. Maybe it's your hungover brain.")


# BackEnd Functions

def logGame(log): #this makes a log file which records all player actions for debugging
    # TODO add settings and more description to log
    # metacache is a fake name for the log file. As well, saved as .plp for obfuscation purposes
    fpath = GAMEINFO['savepath'] + "MetaChache " + GAMEINFO['playername']+".plp"
    f = open(fpath,"w+")
    for i in range(len(log)):
        f.write(str(log[i]) + '\n')
    f.close()

def NameChange(playername):  # A dumb backend workaround to change the players name. TODO other strategies could have startup instantatied after name is defined
    global PLAYER  # The main character. player is an object instance of class character.
    global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    global GAMESETTINGS  # The game settings that are saved in the game
    # ENEMIES['yourself'].name = playername
    # Can't just update the name, need to update the dictionary name
    try:
        ENEMIES['yourself'].name = playername  # yourself gets renamed to player name
        ENEMIES['yourself'].colouredname = "" +personcolour+ playername +textcolour+ ""  # yourself gets renamed to player name
        ENEMIES[playername.lower()] = ENEMIES['yourself']  # puts in new value in the dictionary
        del ENEMIES['yourself']  # deletes old value
        #ENEMIES.update({PLAYER.name.lower():ENEMIES['yourself']}) # adds that new entity to the dictionary


        ENEMIES['your dad'].name = playername + "'s dad"  # yourself gets renamed to player name
        ENEMIES['your dad'].colouredname = "" +personcolour+ playername + "'s dad" +textcolour+ "" # yourself gets renamed to player name
        ENEMIES[playername.lower() + "'s dad"] = ENEMIES['your dad']  # puts in new value in the dictionary
        del ENEMIES['your dad']  # deletes old value
        #ENEMIES.update({PLAYER.name.lower():ENEMIES['yourself']}) # adds that new entity to the dictionary

        ENEMIES[playername.lower()].location = (2, 4, 1, 0)
        MAPS[2][4][1][0].placeEnemy(ENEMIES[playername.lower()])  # then placed on the map
        ENEMIES[playername.lower() + "'s dad"].location = (5, 7, 1, 0)
        MAPS[5][7][1][0].placeEnemy(ENEMIES[playername.lower() + "'s dad"])  # then placed on the map

        #TODO problem is that allkeys are not updated for spellchecking

    except:  # If yourself is already set in the game
        pass

    # these HAVE TO be returned or else the changes are within the scope of the function only
    return ENEMIES, MAPS

def SpellCheck(Word,Psblties): #Spellchecks words in the background to check things closest
    Distance = [edit_distance(Word,key) for key in Psblties]
    index = Distance.index(min(Distance))
    return Psblties[index]

def DisplayTime(value): # converts and displays the time given seconds, for speedrunning
    '''From seconds to Days;Hours:Minutes;Seconds;Milliseconds'''
    # Figured out there is an effecient way to do this using time module but whatev.
    valueD = (((value/24)/60)/60)
    Days = int (valueD)
    valueH = (value-Days*24*3600)
    Hours = int(valueH/3600)
    valueM = (valueH - Hours*3600)
    Minutes = int(valueM/60)
    valueS = (valueM - Minutes*60)
    Seconds = int(valueS)
    valueMS = (valueM - Seconds)
    Milliseconds = valueMS*1000
    printT("Your run-time was: (\S)"+ str(Days) + " Days; " + str(Hours)+ " Hours; " + str(Minutes) + " Minutes; " + str(Seconds) + " Seconds; " + str(Milliseconds) + " Milliseconds")

# this Save and Load is written in GameFunctions (instead of GameClasses where it should be) due to import order and undefined of global variables

def save_game(savename):
    # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    global GAMESETTINGS # The game settings that are saved in the game
    # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # If not assignment within the function  may lead to changes only in the local scope

    # this saves current state to csv file, disabled by default for releasing exe
    # TODO Make these files into the loading with encryption
    # TODO Turn off CSV saves before compiling
    #CSVSaves.entities_to_CSV(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS)

    logGame(GAMEINFO['log'])  # logs the data to be submitted

    # Data dictionary for saving
    DATA = {"PLAYER": PLAYER, "ITEMS": ITEMS, "MAPS": MAPS,"INTERACT":INTERACT,"QUESTS":QUESTS,"ENEMIES":ENEMIES,"GAMEINFO":GAMEINFO,"GAMESETTINGS":GAMESETTINGS}

    savegamepath = GAMEINFO['savepath'] + "SaveFile " + savename + ".plp"

    pickle_game(DATA,savegamepath)  # this actually pickles the data to save it


    return


def load_game(loadname):
    # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    global PLAYER #The main character. player is an object instance of class character.
    global ITEMS #All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global MAPS #All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    global INTERACT #All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global QUESTS #Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    global ENEMIES #All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    global GAMEINFO #Miscellaneous game info. Dictionary of all sorts of variables
    global GAMESETTINGS # The game settings that are saved in the game
    # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # If not assignment within the function  may lead to changes only in the local scope

    x,y,z,dim = PLAYER.location

    loadgamepath = GAMEINFO['savepath'] + "SaveFile " + loadname + ".plp"

    DATA = unpickle_game(loadgamepath)  # this unpickles the game to get the data dictionary

    # Overwritting the current dictionaries
    MAPS = DATA["MAPS"]  # MAPS loads first because least likely to have changed
    PLAYER = DATA["PLAYER"]
    ITEMS = DATA["ITEMS"]
    INTERACT = DATA["INTERACT"]
    QUESTS = DATA["QUESTS"]
    ENEMIES = DATA["ENEMIES"]
    GAMEINFO = DATA["GAMEINFO"]
    GAMESETTINGS = DATA["GAMESETTINGS"]

    GAMEINFO['timestart'] = time.time()  # reset instance start time

    x,y,z,dim = PLAYER.location
    MAPS[x][y][z][dim].search(MAPS,DIMENSIONS,GAMESETTINGS,True)

    # HAVE TO HAVE THESE RETURN INTO THE SCOPE. I HATE GLOBAL VARIABLES ONLY USE PASS BY VALUE EVER
    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


###this function definitions were added for the compiler so they don't have to be referenced
def _edit_dist_init(len1, len2):
    lev = []
    for i in range(len1):
        lev.append([0] * len2)  # initialize 2D array to zero
    for i in range(len1):
        lev[i][0] = i           # column 0: 0,1,2,3,4,...
    for j in range(len2):
        lev[0][j] = j           # row 0: 0,1,2,3,4,...
    return lev


def _edit_dist_step(lev, i, j, s1, s2, substitution_cost=1, transpositions=False):
    c1 = s1[i - 1]
    c2 = s2[j - 1]

    # skipping a character in s1
    a = lev[i - 1][j] + 1
    # skipping a character in s2
    b = lev[i][j - 1] + 1
    # substitution
    c = lev[i - 1][j - 1] + (substitution_cost if c1 != c2 else 0)

    # transposition
    d = c + 1  # never picked by default
    if transpositions and i > 1 and j > 1:
        if s1[i - 2] == c2 and s2[j - 2] == c1:
            d = lev[i - 2][j - 2] + 1

    # pick the cheapest
    lev[i][j] = min(a, b, c, d)


def edit_distance(s1, s2, substitution_cost=1, transpositions=False):
    """
    Calculate the Levenshtein edit-distance between two strings.
    The edit distance is the number of characters that need to be
    substituted, inserted, or deleted, to transform s1 into s2.  For
    example, transforming "rain" to "shine" requires three steps,
    consisting of two substitutions and one insertion:
    "rain" -> "sain" -> "shin" -> "shine".  These operations could have
    been done in other orders, but at least three steps are needed.

    Allows specifying the cost of substitution edits (e.g., "a" -> "b"),
    because sometimes it makes sense to assign greater penalties to substitutions.

    This also optionally allows transposition edits (e.g., "ab" -> "ba"),
    though this is disabled by default.

    :param s1, s2: The strings to be analysed
    :param transpositions: Whether to allow transposition edits
    :type s1: str
    :type s2: str
    :type substitution_cost: int
    :type transpositions: bool
    :rtype int
    """
    # set up a 2-D array
    len1 = len(s1)
    len2 = len(s2)
    lev = _edit_dist_init(len1 + 1, len2 + 1)

    # iterate over the array
    for i in range(len1):
        for j in range(len2):
            _edit_dist_step(lev, i + 1, j + 1, s1, s2,
                            substitution_cost=substitution_cost, transpositions=transpositions)
    return lev[len1][len2]
################this is the start of the file

