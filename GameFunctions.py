#This is the file used for most backend, interaction, startup/global variables,  functions of the game


from GameClasses import *
import StartUp
import AsciiArt
import time
import os #used to put files in the cache folder
import playsound #used to play music and sound effects


#This is where the global variables are defined. Global variables used to pass info between functions and dictionaries used to store many variables/objects in one place while making it clear in the code which one is being referenced
#TODO Ask Mitch why these aren't just in the main file
MAPS = StartUp.WorldMap() 
ITEMS = StartUp.ItemDictionary()
ENEMIES = StartUp.EnemyDictionary()
INTERACT = StartUp.InteractDictionary()
GAMEINFO = {'version':0,'versionname':"",'playername':" ",'gamestart':0,'timestart':0,
            'runtime': 0, 'stepcount':0,'commandcount':0,'log': [],"layersdeep":0,"savepath": "",
            'musicOn': 0.0} #this dictionary is used to store misc game info to be passed between function: speedrun time, start time, etc. Values are initialized to their value types
#version is version of the game, gamestart is the first start time of the game, runtime is the total second count, log is log of all player input, layers deep is how many layers deep in the laptop quest you are
#   musicOn is the indicator for when to next reloop the music

QUESTS = {}  #initializing the quests global variable to be later writen into

GAMESETTINGS = {'DisableOpening': 0, 'SpeedRun': 0, 'HardcoreMode':0, 'DisableMusic': 0}
#disable openning and/or music, speedrun disables openning;lore read times; might disable secrets or opens them, hardcore for now disables eating but might make enemies harder, 

STARTLOCATION = (2,3,1)
STARTHEALTH = 100


EMPTYHEAD = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','head',(0,0,0),-101)
EMPTYBODY = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','body',(0,0,0),-101)
EMPTYHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','hand',(0,0,0),-101)
EMPTYOFFHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','off-hand',(0,0,0),-101)
EMPTYINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
STARTINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
TYINV = {'head':ITEMS['visor glasses'],'body':ITEMS['big hits shirt'],'hand':ITEMS['hulk hands'],'off-hand':ITEMS['green bang bong']} #Setting a starting inventory bugs these somehow making them glitchy in the game, however having the item be dropped/spawned later somehow fixes this so that's the quick fix. Also gets to have the Iron Ring when he graduates
#STARTINV = {'head':ITEMS['gas mask'],'body':ITEMS['okons chainmail'],'hand':ITEMS['iron ring'],'off-hand':ITEMS['green bang bong']}

PLAYER = Character('Minnick',list(STARTLOCATION),STARTHEALTH,STARTINV,EMPTYINV)
Tyler = Character('Tyler Kashak',list(STARTLOCATION),999,TYINV,EMPTYINV)
MAPS[6][1][1].placeItem(ITEMS["big hits shirt"]) #having these spawn the items in the map after should get rid of the wierd bug from having Tyler Kashak having them to start
MAPS[0][3][0].placeItem(ITEMS["hulk hands"])

#Setting up the game path for the game to the cache folder
#using os here to get the current file path and the os.path.join to add the // or \ depending on if it's windows or linuix
GAMEINFO['savepath'] = os.path.join(os.getcwd(), "cache","")
try:
    os.makedirs(GAMEINFO['savepath']) #gets the directory then makes the path if it's not there
except:
    print "\n"#does nothing if the path is already there


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
        Place.removeItem(ITEMS[Item])
        Place.placeItem(drop)
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Link_Item.wav"), False) #plays the sound with 'multithreading'
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location:
        print "\nYou can't equip that, gosh\n"
    else:
        print "\nThat doesn't seem to be around here.\n"

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
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Link_Item_Away.wav"), False) #plays the sound with 'multithreading'
        #Same as equip function. 'None' passed to function if item doesn't exist
    else:
       print "You aren't carrying that item."


def Move(direction):
    global MAPS
    global PLAYER
    global ENEMIES
    bf = ENEMIES['brendan fallon']
    x = PLAYER.location[0]
    y = PLAYER.location[1]
    z = PLAYER.location[2]
    CurrentPlace = MAPS[x][y][z]
    Place = 0
    if direction not in CurrentPlace.walls: 
        if direction in ['f','forward']:
            y += 1
        elif direction in ['b','back']:
            y -= 1
        elif direction in ['r','right']:
            x += 1
        elif direction in ['l','left']:
            x -= 1
        elif direction in ['u','up']:
            z += 1
        elif direction in ['d','down']:
            z -= 1
        Place = MAPS[x][y][z]
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Steps_Stone3.wav"), False) #plays the sound with 'multithreading'
    if Place:
        PLAYER.location[0] = x
        PLAYER.location[1] = y
        PLAYER.location[2] = z
        if bf.location != (None,None,None):
            MAPS[bf.location[0]][bf.location[1]][bf.location[2]].removeEnemy(bf)
        if random() <= 0.003: #TODO make bang bong less awesome of BF more rare so he doesn't spawn and can't run train
            MAPS[x][y][z].placeEnemy(bf)
            AsciiArt.Hero()
            
        if Place.travelled:
            print "========================================================================"
            print Place.lore +"\n\n"+Place.info + Place.search()
            Place.travelled = 0
        else:
            print "========================================================================"
            print Place.info + Place.search()
            return Place
            
        
    else:
        PLAYER.location[0] = CurrentPlace.coords[0]
        PLAYER.location[1] = CurrentPlace.coords[1]
        PLAYER.location[2] = CurrentPlace.coords[2]
        print "\nYou can't go that way!\n"
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
                Damage = int(random()*FDamage)
                Second.health = max(0,Second.health - Damage)
            
            if Second.health:
                Damage = int(random()*SDamage)
                First.health = max(0,First.health - Damage)

     if First == P:           
         print "\nYou attack dealing " + str(SSHealth - Second.health) + " damage.\n" + Second.name + " deals " + str(FSHealth - First.health) + " damage.\n"
         print  "You have " + str(First.health) + " health remaining.\n" + Second.name + " has " + str(Second.health) + " health remaining.\n"
     else:
         print "\n"+First.name + " dealt " + str(SSHealth - Second.health) + " damage.\n" + "You attack dealing " + str(FSHealth - First.health) + " damage.\n"
         print  "You have " + str(Second.health) + " health remaining.\n" + First.name + " has " + str(First.health) + " health remaining.\n"
     if P.health == 0:
        P.alive = False
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","EFXdeath.mp3"), False) #plays the sound with 'multithreading'
        return 0
     if E.health == 0:
        E.alive = False
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","WilhelmScream.mp3"), False) #plays the sound with 'multithreading'
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
        enemy = ENEMIES[E] #making it the object from the name
        bgchance = 0.01
        if PLAYER.inv['head'] == ITEMS['skull helmet']:
            bgchance += 0.1 
        if PLAYER.inv['body'] == ITEMS['big hits shirt']:
            bgchance += 0.1
        if random() <= bgchance: #bigHits feature TODO have oblivion sound effects 
            AsciiArt.BigHits()
            print "\nAn oblivion gate opens and a purple faced hero in ebony armour punches\n" + enemy.name + " to death."
            print enemy.Dinfo + ".\n"
            enemy.alive = False
            if enemy.drop:
               print enemy.name + " dropped the " + ITEMS[enemy.drop].name + "."
               CurrentPlace.placeItem(ITEMS[enemy.drop])
        else:
           Outcome = Combat(PLAYER,enemy) 
           if Outcome:
               print "You defeated " + enemy.name + ".\n"
               print enemy.Dinfo
               if enemy.drop:
                   print enemy.name + " dropped the " + ITEMS[enemy.drop].name + "."
                   CurrentPlace.placeItem(ITEMS[enemy.drop])
           else:
               print "Oh no! You died, without ever finding your iron ring"
    else:
        print "\nThey don't appear to be here.\n"
                        

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
            print "\n"+ enemy.name + " took the " + enemy.need + "."
            print enemy.Sinfo
            ITEMS[enemy.need].location = (None, None, None) #Brendan added this, used to clear the item location
            PLAYER.inv[ITEMS[enemy.need].worn] = PLAYER.emptyinv[ITEMS[enemy.need].worn]
            PLAYER.updateStats()
            enemy.quest = True
            if enemy.drop:
                MAPS[x][y][z].placeItem(ITEMS[enemy.drop])
                print "You see a " + ITEMS[enemy.drop].name +".\n"
                enemy.drop = None      
        elif enemy.quest and enemy.drop:
            playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_SmallItem.wav"), False)
            print "\n"+enemy.Sinfo
            MAPS[x][y][z].placeItem(ITEMS[enemy.drop])
            print "You see a " + ITEMS[enemy.drop].name +".\n"
            enemy.drop = None
        elif enemy.quest:
            print "\n"+enemy.Sinfo+"\n"
        else:
            print "\n" + enemy.info+"\n"
        enemy.spoke = True
    elif E in ENEMIES and ((list(ENEMIES[E].location) == PLAYER.location)) and (ENEMIES[E].alive==False):
        print "\nI don't think they can do that anymore.\n"
    else:
        print "\nThey don't appear to be here.\n"


def Stats():
    playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","EFXpunchInspect.mp3"), False)
    global PLAYER
    print "\nHEALTH: " + str(PLAYER.health)
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
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","EFXpunchInspect.mp3"), False)
        print "\n"+ITEMS[Item].info
        print "ATK : " + str(ITEMS[Item].stats[0]) + " " + "("+str(ITEMS[Item].stats[0]-PLAYER.inv[ITEMS[Item].worn].stats[0])+")"
        print "DEF : " + str(ITEMS[Item].stats[1]) + " " + "("+str(ITEMS[Item].stats[1]-PLAYER.inv[ITEMS[Item].worn].stats[1])+")"
        print "SPD : " + str(ITEMS[Item].stats[2]) + " " + "("+str(ITEMS[Item].stats[2]-PLAYER.inv[ITEMS[Item].worn].stats[2])+")"
        print "WORN: " + str(ITEMS[Item].worn).upper()
        if ITEMS[Item].health: #if edible it shows that health stat plus what your final health would be if eaten
            print "Edible: Yes\n " #+ str(ITEMS[Item].health) + " (" + str(min(100,PLAYER.health + ITEMS[Item].health))+")" +"\n"
        else:
            print""
    elif Item in INTERACT and list(INTERACT[Item].location) == PLAYER.location: #this is for item = interactable
        if INTERACT[Item].need and PLAYER.inv[ITEMS[INTERACT[Item].need].worn]==ITEMS[INTERACT[Item].need]: #if you have the item the interactable needs worn on your body
            playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_SmallItem.wav"), False)
            PLAYER.inv[ITEMS[INTERACT[Item].need].worn] = PLAYER.emptyinv[ITEMS[INTERACT[Item].need].worn]
            INTERACT[Item].quest = True #this turns on the quest flag for the interactable once interacted with if you have the item
            print "\n" + INTERACT[Item].Sinfo
            PLAYER.updateStats()
            ITEMS[INTERACT[Item].need].location=(None,None,None) #Brendan added this, used to clear the item location
            if INTERACT[Item].drop:
                MAPS[x][y][z].placeItem(ITEMS[INTERACT[Item].drop])
                print "You see a " + ITEMS[INTERACT[Item].drop].name +"."
            print ""
        else:
            print INTERACT[Item].info + "\n"
    else:
        print "\nThat doesn't seem to be around here.\n"

def Inventory():
    playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","EFXpunchInspect.mp3"), False)
    global PLAYER
    print ""
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

    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location and not(GAMESETTINGS['HardcoreMode']):
        if Item == "jar of peanut butter" and (PLAYER.name in ["Mitchell Lemieux","Erik Reimers"]):
            print "Oh NO! You're " + PLAYER.name + " ! Don't you remember?\nYOU'RE ALERGIC TO PEANUT BUTTER?\nYou DIE due to your lack of responsibility."
            PLAYER.health = 0
            PLAYER.alive = False
        elif ITEMS[Item].health:
            PLAYER.health = PLAYER.health + ITEMS[Item].health
            PLAYER.health = min(PLAYER.maxhealth, PLAYER.health) #made the minimum of your added health and food so players health doesn't clip over
            PLAYER.health = max(PLAYER.health, 0) #prevents clipping bellow 0
            print "\nYou've eaten the " + ITEMS[Item].name + ".\nHEALTH: "+ str(PLAYER.health)+"\n"
            if PLAYER.health == 0:
                PLAYER.alive = False
            ITEMS[Item].location = (None, None, None) #used to clear the item location
            if ITEMS[Item] == PLAYER.inv[ITEMS[Item].worn]:
                PLAYER.inv[ITEMS[Item].worn] = PLAYER.emptyinv[ITEMS[Item].worn]
                ITEMS[Item].location = (None, None, None)
                PLAYER.updateStats()
                print "The " + ITEMS[Item].name + " has been removed from your inventory.\n"
            else:
                MAPS[x][y][z].removeItem(ITEMS[Item])
    
        else:
            print "You can't eat that!"
    else:
        print "\nThat doesn't seem to be around here.\n"


#BackEnd Functions
        
def logGame(log): #this makes a log file which records all player actions for debugging
    fpath = GAMEINFO['savepath'] + "MetaChache " + GAMEINFO['playername']+".txt" #metacache is a fake name for the log file
    f = open(fpath,"w+") 
    for i in range(len(log)):
        f.write(str(log[i]) + '\n')
    f.close()

def NameChange(): #A dumb backend workaround to change the players name. TODO other strategies could have startup instantatied after name is defined
    global PLAYER
    global ENEMIES
    global MAPS
    #ENEMIES['yourself'].name = playername
    ENEMIES['yourself'].name = PLAYER.name #yourself gets renamed to player name
    ENEMIES.update({PLAYER.name.lower():ENEMIES['yourself']}) #adds that new entity to the dictionary
    MAPS[2][4][1].placeEnemy(ENEMIES[PLAYER.name.lower()]) #then placed on the map
    return
        
def SpellCheck(Word,Psblties): #Spellchecks words in the background to check things closest
    Distance = [edit_distance(Word,key) for key in Psblties]
    index = Distance.index(min(Distance))
    return Psblties[index]

def DisplayTime(value): #converts and displays the time given seconds, for speedrunning
    '''From seconds to Days;Hours:Minutes;Seconds'''
    valueD = (((value/24)/60)/60)
    Days = int (valueD)
    valueH = (value-Days*24*3600)
    Hours = int(valueH/3600)
    valueM = (valueH - Hours*3600)
    Minutes = int(valueM/60)
    valueS = (valueM - Minutes*60)
    Seconds = int(valueS)
    print "Your run-time was: ", Days,"Days; ",Hours,"Hours: ",Minutes,"Minutes; ",Seconds,"Seconds"

def Music(): #a check system to play the song every 43.5 seconds while alive
    length = time.time()-GAMEINFO['timestart'] #checks to see if it's past the time it should have played (will make it choppy but limitted by this module)
    if length > GAMEINFO['musicOn']:
        audiopath = os.path.join(os.getcwd(), "MediaAssets","","ErikBeepBoxSong.mp3") #points to the eddited star wars theme
        playsound.playsound(audiopath, False) #plays the sound with 'multithreading'
        GAMEINFO['musicOn'] += 60 #increments by minute until it will next have to be played


def PrintT(printout): #TODO a possible macro function to auto format and display our text

    return

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
        

    
        
    


    
