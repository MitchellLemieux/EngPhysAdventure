# ENG PHYS TEXT  ADVENTURE
# Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
# First written on Mar  21,2019 by Brendan Fallon:
"""
This Quests.py file is used to write the story, quests, and events of the game by changing objects based on conditions.
EngPhysStory() is the main Eng Phys storyline  and returns once its finished
Quests generally only happen once and are sidequests unrelated to the storyline that do something special
Events are reoccurring based on the condition for the game.
    This also includes PORTALS which is teliportation using interacts
"""


from GameFunctions import *  # importing the global dictionaries/values
import time
import Opening  # used for the EPTA all the way down quest
import os  # used to put files in the cache folder
import AsciiArt
from Colour import *

global QUESTS

# List of quests and storylines that then get's built into a dictionary
# This dictionary is just flags to keep track of quest completion to advance or end quests
# it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
    # sidequests
    'secret spaces',
    'rules sign',
    'EPTA all the way down',
    'national treasure',
    'open the trees',
    'open the cabin',
    'open the forest',
    'power of the forest',
    # Events
    'completionist',
    'PAP',
    # Talk to hooded man
    "talk to devan",
    "talk to mysterious man",
    # Nuke
    "preston get dumbbell",
    "buijs kill chris",
    "dan fix reactor",
    "novog get donut",
    "feynman mirror",
    # Optics
    "kitai get silicon substrate",
    "knights get book",
    "haugen kill soleymani",
    "einstein fridge",
    # Semiconductor
    "lapierre get coffee",
    "kleimann get solar cell",
    "minnick get oscilloscope",
    "get key to display case",
    "maxwell portal",
    # endgame stuff
    'end game start',
    'the dark lord',
    'university man',
    'restored order',
    'create chaos',
    'neutral balance'
    # PHILpocalypse  # After you give Phil is braces he sobers up and becomes tired Phil.
    # After he asks for a coffee "Man I could really use a coffee but I don't want to spend the money
    # if you give him coffee he gives you a free wish "OH YEAH I AM CAFFINATED. I feel like I can do anyhing!"
    # If you give him a cappuccino the PHILpocalypse storyline begins:
    # You see his eyes dilate "OH YEAH I"M FEELING GREAT", He snaps his fingers and there's a flash.
    # You wake in JHE field "Not again" and everyone on the map is gone. Eventually you meet a Phil clone
]

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest: 1})


def sidequests(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope


    # --- Side Quests ---
    # -- Secret Spaces --
    if INTERACT['coat of arms'].quest and QUESTS["secret spaces"]:  # Unlocks the secret space once you get the scroll
        MAPS[0][2][1][0].removeWall("d")  # DON'T FORGET to make wall a list instead of a tuple in the object!
        QUESTS["secret spaces"] = 0

    # -- Rules Sign --
    if INTERACT["rules sign"].quest and QUESTS['rules sign']:  # Once the sign is read
        MAPS[2][3][1][0].removeInteract(INTERACT["rules sign"])
        INTERACT["rules sign"].location = (None,None,None,None)
        printT( "The sign " +indicatecolour+ "disappears" +textcolour+ " in a flash of " +indicatecolour+ "smoke" +textcolour+ ". You look around. Are you still dreaming?")
        QUESTS["rules sign"] = 0

    # -- EBTA All the way Down --
    # when you put the pen in the laptop it opens the thing
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']:
        # TODO as homework see if there's a way to do this with recursion instead of simulating it
        # Would put drums if there was sound effect
        playgame = input('========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame == "y":
            printT("You click on the game and it begins in the terminal. The " +red+ "drumming intensifies" +textcolour+ ". You're not sure if you made the right choice.")
            printT("======================================================================== (\S) (\S)")
            import CreativeMode  # this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler)
            QUESTS['EPTA all the way down'] = 0  # Truns off the quest, has to be before the game saves so the quest is ended when you come back
            save_game(str(GAMEINFO['layersdeep']))  # saving game to be reloaded after death or won the game
            log = GAMEINFO['log']  # keeps the log as a temporary variable to keep a running log in the nested game
            Opening.Opening()
            newplayername = input("First, what is your name?\n")
            layers = GAMEINFO['layersdeep']  # saves layersdeep to a temporary variable for after the load
            MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS = load_game("basegame")  # should display the exact start
            GAMEINFO['layersdeep'] = layers + 1   # increments the global layers deep because you're now in a lower level, using the memory of the local variable

            GAMEINFO['playername'] = PLAYER.name = newplayername  # this is done for the log
            GAMEINFO['gamestart'] = time.time()  # Settign the game and timestart for for this layer
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            # Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame), "--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],
                                     GAMEINFO['playername'], time.ctime(GAMEINFO['timestart']),
                                     "--LOG START--"]  # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame == "n":
            printT("You " +indicatecolour+ "decide against it" +textcolour+ ", fearing the worst. You safely edject the pen, drop it on the floor, and " +red+ "smash" +textcolour+ " it to pieces. Better safe than sorry. (\S)" +lightblue+ "The drumming stops" +textcolour+ ".)")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log
        else:
            printT("" +losecolour+ "It was a yes or no question" +textcolour+ ". When you look back the files are " +losecolour+ "gone" +textcolour+ ". (\S)Even the FlexPDE code. Good riddance.")
            printT("========================================================================")
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log

    #National Treasure
    if INTERACT["tri-coloured glasses"].quest and QUESTS['national treasure']:  # Once the sign is read
        MAPS[1][0][1][0].removeWall("u")  # DON'T FORGET to make wall a list instead of a tuple in the object!
        QUESTS["national treasure"] = 0

    if INTERACT["red book"].quest and QUESTS['open the trees']:  # Once the sign is read
        printT("You feel like you've " +indicatecolour+ "gained" +textcolour+ " some knowledge!")
        MAPS[3][7][1][0].removeInteract(INTERACT['gap in the trees'])
        INTERACT['gap in the trees'].location = (None, None, None, None)
        INTERACT['gap in the trees'].location = None
        MAPS[3][7][1][0].placeInteract(INTERACT['opening in the trees'])
        INTERACT['opening in the trees'].location = (3,7,1,0)
        QUESTS['open the trees'] = 0
        #return INTERACT,MAPS  # don't need to return this scope because reasons?


    if INTERACT["lit firepit"].quest and QUESTS['open the cabin']:
        MAPS[8][9][0][4].removeWall("r")  # DON'T FORGET to make wall a list instead of a tuple in the object!
        QUESTS['open the cabin'] = 0

    if INTERACT['gate of the forest'].quest and QUESTS['open the forest']:
        MAPS[0][7][0][4].removeWall("b")  # DON'T FORGET to make wall a list instead of a tuple in the object!
        QUESTS['open the forest'] = 0

    if INTERACT['stone pedestal'].quest and QUESTS['power of the forest']:
        PLAYER.maxhealth = 200
        PLAYER.health = 200
        PLAYER.basestats = [100,100,100]
        PLAYER.updateStats()
        printT(" (\S) (\S)You see a " +indicatecolour+ "flash of light" +textcolour+ " and " +wincolour+ "feel stronger" +textcolour+ ".")
        AsciiArt.HauntedForest()
        QUESTS['power of the forest'] = 0

    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS



def ebta_story(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # Talk to devan
    if ENEMIES["devan the most unhelpful"].spoke and QUESTS["talk to devan"]:
        MAPS[1][3][1][0].removeEnemy(ENEMIES["devan the most unhelpful"])  # removes him from infront of hatch
        ENEMIES["devan the most unhelpful"].location = (2,4,0,0)
        MAPS[2][4][0][0].placeEnemy(ENEMIES["devan the most unhelpful"])
        ENEMIES["devan the most unhelpful"].info = "We can talk in here. I've heard about you seeking your " +itemcolour+ "iron ring" +textcolour+ ". Turns out this thing goes deeper than I could have imagined, way deeper. It seems last night you got really drunk at the " +mapcolour+ "Phoenix" +textcolour+ " and did something to piss off somebody very bad. I'd say if you're trying to get your ring, you should start there."
        ENEMIES["devan the most unhelpful"].spoke = False
        QUESTS["talk to devan"] = 0


    # Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1][0].placeEnemy(ENEMIES["dr. kitai"])
        MAPS[2][4][2][0].placeEnemy(ENEMIES["dr. preston"])
        MAPS[1][6][2][0].placeEnemy(ENEMIES["dr. lapierre"])
        MAPS[5][4][1][0].removeEnemy(ENEMIES["hooded man"])
        ENEMIES["hooded man"].location = (None, None, None, None)  # the location should be set to none but for some reason it's fine
        ENEMIES['hooded man'].spoke = False
        QUESTS["talk to mysterious man"] = 0

    # Nuke quests
    if ENEMIES['dr. preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1][0].placeEnemy(ENEMIES["dr. buijs"])
        QUESTS["preston get dumbbell"] = 0

    if ENEMIES['dr. buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0][0].placeEnemy(ENEMIES['dan fitzgreen'])
        ENEMIES['dan fitzgreen'].quest = True
        QUESTS['buijs kill chris'] = 0

    if INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        MAPS[2][6][0][0].placeEnemy(ENEMIES['dr. novog'])
        MAPS[4][5][0][0].placeEnemy(ENEMIES['stefan boltzmann'])
        QUESTS["dan fix reactor"] = 0

    if ENEMIES['dr. novog'].quest and QUESTS["novog get donut"]:
        QUESTS['novog get donut'] = 0

    if INTERACT['ancient mirror'].quest and QUESTS["feynman mirror"]:
        QUESTS["feynman mirror"] = 0

    # Optics quests
    if ENEMIES['dr. lapierre'].quest and QUESTS["lapierre get coffee"]:
        MAPS[5][4][1][0].placeEnemy(ENEMIES['dr. knights'])
        QUESTS["lapierre get coffee"] = 0

    if ENEMIES['dr. knights'].quest and QUESTS["knights get book"] and ITEMS["3w textbook"].location == (3,4,0,0):
        MAPS[1][6][0][0].placeEnemy(ENEMIES['dr. haugen'])
        QUESTS["knights get book"] = 0

    if ENEMIES['dr. haugen'].quest and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        ENEMIES['dr. haugen'].alive = False
        MAPS[1][6][0][0].removeEnemy(ENEMIES['dr. haugen'])
        ENEMIES['dr. haugen'].location = (None, None, None, None)
        MAPS[1][6][0][0].placeItem(ITEMS["haugen's clothes"])

    if INTERACT['fridge'].quest and QUESTS['einstein fridge']:
        QUESTS['einstein fridge'] = 0

    # Semiconductor quests
    if ENEMIES['dr. kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2][0].placeEnemy(ENEMIES['dr. kleimann'])
        QUESTS['kitai get silicon substrate'] = 0

    if ENEMIES['dr. kleimann'].quest and QUESTS["kleimann get solar cell"]:
        MAPS[3][4][1][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["kleimann get solar cell"] = 0

    # Minnick's Glasses activate the need quest in all further items. So quest is driven by interacts from here
    if ENEMIES['dr. minnick'].quest and QUESTS["minnick get oscilloscope"]:
        MAPS[6][1][1][0].removeWall("d")  # DON'T FORGET to make wall a list instead of a tuple in the object!
        ENEMIES['dr. minnick'].quest = False
        ENEMIES['dr. minnick'].drop = 'gauss eye'  # this has to be lowercase or it throws a key error - All items are defined as lower case when stored
        ENEMIES['dr. minnick'].need = "faraday's cage"  # this has to be lowercase or it throws a key error
        ENEMIES['dr. minnick'].info = "I need to complete " + deadpersoncolour+"Kenrick's"+textcolour+" design... use my "+itemcolour+"glasses "+textcolour+"to find what we need!"
        ENEMIES['dr. minnick'].Sinfo = "'" +indicatecolour+ "Great" +textcolour+ "! Now we can open the window to the " +mapcolour+ "electronics world" +textcolour+ "!'\nYou step back and watch as " +personcolour+ "Dr. Minnick" +textcolour+ " adds " +itemcolour+"Faraday's Cage "+textcolour+"to the " +itemcolour+ "oscilloscope" +textcolour+ ".\n'I do not know what this " +personcolour+ "oracle" +textcolour+ " will have to say.'\n'It is just my responsibility to give you access to their knowledge.'\nYour vision begins to go blurry as you hear a low whirr grow louder and " +itemcolour+ "Kenrick's oscilloscope" +red+ " glows" +textcolour+ " with\nconsiderable intensity!\nYou are shocked as you open your eyes. It seems as if you were dropped into the set of 'Tron'.\nA figure approaches as your vision slowly returns.\nThe figure is revealed to be " +personcolour+ "James Clerk Maxwell" +textcolour+ "!\n'We have waited many years for your coming.'\n'You will be the one to determine the fate of this faculty.'\n'My "+wincolour+"quantum relic "+textcolour+"along with the two others will give you the power to have your " +itemcolour+ "ring" +textcolour+ " returned to you.'\n'"+indicatecolour+"Once you have all three you" +textcolour+ " will be able to access your " +itemcolour+ "ring" +textcolour+ " from the "+mapcolour+"statue of McMaster."+textcolour+"'\n'Good luck.'"
        MAPS[3][4][1][0].removeEnemy(ENEMIES['dr. minnick'])
        ENEMIES['dr. minnick'].location = (None, None, None, None)
        MAPS[1][7][0][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["minnick get oscilloscope"] = 0

    if INTERACT['display case'] and QUESTS["get key to display case"]:
        QUESTS["get key to display case"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["maxwell portal"]:
        QUESTS['maxwell portal'] = 0

    # endgame

    if QUESTS['end game start'] and not (QUESTS["maxwell portal"] or QUESTS['einstein fridge'] or QUESTS["feynman mirror"]):
        MAPS[5][2][1][0].placeEnemy(ENEMIES['hooded man'])
        printT(" (\S)You feel a strange " +indicatecolour+ "pull" +textcolour+ " towards the " +mapcolour+ "McMaster Statue" +textcolour+ ". (\S)")
        MAPS[5][2][1][0].lore = "You approach the " +interactcolour+ "statue" +textcolour+ " and notice the mysterious "+personcolour+"Hooded Man "+textcolour+"beneath the tree.\nHe notices you approach and stops the incantation he was reciting.\nHe motions for you to come closer to speak."
        MAPS[5][2][1][0].travelled = 1
        ENEMIES['hooded man'].info = "'I knew you could do it.'\n'I knew you were the one the prophecy spoke of.'\n'For too long the " +indicatecolour+ "Quantum Order" +textcolour+ " has kept me in isolation...'\n'They thought I was poisoning the minds of students and did not agree\nwith my methods.'\n'But now you have brought the "+wincolour+"Quantum Relics "+textcolour+"which will give me the power\nto shape the faculty as I see fit!'\nThe " +personcolour+ "Hooded Man" +textcolour+ " pulls back his hood to reveal the familiar face you only recall from legend!\nIt is "+personcolour+"Dr. Cassidy himself"+textcolour+"!"
        QUESTS['end game start'] = 0

    if not QUESTS['end game start'] and ENEMIES['hooded man'].spoke and QUESTS['the dark lord']:
        MAPS[5][2][1][0].removeEnemy(ENEMIES['hooded man'])
        ENEMIES['hooded man'].location = (None, None, None, None)
        MAPS[5][2][1][0].placeEnemy(ENEMIES['dr. cassidy'])
        QUESTS['the dark lord'] = 0

    if ENEMIES['dr. cassidy'].spoke and QUESTS['university man']:
        MAPS[5][2][1][0].placeEnemy(ENEMIES['sir william mcmaster'])
        ENEMIES['dr. cassidy'].info = "Destroy "+personcolour+"Sir William McMaster "+textcolour+"and we can rule this university together!"
        QUESTS['university man'] = 0

    if not ENEMIES['dr. cassidy'].alive and not ENEMIES['sir william mcmaster'].alive and QUESTS['neutral balance']:  # Neutral Ending, kill both
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 3
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    # # Brian did this
    # booty = 1
    # bitches = 6*9 + 6 + 9
    # big = booty*bitches
    # print str(big)

    if not ENEMIES['sir william mcmaster'].alive and QUESTS['create chaos']:
        ENEMIES['dr. cassidy'].Dinfo = "NO WAIT? WHY? "+personcolour+"Dr. Cassidy "+textcolour+"falls, slain beside "+personcolour+"Sir William McMaster "+textcolour+". (\S)You see the "+wincolour+"Deed to McMaster"+textcolour+"drop from his pocket."
        ENEMIES['dr. cassidy'].drop = None
        ENEMIES['dr. cassidy'].info = "Take the power you hold in your " +itemcolour+ "Iron Ring" +textcolour+ " and destroy the rest of the " \
                                      "" +indicatecolour+ "Quantum Order" +textcolour+ "! (\S)This includes "+personcolour+"Dr. Minnick, "+personcolour+"Dr. Novog"+textcolour+", "+personcolour+"Dr. Kitai"+textcolour+", "+personcolour+"Dr. knights"+textcolour+", " \
                                      ""+personcolour+"Dr. Preston"+textcolour+", "+personcolour+"Dr. Kleimann"+textcolour+", "+personcolour+"Dr. Buijs"+textcolour+", "+personcolour+"Dr. Lapierre"+textcolour+", and "+personcolour+"Dr. Nagasaki"+textcolour+"."
        DEATHS = [ENEMIES[i].alive for i in
                  ['dr. minnick', 'dr. novog', 'dr. kitai', 'dr. knights', 'dr. preston', 'dr. kleimann', 'dr. buijs',
                   'dr. lapierre', 'dr. nagasaki']]
        if True in DEATHS:
            pass
        else:
            PLAYER.alive = False
            GAMEINFO['winner'] = 1
            return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS  # Dark ending, kill McMaster and all Quantum Order

    elif not ENEMIES['dr. cassidy'].alive and QUESTS['restored order']:  # Light Ending, kill Cassidy
        ENEMIES['sir william mcmaster'].Dinfo = "NO WAIT? WHY? "+personcolour+"Sir William McMaster "+textcolour+" falls, slain beside "+personcolour+"Dr. Cassidy "+textcolour+". (\S)You see the "+wincolour+"Deed to McMaster"+textcolour+" drop from his pocket."
        ENEMIES['sir william mcmaster'].drop = None
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 2
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


    if not ENEMIES['hooded man'].alive:  # say if you kill the hooded man, say bit hits him, the game ends
        PLAYER.alive = False  # does this so you can get out of the main loop
        GAMEINFO['winner'] = 2
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS

    else:
        if not GAMEINFO['winner']: GAMEINFO['winner'] = 0
        return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS


# If Events list gets to long can make it its own file
def events(MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS):
    # # These are all the global dictionaries/objects in the game. Anywhere where a loadgame happens you need all the global variables
    # global PLAYER  # The main character. player is an object instance of class character.
    # global ITEMS  # All the items. This a dictionary of objects of class equipment keyed by their lowcase equipment name (item.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global MAPS  # All the locations. A tuple of objects of class Map inxed by there x,y,z coordinate (MAPS[x][y][z])
    # global INTERACT  # All the interactables (stationary things that need something). This a dictionary of objects of class Interact keyed by their lowcase name (interact.name). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global QUESTS  # Quest statuses. This is a dictionary of flags (1 or 0) for the status of the quest keyed by quest name.
    # global ENEMIES  # All the npcs. This a dictionary of objects of class Enemy keyed by their lowcase equipment name (item.name.lower()). Remember the lowercase, may trip you up if referencing upercase version in the file.
    # global GAMEINFO  # Miscellaneous game info. Dictionary of all sorts of variables
    # global GAMESETTINGS  # The game settings that are saved in the game
    # # global keyword makes the variables inside the function reference the correct global scope variable when assigned in the function.
    # # If not assignment within the function  may lead to changes only in the local scope

    # PAP Event
    # TODO Make time not GMT so it doesn't matter which time zone you're in
    #TODO Make sure this isn't set so it's not always 420
    #insttime = time.gmtime(time.time() - 4 * 60 * 60)  # Used to debug and test the time based events by adding timer
    # print time.asctime(insttime)  # Prints out the ascci time to debug (Also nice to see but breaks immersion)
    if QUESTS['completionist']:
        insttime = time.localtime()  # Instantaneous struct_time object at the time of reading if you haven't beaten everything
    else:
        insttime = time.gmtime(1562765901.005 + 24240 - 141 - (4 * 60 * 60))  # Sets time to constantly 4:20pm time object
    #print insttime  # for debugging time
    # Thunder, cowboys, Bell, PAP sound

    # Simulated times to trigger the event, based on seconds from Epoch

    # gmtenthirty = gmfourtwenty + 6 * 60 * 60 + 10 * 60  # 10:30pm
    # insttime = time.gmtime(gmtenthirty)     # 10:30pm time object
    # TODO Make it so if you Do all intractables + (even empty ones) + Quests after winning the game you unlock PAP
    # if INTERACT['red book'].quest == True:
    #     gmfourtwenty = 1562765901.005 + 24240 - 141 - (4 * 60 * 60)  # 4:20pm, Subtracting the 4 hours for gm time
    #     insttime = time.gmtime(gmfourtwenty)  # 4:20pm time object
    # if INTERACT['blue book'].quest == True:
    #     insttime = time.localtime()  # Instantaneous struct_time object at the time of reading

    #LINEBREAK = "========================================================================"  # standard display with 72 characters
    LINEBREAK = "=======================The=Eng=Phys=Text=Adventure=======================" #standard display with 72 characters

    #print GAMEINFO['winner']
    if GAMEINFO['winner'] and QUESTS['completionist']:
        enemycompletion = [ENEMIES[i].quest for i in
                      ['rod the bowler', 'brian the weeb', 'erik the sk8r', 'brendan fallon', 'liam the gamer',
                       'steven the first-year', 'paul the janitor','phil the drunk', 'zack the snack','connor the biologist']]
        interactcompletion = [INTERACT[i].quest for i in
                      ['garbage can', 'rca tv', 'sharpxchange', 'rules sign', 'lenovo laptop', 'coat of arms',
                       'mouse','gate of the forest']]

        # print "status " + str(GAMEINFO['winner'])
        # enemycompletion = [ENEMIES[i].quest for i in ['erik the sk8r']]
        # interactcompletion = [INTERACT[i].quest for i in
        #               ['garbage can']]

        if (False in enemycompletion) or (False in interactcompletion):
            #print enemycompletion
            #print interactcompletion
            pass
        else:
            input("\n" +wincolour+ "YOU DID IT!!!! YOU 100% THE GAME! Type anything to continue:" +textcolour+ "")
            AsciiArt.Acheivement()
            GAMEINFO['log'].append("---THEY 100% the game!---")  # appends they won at the end of the log file to make it easier find
            save_game(GAMEINFO['playername'] + " 100 Percent")  # saves all data to later be submited, different from the main save file
            gmfourtwenty = 1562765901.005 + 24240 - 141 - (4 * 60 * 60)  # 4:20pm, Subtracting the 4 hours for gm time
            insttime = time.gmtime(gmfourtwenty)  # Sets time to constantly 4:20pm time object
            QUESTS['completionist'] = 0

    # Setting up the Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if (insttime.tm_hour == 4 or insttime.tm_hour == 16) and insttime.tm_min == 20 and QUESTS["PAP"]:
        QUESTS["PAP"] = 0
        # Signaling Event, depends whether you're inside or outside
        print("A Bolt of lightening strikes the top of JHE")
        # TODO make this an interior after so you decide to go in
        MAPS[2][4][3][0].info = "~?~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "As you reach the top of the stairs you can feel the " +red+ "heat" +textcolour+ " intensify. " \
                                "Where the way was blocked before is a " +red+ "melted hole" +textcolour+ " just big enough for you to fit through. You expect to enter the " \
                                "hallway but see all the interior walls have been removed. All that remains are stone walls and boarded up windows. " \
                                "Textbooks and broken lab equipment litter the ground. You turn the corner to the lecture hall where you would " \
                                "fall asleep in the 8:30 1D04 lecture. Glowing red hot in the centre of the room is the " +interactcolour+ "Pack-a-Punch Machine" +textcolour+ "! " \
                                "(\S) (\S) Enscribed on the side in graffiti is 'BLAZE IT'."
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].placeInteract(INTERACT["pack-a-punch"])
    # Event Main Activity "Pack-a-Punching" when you inspect the machine
    elif (PLAYER.location == list(INTERACT["pack-a-punch"].location)) and INTERACT["pack-a-punch"].quest:
        PAPScreen = True
        upgradechoice = 0
        sacrificechoice = 0
        while PAPScreen:
            print(LINEBREAK)
            # AsciiArt.PackScreen() # TODO Enable once Dynamic Ascii Art
            # Displaying Options
            if upgradechoice == 0:
                print("Item 1: Choose an " +itemcolour+ "Item" +textcolour+ " to " +wincolour+ "Upgrade" +textcolour+ "")
            else:
                print("Item 2: Choose an " +textcolour+ "Item" +textcolour+ " to " +losecolour+ "Sacrifice" +textcolour+ "")
            k = 0
            for i in PLAYER.inv:
                if PLAYER.inv[i].name == EMPTYINV[i].name:  # skips empty items
                    # print "THIS B**** EMPTY - YEET"
                    continue  # advance to the next i

                k += 1
                if (k != int(upgradechoice)):
                    print("[" + str(k) + "]" + PLAYER.inv[i].name + " " + str(PLAYER.inv[i].stats))
            print("[" + str(k + 1) + "]Back\n")
            # Input and Check Input
            try:
                if upgradechoice == 0:
                    upgradechoice = eval(input("Choose the number of the " +itemcolour+ "item" +textcolour+ " you want to " +interactcolour+ "Pack-a-Punch" +textcolour+ ": "))
                    if upgradechoice <= 0 or upgradechoice > k + 1:
                        print("" +losecolour+ "Please enter a valid option!" +textcolour+ "")
                        upgradechoice = 0
                else:
                    sacrificechoice = eval(input("Choose the number of the " +itemcolour+ "item" +textcolour+ " you want to " +losecolour+ "sacrifice" +textcolour+ ": "))
                    if sacrificechoice <= 0 or sacrificechoice > k + 1:
                        print("Please enter a valid option!")
                        sacrificechoice = 0
                    elif upgradechoice == sacrificechoice:
                        print("" +losecolour+ "Please enter a valid option!" +textcolour+ "")
                        sacrificechoice = 0

            except:
                print("" +losecolour+ "Please input a number selection!" +textcolour+ "")

            # Back Options Options
            if upgradechoice == k + 1:  # if you choose back on upgrade choice screen the loop exits
                PAPScreen = False  # Break the loop to exit it
            elif sacrificechoice == k + 1:  # if you choice back on sacrifice screen it resets to screen 1
                upgradechoice = 0
                sacrificechoice = 0

            # PAP Operation
            if (0 < upgradechoice < k + 1) and (0 < sacrificechoice < k + 1):
                PAPScreen = False

                # Getting the item objects
                k = 0
                for i in PLAYER.inv:
                    if PLAYER.inv[i].name == EMPTYINV[i].name:  # skips empty items
                        # print "THIS B**** EMPTY - YEET"
                        continue  # advance to the next i
                    k += 1
                    if k == upgradechoice:
                        upgrade = PLAYER.inv[i]  # copying the object to a temp variable
                    elif k == sacrificechoice:
                        sacrifice = PLAYER.inv[i]  # copying object to a temp variable

                if input("Upgrading: " + upgrade.colouredname + "\nSacrificing: " + sacrifice.colouredname + "\n\nThis cannot be undone. \nType Y if this is correct:").lower() in ["y", 'yes', '1']:
                    pass  # if they're sure they want to do something go foward
# The pass statement in Python is used when a statement is required syntactically but you do not want code to execute.
                else:  # goes back to the loop and start again
                    break
                    upgradechoice = 0
                    sacrificechoice = 0
                # Dropping the items
                PLAYER.drop(upgrade)  # Item is removed from the player inventory
                PLAYER.drop(sacrifice)  # Item is removed from the player inventory
                #del ITEMS[upgrade.name.lower()]  # deleting from the items dictionary so isn't around
                #del ITEMS[sacrifice.name.lower()]  # deleting from the items dictionary so isn't around

                # Upgrading the one item based on the sacrifice
                printT("The Machine Reads: " +wincolour+ "'Pack-a-Punching" +indicatecolour+ " Please Wait" +textcolour+ "'")
                upgrade.colouredname = "" +wincolour+"Better " +itemcolour+ upgrade.name +textcolour+""  # Adding Better to left side of name each time it's upgraded
                upgrade.name = "Better " + upgrade.name  # Adding Better to left side of name each time it's upgraded
                sumUStats = upgrade.stats[0] + upgrade.stats[1] + upgrade.stats[2]  # taking the sum of the stats of each item
                sumSStats = sacrifice.stats[0] + sacrifice.stats[1] + sacrifice.stats[2]
                # Sum of item stats of sacrifice has to be 1/10th that of the PAP item to double or add (whichever is better), or else they just add
                if sumUStats / 10 <= sumSStats:
                    # Doubling stats of the item
                    if sumUStats + sumSStats > sumUStats * 2:
                        upgrade.stats = (upgrade.stats[0] + sacrifice.stats[0], upgrade.stats[1] + sacrifice.stats[1],
                                         upgrade.stats[2] + sacrifice.stats[2])  # replacing stats tuple with sum
                    else:
                        upgrade.stats = (upgrade.stats[0] * 2, upgrade.stats[1] * 2,
                                         upgrade.stats[2] * 2)  # replacing stats tuple with doubling them
                else:
                    # Adding the Stats
                    upgrade.stats = (upgrade.stats[0] + sacrifice.stats[0], upgrade.stats[1] + sacrifice.stats[1],
                                     upgrade.stats[2] + sacrifice.stats[2])  # replacing stats tuple


                upgrade.location = (2,4,3,0)
                ITEMS[upgrade.name.lower()] = upgrade  # writing it to the ITEMS dictionary
                MAPS[2][4][3][0].placeItem(upgrade)  # Placing the Upgraded Item on the ground

                # TODO problem is that allkeys are not updated for spellchecking

                printT("The "+interactcolour+"Pack-a-Punch "+textcolour+"wirls and screaches, glowing bright, before spitting out the " + upgrade.colouredname + " onto the ground!")
                # TODO add pack-a-punch sound

        # Resetting quest flag so you don't always inspect it once you enter the room
        INTERACT["pack-a-punch"].quest = False



    # Resetting the Event
    elif (QUESTS["PAP"] == 0) and (not (PLAYER.location == (2, 4, 3, 0))) and (not (insttime.tm_min == 20)):
        QUESTS["PAP"] = 1

        #print "DONT BLAZE IT"
        MAPS[2][4][3][0].info = "~3RD FLOOR JHE Stairs~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "You see solid block of sheet metal covering the door. Was it " +indicatecolour+ "always" +textcolour+ " this way?"
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].removeInteract(INTERACT["pack-a-punch"])
        INTERACT["pack-a-punch"].location = (None, None, None, None)

    # TENThirty Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if (insttime.tm_hour == 10 or insttime.tm_hour == 22) and insttime.tm_min == 30:
        if not (PLAYER.inv['body'] == EMPTYBODY):  # If  your body isn't empty
            printT("" + wincolour+"10:30 "+textcolour+"NO SHIRTY")
            print("You feel compelled to take your "+itemcolour+"shirt "+losecolour+"off "+textcolour+"and drop it on the ground")
            # Drops the item you have on you, don't forget it has to be name of the item and lowercase.
            # Also can't be PLAYER.drop function because then it doesn't go onto the ground
            Drop(PLAYER.inv['body'].name.lower())

    # Killcount counter in player will trigger the police eventually


    # --- Portals ---
    # TODO Build in this portal fucntionality into INTERACTS or maybe just places with doors

    # To Green Lake
    if INTERACT["lake painting"].quest:
        PLAYER.location = [0,0,0,3]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[0][0][0][3]
        CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
        INTERACT["lake painting"].need = None
        printT("(\S)You no longer need the keys to get into this place.")
        INTERACT["lake painting"].quest = False

    # Back to Art Museum
    if INTERACT["portkey"].quest:
        PLAYER.location = [3,0,1,0]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[3][0][1][0]
        CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
        INTERACT["portkey"].quest = False


    # To Haunted forest from COOTES DRIVE

    if INTERACT['opening in the trees'].quest:
        PLAYER.location = [4,0,0,4]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[4][0][0][4]
        if CurrentPlace.travelled:
            printT("You enter... (\S)")
            AsciiArt.HauntedForest()
        CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
        INTERACT['opening in the trees'].quest = False

    # To COOTES DRIVE from Haunted Forest Start
    if INTERACT['trail to cootes drive'].quest:
        PLAYER.location = [3,7,1,0]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[3][7][1][0]
        CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
        INTERACT['trail to cootes drive'].quest = False

    # To COOTES DRIVE from escape rope
    if INTERACT['escape rope'].quest:
        PLAYER.location = [3,7,1,0]  # WHEN YOU TELIPORT IT HAS TO BE A LIST BECAUSE PLAYER LOCATION IS A LIST
        CurrentPlace = MAPS[3][7][1][0]
        CurrentPlace.search(MAPS, DIMENSIONS,GAMESETTINGS, True)
        INTERACT['escape rope'].quest = False


    return MAPS, PLAYER, ITEMS, INTERACT, QUESTS, ENEMIES, GAMEINFO, GAMESETTINGS