#ENG PHYS TEXT  ADVENTURE
#Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
#Wrote on Dec  22,2018: 
import pickle
#from GameFunctions import *


def saveGame(savename, PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, extrainfo):

    f = open("SaveFile "+savename+".txt","w+")
    x = [PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, extrainfo] #puts all info into a list to be saved
##    types in x
##    <type 'instance'>
##    <type 'dict'>
##    <type 'tuple'>
##    <type 'dict'>
##    <type 'dict'>
##    <type 'dict'>
##    <type 'list'>
    pickle.dump(x, f) #pickles the list of gamedata to the save file
    f.close()
    print "Your game has been saved!"
    
    
def loadGame(loadname):
    global PLAYER
    global ITEMS
    global MAPS
    global ENEMIES
    global INTERACT
    global QUESTS
    try:
        f = open("SaveFile "+loadname +".txt","r+")
        save = pickle.load(f)
        f.close()
        print "You game has been loaded!"
        return save
    except IOError:
        print "There is no file named SaveFile " + savename
        return

 
