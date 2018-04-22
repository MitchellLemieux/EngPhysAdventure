from GameClasses import *
import StartUp


MAPS = StartUp.WorldMap()
ITEMS = StartUp.ItemDictionary()
ENEMIES = StartUp.EnemyDictionary()
INTERACT = StartUp.InteractDictionary()

STARTLOCATION = (2,3,1)
STARTHEALTH = 100

EMPTYHEAD = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','head',(0,0,0),-101)
EMPTYBODY = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','body',(0,0,0),-101)
EMPTYHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','hand',(0,0,0),-101)
EMPTYOFFHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','off-hand',(0,0,0),-101)
EMPTYINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
STARTINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
#STARTINV = {'head':ITEMS['gas mask'],'body':ITEMS['okons chainmail'],'hand':ITEMS['the solar ray'],'off-hand':ITEMS['diary of the fallen']}

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
       global MAPS
    global PLAYER
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    CurrentPlace = MAPS[x][y][z]
    Place = 0
    if direction not in CurrentPlace.walls:
        if direction == 'f':
            y += 1
        elif direction == 'b':
            y -= 1
        elif direction == 'r':
            x += 1
        elif direction == 'l':
            x -= 1
        elif direction == 'u':
            z += 1
        elif direction == 'd':
            z -= 1
        Place = MAPS[x][y][z]
    if Place:
        PLAYER.location[0] = x
        PLAYER.location[1] = y
        PLAYER.location[2] = z
        if Place.travelled:
            print "========================================================================"
            print Place.lore + "\n\n" + Place.info + Place.search()
            Place.travelled = 0
        else:
            print "========================================================================"
            print "\n"+Place.info
            print "\n" +Place.search()
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
    if E in ENEMIES and (list(ENEMIES[E].location) == PLAYER.location) and (ENEMIES[E].alive):
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
    if E in ENEMIES and ((list(ENEMIES[E].location) == PLAYER.location)) and (ENEMIES[E].alive):
        enemy = ENEMIES[E]
        if enemy.need and PLAYER.inv[ITEMS[enemy.need].worn]==ITEMS[enemy.need]and not enemy.quest:
            print enemy.Sinfo
            print enemy.name + " took the " + enemy.need + "."
            ITEMS[enemy.need].location = (None, None, None) #Brendan added this, used to clear the item location
            PLAYER.inv[ITEMS[enemy.need].worn] = PLAYER.emptyinv[ITEMS[enemy.need].worn]
            PLAYER.updateStats()
            enemy.quest = True
            if enemy.drop:
                MAPS[x][y][z].placeItem(ITEMS[enemy.drop])
                print "You see a " + ITEMS[enemy.drop].name +".\n"
                enemy.drop = None      
        elif enemy.quest and enemy.drop:
            print enemy.Sinfo
            print "You see a " + ITEMS[enemy.drop].name +".\n"
            enemy.drop = None
        elif enemy.quest:
            print enemy.Sinfo
        else:
            print enemy.info
        enemy.spoke = True
    else:
        print "They don't appear to be here.\n"


def Stats():
    global PLAYER
    print "HEALTH: " + str(PLAYER.health)
    print "ATK: " + str(PLAYER.stats[0])
    print "DEF: " + str(PLAYER.stats[1])
    print "SPD: " + str(PLAYER.stats[2])+"\n"

def Inspect(Item): #Item is the inspect item
    global MAPS
    global ITEMS
    global PLAYER
    global INTERACT
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location: #this is for item = equipment
        print "\n"+ITEMS[Item].info
        print "ATK : " + str(ITEMS[Item].stats[0]) + " " + "("+str(ITEMS[Item].stats[0]-PLAYER.inv[ITEMS[Item].worn].stats[0])+")"
        print "DEF : " + str(ITEMS[Item].stats[1]) + " " + "("+str(ITEMS[Item].stats[1]-PLAYER.inv[ITEMS[Item].worn].stats[1])+")"
        print "SPD : " + str(ITEMS[Item].stats[2]) + " " + "("+str(ITEMS[Item].stats[2]-PLAYER.inv[ITEMS[Item].worn].stats[2])+")"
        print "WORN: " + str(ITEMS[Item].worn).upper()
        if ITEMS[Item].health > -101: #if edible it shows that health stat plus what your final health would be if eaten
            print "Edible: Yes " #+ str(ITEMS[Item].health) + " (" + str(min(100,PLAYER.health + ITEMS[Item].health))+")" +"\n"
        
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location: #this is for item = interactable
        if INTERACT[Item].need and PLAYER.inv[ITEMS[INTERACT[Item].need].worn]==ITEMS[INTERACT[Item].need]:
            PLAYER.inv[ITEMS[INTERACT[Item].need].worn] = PLAYER.emptyinv[ITEMS[INTERACT[Item].need].worn]
            INTERACT[Item].quest = True
            print "\n" + INTERACT[Item].Sinfo + "\n"
            PLAYER.updateStats()
            ITEMS[INTERACT[Item].need].location = (None, None, None) #Brendan added this, used to clear the item location
            if INTERACT[Item].drop:
                MAPS[x][y][z].placeItem(ITEMS[INTERACT[Item].drop])
                print "You see a " + ITEMS[INTERACT[Item].drop].name +".\n"
                INTERACT[Item].drop = None
        else:
            print "\n" + INTERACT[Item].info + "\n"
    else:
        print "That doesn't seem to be around here.\n"

def Inventory():
    global PLAYER
    print "\n"
    for i in PLAYER.inv:
        print i.upper() + ": " + PLAYER.inv[i].name
    print ""

def Eat(Item):
    global PLAYER
    global ITEMS
    global MAPS
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    
    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location:
        if ITEMS[Item].health > -101:
            PLAYER.health = PLAYER.health + ITEMS[Item].health
            PLAYER.health = min(100, PLAYER.health)
            print "You've eaten the " + ITEMS[Item].name + ".\n HEALTH: " + str(PLAYER.health)
            ITEMS[Item].location = (None, None, None) #used to clear the item location
            if ITEMS[Item] == PLAYER.inv[ITEMS[Item].worn]:
                PLAYER.inv[ITEMS[Item].worn] = PLAYER.emptyinv[ITEMS[Item].worn]
                PLAYER.updateStats()
                print "The " + ITEMS[Item].name + " has been removed from your inventory."
            else:
                MAPS[x][y][z].Remove(ITEMS[Item])
           
           
        else:
            print "You can't eat that!"
    else:
        print "That doesn't seem to be around here.\n"

QUESTS = {"talk to mysterious man": 1,
          "preston get dumbbell": 1,
          "buijs kill chris" : 1,
          "dan fix reactor" : 1,
          "novog get donut" : 1,
          "feynman mirror" :1,
          "kitai get silicon substrate": 1,
          "lapierre get coffee": 1,
          "knights get book": 1,
          "haugen kill soleymani" : 1,
          
         
          }


def Story():
    global PLAYER
    global QUESTS
    global ITEMS
    global ENEMIES
    global INTERACT
    global MAPS
    
    #Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1].placeEnemy(ENEMIES["dr.kitai"])
        MAPS[2][4][2].placeEnemy(ENEMIES["dr.preston"])
        MAPS[1][6][2].placeEnemy(ENEMIES["dr.lapierre"])
        MAPS[5][4][1].removeEnemy(ENEMIES["hooded man"])
        QUESTS["talk to mysterious man"] = 0

    
        
    if ENEMIES['dr.preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1].placeEnemy(ENEMIES["dr.buijs"])
        QUESTS["preston get dumbbell"] = 0
        
    if ENEMIES['dr.buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0].placeEnemy(ENEMIES['dan fitzgreen'])
        QUESTS['buijs kill chris'] = 0

    if ENEMIES['dan fitzgreen'].spoke and INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        ENEMIES['dan fitzgreen'].quest = True
        MAPS[2][6][0].placeEnemy(ENEMIES['dr.novog'])
        QUESTS["dan fix reactor"] = 0
        
    if ENEMIES['dr.novog'].quest and QUESTS["novog get donut"]:
        QUESTS['novog get donut'] = 0

    if INTERACT['ancient mirror'].quest and QUESTS["feynman mirror"]:
        QUESTS["feynman mirror"] = 0

    if ENEMIES['dr.kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2].placeEnemy(ENEMIES['dr.kleimann'])
        QUESTS['kitai get silicon substrate'] = 0
    
    
    if ENEMIES['dr.lapierre'].quest and QUESTS["lapierre get coffee"]:
        MAPS[5][4][1].placeEnemy(ENEMIES['dr.knights'])
        QUESTS["lapierre get coffee"]= 0
        
    if ENEMIES['dr.knights'].quest and QUESTS["knights get book"]:
        MAPS[1][6][0].placeEnemy(ENEMIES['dr.haugen'])
        QUESTS["knights get book"] = 0
    

    if ENEMIES['dr.haugen'].spoke and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        

    
