#ENG PHYS TEXT  ADVENTURE
#Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
#Wrote on Dec  22,2018: 
import pickle
from GameFunctions import * #importing the global dictionaries/values
from StartUp import XRANGE, YRANGE, ZRANGE, DRANGE #Importing the map bound variables from StartUp to be used in the load function
import CSVSaves

def saveGame(savename):
    global PLAYER
    global ITEMS
    global MAPS
    global ENEMIES
    global INTERACT
    global QUESTS
    global GAMEINFO
    global GAMESETTINGS

    # this saves current state to csv file, disabled by default for releasing exe
    # TODO Make these files into the loading with encryption
    # TODO Turn off CSV saves before compiling
    CSVSaves.entities_to_CSV(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS)

    f = open(GAMEINFO['savepath'] + "SaveFile " + savename + ".txt", "w+")
    x = [PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, GAMEINFO, GAMESETTINGS] # puts all info into a list to be saved
##    types in x
##    <type 'instance'>
##    <type 'dict'>
##    <type 'tuple'>
##    <type 'dict'>
##    <type 'dict'>
##    <type 'dict'>
##    <type 'dict'>
##    <type 'dict'>
    pickle.dump(x, f) #pickles the list of gamedata to the save file
    f.close()
    return
    
    
def loadGame(loadname):
    global PLAYER
    global ITEMS
    global MAPS
    global ENEMIES
    global INTERACT
    global QUESTS
    global GAMEINFO
    global GAMESETTINGS
    try:
        f = open(GAMEINFO['savepath'] +"SaveFile "+loadname +".txt","r+")
        save = pickle.load(f)
        f.close()
        #seperates the list
        loadplayer = save[0]
        loaditems = save[1]
        loadmap = save[2]
        loadenemy = save[3]
        loadinter = save[4]
        loadquest = save[5]
        loadinfo = save[6]
        loadsettings = save[7]
        
        
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
        for setting in GAMESETTINGS:
            GAMESETTINGS[setting] = loadsettings[setting]
        #for some reason putting MAPS load below these other ones fixed a bunch of bugs
        for x in range(XRANGE):
            for y in range(YRANGE):
                for z in range(ZRANGE):
                    for dim in range (DRANGE):
                        if MAPS[x][y][z][dim]: #There are different objects in 1 vs the other so need to replace object in each list with the new one of reference
                            MAPS[x][y][z][dim].__dict__ = loadmap[x][y][z][dim].__dict__

        GAMEINFO['commandcount'] += 1 #+1 command to load the game because it doesn't count the loadgame command
        GAMEINFO['log'].append("loadgame") #adds the load game command to the log

        
        #Displayes the current place info again to show it's been loaded
        CurrentPlace = MAPS[PLAYER.location[0]][PLAYER.location[1]][PLAYER.location[2]][PLAYER.location[3]]
        print "========================================================================"
        if CurrentPlace.travelled == 1: #To print out the starting location for new files
            print CurrentPlace.lore
        print CurrentPlace.info + CurrentPlace.search() #prints the basic lore to give you bearing on where you are

        #YOU HAVE TO USE THIS DARN .__dict___ thing to copy the object atributes https://stackoverflow.com/questions/36243488/how-can-i-overwrite-an-object-in-python
        #This is ineffecient but works. I think main problem I had is loading where the loaded objects are a new memory location but the game still references old locations
        #It's best to reference things by name  
        #Acording to this lists make new functions: http://interactivepython.org/runestone/static/CS152f17/Lists/ObjectsandReferences.html
        #use (a is b) to see if a and b refer to the same memory location
        return PLAYER,ITEMS,MAPS,ENEMIES,INTERACT,QUESTS,GAMEINFO
    except IOError:
        print "There is no file named SaveFile " + loadname + ". Please try again."
        return
    except (KeyError,AttributeError): #dictionary = key error (ITEMS, ENEMIES, INTERACTS, quest, gameinfo), atribute error = Map error or object attribute
        print "There is a mismatch between the versions of the game."
        if GAMEINFO['version'] > loadinfo['version']:
            print "This is an old version of the game. Attempting to update the file"
        else:
            print "Attempting to reconsile the different versions automatically."
        #updateSave(save), function isn't done
        return

    #except KeyError as E

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
 
