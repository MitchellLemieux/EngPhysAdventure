#Developer testing 
from GameFunctions import *

x = PLAYER.location[0]
y = PLAYER.location[1]
z = PLAYER.location[2]
CurrentPlace = MAPS[x][y][z]
print CurrentPlace.lore + "\n" + CurrentPlace.info + "\n" + CurrentPlace.search()


while(PLAYER.alive):
    
  
    #Getting input and splitting it at the spaces
    direction = raw_input('What do you want to do?\n').lower().split(" ",1)
    #print direction
    
    if len(direction) == 1:

        verb = direction[0]
        
        if verb in ['u','d','l','r','f','b']:
            CurrentPlace = Move(verb)

        elif (verb == 'search'):
            print CurrentPlace.search()
            
        elif (verb == 'stats'):
            print "HEALTH: " + str(PLAYER.health)+"\n"+str(PLAYER.stats)


    elif (len(direction) == 2):
        verb = direction[0]
        objectName = direction [1]
        
        if verb == 'equip':
                Equip(objectName)
        
        if verb == 'drop':
                Drop(objectName)

        if verb == 'attack':
                Attack(objectName)

        if verb == 'talk':
            Talk(ObjectName)
        
                        

    

