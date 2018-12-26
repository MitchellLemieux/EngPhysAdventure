#ENG PHYS TEXT  ADVENTURE
#Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
#Wrote on Dec  22,2018: 
import pickle
global PLAYER
global ITEMS
global MAPS
global INTERACT
global playername
global QUESTS

def saveGame(PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, extrainfo):
    f = open("SaveFile.txt","w+")
    x = [PLAYER, ITEMS, MAPS, ENEMIES, INTERACT, QUESTS, extrainfo]
    #x = PLAYER
##print type(PLAYER)
##print type(ITEMS)
##print type(MAPS)
##print type(INTERACT)
##print type(QUESTS)
##
##<type 'instance'>
##<type 'dict'>
##<type 'tuple'>
##<type 'dict'>
##<type 'dict'>

    pickle.dump(x, f)
    
    f.close()
    print "Your game has been saved!"
    
def loadGame():
    global PLAYER
    f = open("SaveFile.txt","r+")
    loaddata = pickle.load(f)
    f.close()
    print "You game has been loaded!"
    return loaddata
    
    print "Your game has been loaded " + str(PLAYER.name)
    return save

    
    
    
#    #all the character stats
#    print PLAYER.name
#    print PLAYER.location
#    for i in PLAYER.inv: #this prints out just the inventory names
#        print PLAYER.inv[i].name
#    print PLAYER.health
#    print PLAYER.stats
#    print PLAYER.alive
#    
#    for item in ITEMS: #printing out all the attributes of each item
#        print item
#        print ITEMS[item].image
#        print ITEMS[item].info
#        print ITEMS[item].worn
#        print ITEMS[item].stats
#        print ITEMS[item].location
#        print ITEMS[item].health
#
#        
    print "The game has been saved!"
 
