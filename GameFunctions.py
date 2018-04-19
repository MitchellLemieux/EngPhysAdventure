from GameClasses import *
import StartUp


MAPS = StartUp.WorldMap()
ITEMS = StartUp.ItemDictionary()
ENEMIES = StartUp.EnemyDictionary()
INTERACT = StartUp.InteractDictionary()

STARTLOCATION = (2,3,1)
STARTHEALTH = 100

EMPTYHEAD = Equipment('EMPTY',(0,0,0),'EMPTY.png','Nothing is Equipped','head',(0,0,0))
EMPTYBODY = Equipment('EMPTY',(0,0,0),'EMPTY.png','Nothing is Equipped','body',(0,0,0))
EMPTYHAND = Equipment('EMPTY',(0,0,0),'EMPTY.png','Nothing is Equipped','hand',(0,0,0))
EMPTYOFFHAND = Equipment('EMPTY',(0,0,0),'EMPTY.png','Nothing is Equipped','off-hand',(0,0,0))
EMPTYINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
STARTINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}

PLAYER = Character('Minnick',list(STARTLOCATION),STARTHEALTH,STARTINV,EMPTYINV)


def Equip(Item):
    global PLAYER
    global ITEMS
    global MAPS
    global INTERACT
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    Place = MAPS[x][y][z]
    if Item in ITEMS:
        #this is different than the equip method in the Character class.
        #Makes sure the item is dropped at the current location
        drop = PLAYER.equip(ITEMS[Item])
        Place.Remove(ITEMS[Item])
        Place.placeItem(drop)
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:
        print "You can't equip that, gosh"
    else:
        print "That doesn't seem to be around here."

def Drop(Item):
    global MAPS
    global PLAYER
    global ITEMS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    Place = MAPS[x][y][z]
    if Item in ITEMS:
        drop = PLAYER.drop(ITEMS[Item])
        Place.placeItem(drop)
        #Same as equip function. 'None' passed to function if item doesn't exist
    else:
       print "You aren't carrying that item."


def Move(direction):
    global MAPS
    global PLAYER
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    CurrentPlace = MAPS[x][y][z]
    Place = 0
    if direction not in CurrentPlace.walls:
        PLAYER.move(direction)
        x = PLAYER.location[0]
        y = PLAYER.location[1]
        z = PLAYER.location[2]
        Place = MAPS[x][y][z]
    if Place:
        if Place.travelled:
            print Place.lore + "\n" + Place.info + Place.search()
            Place.travelled = 0
        else:
            print Place.info + Place.search()
        return Place
    else:
        PLAYER.location = list(CurrentPlace.coords)
        print "You can't go that way!\n"
        return CurrentPlace

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
            First = choice(Combatatants)
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
                Damage = int(random()*FDamage)
                Second.health = max(0,Second.health - Damage)
            
            if Second.health:
                Damage = int(random()*SDamage)
                First.health = max(0,First.health - Damage)

     if First == P:           
         print "You attack dealing " + str(SSHealth - Second.health) + " damage.\n" + Second.name + " deals " + str(FSHealth - First.health) + " damage.\n"
         print  "You have " + str(First.health) + " health remaining.\n" + Second.name + " has " + str(Second.health) + " health remaining.\n"
     else:
         print First.name + " dealt " + str(SSHealth - Second.health) + " damage.\n" + "You attack dealing " + str(FSHealth - First.health) + " damage.\n"
         print  "You have " + str(Second.health) + " health remaining.\n" + First.name + " has " + str(First.health) + " health remaining.\n"
     if P.health == 0:
        P.alive = False
        return 0
     if E.health == 0:
        E.alive = False
        return 1

def Attack(E):
    global ENEMIES
    global MAPS
    global PLAYER
    global ITEMS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    CurrentPlace = MAPS[x][y][z]
    if E in ENEMIES and (ENEMIES[E].location == tuple(PLAYER.location)) and (ENEMIES[E].alive):
        enemy = ENEMIES[E]
        if random() <= 0.01:
            print "An oblivion gate opens and a purple faced hero in ebony armour punches " + enemy.name + " to death.\n"
            print enemy.Dinfo + ".\n"
            if enemy.drop:
               print enemy.name + " dropped the " + ITEMS[enemy.drop].name + "."
               CurrentPlace.placeItem(ITEMS[enemy.drop])
        else:
           Outcome = Combat(PLAYER,enemy) 
           if Outcome:
               print "You defeated " + enemy.name + ".\n"
               print enemy.Dinfo + ".\n"
               if enemy.drop:
                   print enemy.name + " dropped the " + ITEMS[enemy.drop].name + "."
                   CurrentPlace.placeItem(ITEMS[enemy.drop])
           else:
               print "Oh no! You died, without ever finding your iron ring"
    else:
        print "They don't appear to be here."
                        

def Talk(E):
    global ENEMIES
    global MAPS
    global PLAYER
    global ITEMS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    if E in ENEMIES and (ENEMIES[E].location == tuple(PLAYER.location)) and (ENEMIES[E].alive):
        enemy = ENEMIES[E]
        if enemy.need and PLAYER.inv[ITEMS[enemy.need].worn]==ITEMS[enemy.need]and not enemy.quest:
            print enemy.Sinfo
            print enemy.name + " took the " + enemy.need + "."
            enemy.quest = True
            MAPS[x][y][z].placeItem(ITEMS[enemy.drop])
            print "You see a " + ITEMS[enemy.drop].name +".\n"
            enemy.drop = None
            PLAYER.inv[ITEMS[enemy.need].worn] = PLAYER.emptyinv[ITEMS[enemy.need].worn]
        elif enemy.quest:
            print enemy.Sinfo
        else:
            print enemy.info
    else:
        print "They don't appear to be here.\n"


def Stats():
    global PLAYER
    print "HEALTH: " + str(PLAYER.health)
    print "ATK: " + str(PLAYER.stats[0])
    print "DEF: " + str(PLAYER.stats[1])
    print "SPD: " + str(PLAYER.stats[2])+"\n"

def Inspect(Item):
    global MAPS
    global ITEMS
    global PLAYER
    global INTERACT
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location:
        print "\n"+ITEMS[Item].info
        print "ATK : " + str(ITEMS[Item].stats[0])
        print "DEF : " + str(ITEMS[Item].stats[1])
        print "SPD : " + str(ITEMS[Item].stats[2])
        print "WORN: " + str(ITEMS[Item].worn).upper()+"\n"
            
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:
        if Item.need and PLAYER.inv[ITEMS[Item.need].worn]==ITEMS[Item.need]:
            PLAYER.inv[ITEMS[Item.need].worn] = PLAYER.emptyinv[ITEMS[Item.need].worn]
            Item.quest = True
            print Item.Sinfo
            if Item.drop:
                MAPS[x][y][z].placeItem(ITEMS[Item.drop])
                print "You see a " + ITEMS[Item.drop].name +".\n"
                Item.drop = None
        else:
            print Item.info
    else:
        print "That doesn't seem to be around here.\n"

def Inventory():
    global PLAYER
    print "\n"
    for i in PLAYER.inv:
        print i.upper() + ": " + PLAYER.inv[i].name
    print ""
    
    
    
