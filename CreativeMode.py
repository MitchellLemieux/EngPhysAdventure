#ENG PHYS TEXT  ADVENTURE
#Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
#Wrote on Dec  22,2018: 
import pickle
from GameFunctions import * #importing the global dictionaries/values
from StartUp import XRANGE, YRANGE, ZRANGE, DRANGE #Importing the map bound variables from StartUp to be used in the load function
import CSVSaves
from Colour import *

#Obsolete and moved to GameCLasses+Gamefuntions because pickling needs to be where custom classes are defined
# def saveGame(savename):
#     global PLAYER
#     global ITEMS
#     global MAPS
#     global ENEMIES
#     global INTERACT
#     global QUESTS
#     global GAMEINFO
#     global GAMESETTINGS
#
#     # this saves current state to csv file, disabled by default for releasing exe
#     # TODO Make these files into the loading with encryption
#     # TODO Turn off CSV saves before compiling
#     #CSVSaves.entities_to_CSV(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS)
#
#     f = open(GAMEINFO['savepath'] + "SaveFile " + savename + ".plp", "w+")  # Saved as .plp for obfuscation purposes
#     x = [PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS] # puts all info into a list to be saved
# ##    types in x
# ##    <type 'instance'>
# ##    <type 'dict'>
# ##    <type 'tuple'>
# ##    <type 'dict'>
# ##    <type 'dict'>
# ##    <type 'dict'>
# ##    <type 'dict'>
# ##    <type 'dict'>
#     pickle.dump(x, f) #pickles the list of gamedata to the save file
#     f.close()
#
#     return


# def loadGame(loadname):
#     global PLAYER
#     global ITEMS
#     global MAPS
#     global ENEMIES
#     global INTERACT
#     global QUESTS
#     global GAMEINFO
#     global GAMESETTINGS
#
#
#     try:
#         # f = open(GAMEINFO['savepath'] +"SaveFile "+loadname +".plp","r+")  # Saved as .plp for obfuscation purposes
#         # save = pickle.load(f)
#         # f.close()
#         # #seperates the list
#         # loadplayer = save[0]
#         # loaditems = save[1]
#         # loadmap = save[2]
#         # loadenemy = save[3]
#         # loadinter = save[4]
#         # loadquest = save[5]
#         # loadinfo = save[6]
#         # loadsettings = save[7]
#         #
#         #
#         # for info in GAMEINFO: #when itterating through list the itterating variable is the string of the key
#         #     GAMEINFO[info] = loadinfo[info]
#         # PLAYER.__dict__ = loadplayer.__dict__
#         # for item in ITEMS:
#         #     ITEMS[item].__dict__ = loaditems[item].__dict__ #assignment better when no subitems? .__dict for when there is
#         # for enemy in ENEMIES:  #.__dict__ removed on these and it works?
#         #     ENEMIES[enemy].__dict__ = loadenemy[enemy].__dict__
#         # for inter in INTERACT:
#         #     INTERACT[inter].__dict__ = loadinter[inter].__dict__
#         # for quest in QUESTS:
#         #     QUESTS[quest] = loadquest[quest]  # doesn't need .__dict___ for some reason
#         # for setting in GAMESETTINGS:
#         #     GAMESETTINGS[setting] = loadsettings[setting]  # doesn't need .__dict___ for some reason
#         # #for some reason putting MAPS load below these other ones fixed a bunch of bugs
#         # for x in range(XRANGE):
#         #     for y in range(YRANGE):
#         #         for z in range(ZRANGE):
#         #             for dim in range (DRANGE):
#         #                 if MAPS[x][y][z][dim]:  # There are different objects in 1 vs the other so need to replace object in each list with the new one of reference
#         #                     MAPS[x][y][z][dim].__dict__ = loadmap[x][y][z][dim].__dict__
#         #                     # Attempting to load in the map items to stop ghosting
#         #                     # MAPS[x][y][z][dim].items = loadmap[x][y][z][dim].items
#         #                     # MAPS[x][y][z][dim].ENEMY = loadmap[x][y][z][dim].ENEMY
#         #                     # MAPS[x][y][z][dim].walls = loadmap[x][y][z][dim].walls
#
#
#         GAMEINFO['commandcount'] += 1 #+1 command to load the game because it doesn't count the loadgame command
#         GAMEINFO['log'].append("loadgame") #adds the load game command to the log
#
#
#         #Displayes the current place info again to show it's been loaded
#         CurrentPlace = MAPS[PLAYER.location[0]][PLAYER.location[1]][PLAYER.location[2]][PLAYER.location[3]]
#         printT("========================================================================")
#
#         # searches and prints the information with spawn set to true to print "You wake up in"
#         CurrentPlace.search(MAPS, DIMENSIONS,True)
#
#         #YOU HAVE TO USE THIS DARN .__dict___ thing to copy the object atributes https://stackoverflow.com/questions/36243488/how-can-i-overwrite-an-object-in-python
#         #This is ineffecient but works. I think main problem I had is loading where the loaded objects are a new memory location but the game still references old locations
#         #It's best to reference things by name
#         #Acording to this lists make new functions: http://interactivepython.org/runestone/static/CS152f17/Lists/ObjectsandReferences.html
#         #use (a is b) to see if a and b refer to the same memory location
#         return PLAYER,ITEMS,MAPS,ENEMIES,INTERACT,QUESTS,GAMEINFO, GAMESETTINGS
#
#     except IOError:
#         print "There is no file named SaveFile " + loadname + ". Please try again."
#         return
#     except KeyError as E:
#         print E.args[0]
#         # TODO finish this for simple dictionary changes by using E.args[0] as the key to remove
#         printT("There is a mismatch between the objects in the game. You don't need to do anything but the game may not have loaded properly! We're sorry for any inconvenience.")
#         printT("At this time we can't update the file. Some things might be broken")
#         x, y, z, dim = PLAYER.location
#         MAPS[x][y][z][dim].search(MAPS, DIMENSIONS,True)
#
#         return PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS
#
#     except AttributeError:  # dictionary = key error (ITEMS, ENEMIES, INTERACTS, quest, gameinfo), atribute error = Map error or object attribute
#         if GAMEINFO['version'] > loadinfo['version']:
#             print "This is an old version of the game. At this time we don't have file updaters. Sorry!"
#         else:
#             print "Something went wrong with the loading! Things might be broken! We're sorry!"
#
#         #updateSave(save), function isn't done
#         x, y, z, dim = PLAYER.location
#         MAPS[x][y][z][dim].search(MAPS, DIMENSIONS,True)
#         return PLAYER,ITEMS,MAPS,ENEMIES,INTERACT,QUESTS,GAMEINFO, GAMESETTINGS



def updateSave(save): #this file tries to autoatically update the save file
    # TODO finish this for simple dictionary changes
    global PLAYER
    global ITEMS
    global MAPS
    global ENEMIES
    global INTERACT
    global QUESTS
    global GAMEINFO
    #Eventually have to catch for added creativemode items but not now
    #There's something in the current version than the save/old version.
    while True:
        #try:
        for info in GAMEINFO: #when itterating through list the itterating variable is the string of the key
            GAMEINFO[info] = loadinfo[info]
        #except KeyError as e:
        PLAYER.__dict__ = loadplayer.__dict__
        try: #this key error loop method isn't the most effecient but should be robust, could just compare keys/items
            for item in ITEMS:
                ITEMS[item] = loaditems[item] #assignment better when no subitems? .__dict for when there is
        except KeyError as e:
            loaditems.udate( {e:ITEMS[e]} ) #this is how you append to a dictionary, with another dictionary
            #wordFreqDic.update( {'before' : 23} )
            
        for enemy in ENEMIES:  #.__dict__ removed on these and it works?
            ENEMIES[enemy] = loadenemy[enemy]
        for inter in INTERACT:
            INTERACT[inter] = loadinter[inter]
        for quest in QUESTS:
            QUESTS[quest] = loadquest[quest]
        #for some reason putting MAPS load below these other ones fixed a bunch of bugs
        for x in range(XRANGE):
            for y in range(YRANGE):
                for z in range(ZRANGE):
                    for dim in range(DRANGE):
                        if MAPS[x][y][z][dim]: #There are different objects in 1 vs the other so need to replace object in each list with the new one of reference
                            MAPS[x][y][z][dim].__dict__ = loadmap[x][y][z][dim].__dict__
    
    
    
    return
 
def creative_parser(command):
    # EVERYTHING DISABLE FOR RELEASE
#     print command
#     # Going to go:
#     # / Commandtype Classtype /Noun/ (/ / so can be multiword without needing context) Attribute/Method(make sure all only 1 word) /Value/ (/ / if string, nothing if int/float/bool)
#     # ex) / Set Enemy /Dr. Minnick/ sinfo /WHO THE HELL ARE YOU/
#     # Does it one section at a time, splits left by two spaces gets first two words
#     # Splits around / / characters to get the rest
#
#     #testline = "Set Enemy /Dr. Minnick/ sinfo /WHO THE HELL ARE YOU/"
#
#     # Parser WILL BE DIFFERENT FOR EACH COMMAND based on what is needed
#     # Seperating the first 2 spaces to get first two words
#     spaceseperate = command.lower().split(" ", 2)  # SPLIT works from the left normally but rsplit works from the right
#     slashseperate = spaceseperate[2].split("/", 4)  # splits by lines
#     # info = info[:1]  # Could use [:-1] removes last element by taking subset n-1 ellements
#     del slashseperate[-1]  # deletes last empty element
#     del slashseperate[0]  # deletes 1st empty element, not deleting empty spaces because could be empty name
#     slashseperate[1] = slashseperate[1].strip(" ")  # gets rid of empty space in attribute
#     #Maybe delete empty spaces in each attritube
#
#     commandtype = spaceseperate[0].lower()
#     classtype = spaceseperate[1].lower()
#     noun = slashseperate[0].lower()
#
#     # Might leave these prints in there so people understand
#     print commandtype
#     print classtype
#     print noun
#     print attribute
#     print value
# # Go through first 3 values (commandtype, classtype, noun) then each subsequent one based on need
#
#
#     if commandtype == "read":   # passing to the read function
#         creative_read(classtype, spaceseperate[2])
#     # elif commandtype == "set":
#     #     creative_set(classtype, spaceseperate[2])
#     # elif commandtype == "new":
#     #     creative_new(classtype, spaceseperate[2])
#     # elif commandtype == "spawn":
#     #     creative_spawn(classtype, spaceseperate[2])
#     # elif commandtype == "remove":
#     #     creative_remove(classtype, spaceseperate[2])
#     # else:
#     #     print "I don't recognize that Creative command. Options are:\nRead, Set, New, Spawn, Remove"

    return

# Read
# read attributes
#/ex) / read Enemy /Dr. Minnick/ attack
# def creative_read(classtype, )
#     attribute = slashseperate[1].lower()
#     value = slashseperate[2].lower()
#
#
#     return

# Set
#set attributes
#/Set Enemy /Alex Jones/ info /I"M COMMIN/

# New
# creates a new base object
#/ Create Enemy Dr. Minnick2.0

# Spawn
# gives you a copy of that object at that location
#/ Spawn item msp430

# Remove
# Removes ALL of given ellement in the game at the time
#/ Remove Enemy Dr. Minnick

# needs to be error checking if that ellement doesn't exist, but will be no spellchecking


