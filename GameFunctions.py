from GameClasses import *
import StartUp
import AsciiArt
import Opening #used for the EPTA all the way down quest
import time
import os #used to put files in the cache folder


#This is where the global variables are defined. Global variables used to pass info between functions and dictionaries used to store many variables/objects in one place while making it clear in the code which one is being referenced
#TODO Ask Mitch why these aren't just in the main file
MAPS = StartUp.WorldMap() 
ITEMS = StartUp.ItemDictionary()
ENEMIES = StartUp.EnemyDictionary()
INTERACT = StartUp.InteractDictionary()
GAMEINFO = {'version':0,'versionname':"",'playername':" ",'gamestart':0,'timestart':0,
            'runtime': 0, 'stepcount':0,'commandcount':0,'log': [],"layersdeep":0,"savepath": ""} #this dictionary is used to store misc game info to be passed between function: speedrun time, start time, etc. Values are initialized to their value types
#version is version of the game, gamestart is the first start time of the game, runtime is the total second count, log is log of all player input, layers deep is how many layers deep in the laptop quest you are

STARTLOCATION = (2,3,1)
STARTHEALTH = 100


EMPTYHEAD = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','head',(0,0,0),-101)
EMPTYBODY = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','body',(0,0,0),-101)
EMPTYHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','hand',(0,0,0),-101)
EMPTYOFFHAND = Equipment('EMPTY',(None,None,None),'EMPTY.png','Nothing is Equipped','off-hand',(0,0,0),-101)
EMPTYINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
STARTINV = {'head':EMPTYHEAD,'body':EMPTYBODY,'hand':EMPTYHAND,'off-hand':EMPTYOFFHAND}
TYINV = {'head':ITEMS['visor glasses'],'body':ITEMS['big hits shirt'],'hand':ITEMS['hulk hands'],'off-hand':ITEMS['green bang bong']} #gets to have the Iron Ring when he graduates
#STARTINV = {'head':ITEMS['gas mask'],'body':ITEMS['okons chainmail'],'hand':ITEMS['iron ring'],'off-hand':ITEMS['green bang bong']}

PLAYER = Character('Minnick',list(STARTLOCATION),STARTHEALTH,STARTINV,EMPTYINV)
Tyler = Character('Tyler Kashak',list(STARTLOCATION),999,TYINV,EMPTYINV)

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
        #febreeze isn't droped
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
        if bf.location != (None,None,None):
            MAPS[bf.location[0]][bf.location[1]][bf.location[2]].removeEnemy(bf)
        if random() <= 0.003:
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
        enemy = ENEMIES[E] #making it the object from the name
        if random() <= 0.01: #bigHits feature
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
            print "\n"+enemy.Sinfo
            MAPS[x][y][z].placeItem(ITEMS[enemy.drop])
            print "You see a " + ITEMS[enemy.drop].name +".\n"
            enemy.drop = None
        elif enemy.quest:
            print "\n"+enemy.Sinfo+"\n"
        else:
            print "\n" + enemy.info+"\n"
        enemy.spoke = True
    else:
        print "\nThey don't appear to be here.\n"


def Stats():
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

    if Item in ITEMS and list(ITEMS[Item].location) == PLAYER.location:
        if Item == "jar of peanut butter" and (PLAYER.name == "Mitchell Lemieux" or "Erik Reimers"):
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

def logGame(log): #this makes a log file which records all player actions for debugging
    fpath = GAMEINFO['savepath'] + "MetaChache " + GAMEINFO['playername']+".txt" #metacache is a fake name for the log file
    f = open(fpath,"w+") 
    for i in range(len(log)):
        f.write(str(log[i]) + '\n')
    f.close()
    
QUESTS = {
          #sidequests
          'secret spaces': 1,
          'EPTA all the way down': 1,
          #Talk to hooded man
          "talk to mysterious man": 1,
          #Nuke
          "preston get dumbbell": 1,
          "buijs kill chris" : 1,
          "dan fix reactor" : 1,
          "novog get donut" : 1,
          "feynman mirror" :1,
          #Optics
          "kitai get silicon substrate": 1,
          "knights get book": 1,
          "haugen kill soleymani" : 1,
          "einstein fridge": 1,
          #Semiconductor
          "lapierre get coffee": 1,
          "kleimann get solar cell": 1,
          "minnick get oscilloscope": 1,
          "get key to display case": 1,
          "maxwell portal": 1,
          #endgame stuff
          'end game start' :1,
          'the dark lord' :1,
          'university man':1,
          'restored order': 1,
          'create chaos': 1
          }


def Story():
    global PLAYER
    global QUESTS
    global ITEMS
    global ENEMIES
    global INTERACT
    global MAPS
    #Side Quests
    if INTERACT['coat of arms'].quest and QUESTS["secret spaces"]: #Unlocks the secret space once you get the scroll
        MAPS[0][2][1].removeWall("d")
        QUESTS["secret spaces"] = 0
    
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']: #when you put the pen in the laptop it restarts the game
    #TODO as homework see if there's a way to do this with recursion instead of simulating it
        playgame = raw_input('========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame =="y":
            print "You click on the game and it begins in the terminal. The drumming \nintensifies. You're not sure if you made the right choice.\n========================================================================\n\n\n"
            import CreativeMode #this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler
            QUESTS['EPTA all the way down'] = 0 #Truns off the quest, has to be before the game saves so the quest is ended when you come back
            CreativeMode.saveGame(str(GAMEINFO['layersdeep'])) #saving game to be reloaded after death or won the game
            log =  GAMEINFO['log'] #keeps the log as a temporary variable to keep a running log in the nested game
            Opening.Opening()
            newplayername = raw_input("First, what is your name?\n")
            layers = GAMEINFO['layersdeep'] #saves layersdeep to a temporary variable for after the load
            CreativeMode.loadGame("basegame") #should display the exact start
            GAMEINFO['layersdeep'] = layers + 1 #increments the global layers deep because you're now in a lower level, using the memory of the local variable

            GAMEINFO['playername']= PLAYER.name = newplayername #this is done for the log
            GAMEINFO['gamestart'] = time.time() #Settign the game and timestart for for this layer
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            #Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame),"--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],  GAMEINFO['playername'], time.ctime(GAMEINFO['timestart']), "--LOG START--"] #log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame =="n":
            print "You decide against it, fearing the worst. You safely edject the pen, \ndrop it on the floor, and smash it to pieces. Better safe than sorry.\nThe drumming stops.\n========================================================================"
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)] #adds your command to the log
        else:
            print "It was a yes or no question. When you look back the files are gone.\nEven flexpde. Good riddance.\n========================================================================"
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)] #adds your command to the log
    
    #Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1].placeEnemy(ENEMIES["dr. kitai"])
        MAPS[2][4][2].placeEnemy(ENEMIES["dr. preston"])
        MAPS[1][6][2].placeEnemy(ENEMIES["dr. lapierre"])
        MAPS[5][4][1].removeEnemy(ENEMIES["hooded man"])
        ENEMIES['hooded man'].spoke = False
        QUESTS["talk to mysterious man"] = 0

    #Nuke quests
    if ENEMIES['dr. preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1].placeEnemy(ENEMIES["dr. buijs"])
        QUESTS["preston get dumbbell"] = 0
        
    if ENEMIES['dr. buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0].placeEnemy(ENEMIES['dan fitzgreen'])
        ENEMIES['dan fitzgreen'].quest = True
        
        QUESTS['buijs kill chris'] = 0

    if ENEMIES['dan fitzgreen'].spoke and INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        MAPS[2][6][0].placeEnemy(ENEMIES['dr. novog'])
        QUESTS["dan fix reactor"] = 0
        
    if ENEMIES['dr. novog'].quest and QUESTS["novog get donut"]:
        QUESTS['novog get donut'] = 0

    if INTERACT['ancient mirror'].quest and QUESTS["feynman mirror"]:
        QUESTS["feynman mirror"] = 0

    
    #Optics quests
    if ENEMIES['dr. lapierre'].quest and QUESTS["lapierre get coffee"]:
        MAPS[5][4][1].placeEnemy(ENEMIES['dr. knights'])
        QUESTS["lapierre get coffee"]= 0
        
    if ENEMIES['dr. knights'].quest and QUESTS["knights get book"]:
        MAPS[1][6][0].placeEnemy(ENEMIES['dr. haugen'])
        QUESTS["knights get book"] = 0
    

    if ENEMIES['dr. haugen'].quest and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        ENEMIES['dr. haugen'].alive = False
        MAPS[1][6][0].removeEnemy(ENEMIES['dr. haugen'])
        MAPS[1][6][0].placeItem(ITEMS["haugen's clothes"])
        

    if INTERACT['fridge'].quest and QUESTS['einstein fridge']:
        QUESTS['einstein fridge'] = 0
        
    

    #Semiconductor quests    
    if ENEMIES['dr. kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2].placeEnemy(ENEMIES['dr. kleimann'])
        QUESTS['kitai get silicon substrate'] = 0

    if ENEMIES['dr. kleimann'].quest and QUESTS["kleimann get solar cell"]:
        MAPS[3][3][1].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["kleimann get solar cell"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["minnick get oscilloscope"]:
        ENEMIES['dr. minnick'].quest = False
        ENEMIES['dr. minnick'].drop ='gauss eye' #this has to be lowercase or it throws a key error - All items are defined as lower case when stored
        ENEMIES['dr. minnick'].need = "faraday's cage" #this has to be lowercase or it throws a key error
        ENEMIES['dr. minnick'].info = "I need to complete Kenrick's design... use my glasses to find what we need!"
        ENEMIES['dr. minnick'].Sinfo = "'Great! Now we can open the window to the electronics world!'\nYou step back and watch as Dr. Minnick adds Faraday's Cage to the oscilloscope.\n'I do not know what this oracle will have to say.'\n'It is just my responsibiliy to give you access to their knowledge.'\nYour vision begins to go blurry as you hear a low whirr grow louder and Kenrick's oscilloscope glows with\nconsiderable intensity!\nYou are shocked as you open your eyes. It seems as if you were dropped into the set of 'Tron'.\nA figure approaches as your vision slowly returns.\nThe figure is revealled to be James Clerk Maxwell!\n'We have waited many years for your coming.'\n'You will be the one to determine the fate of this faculty.'\n'My quantum relic along with the two others will give you the power to have your ring returned to you.'\n'Once you have all three you will be able to access your ring from the statue of McMaster.'\n'Good luck.'"
        MAPS[3][3][1].removeEnemy(ENEMIES['dr. minnick'])
        MAPS[1][7][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["minnick get oscilloscope"] = 0

    if INTERACT['display case'] and QUESTS["get key to display case"]:
        QUESTS["get key to display case"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["maxwell portal"]:
        QUESTS['maxwell portal'] = 0

    #endgame

    if QUESTS['end game start'] and not(QUESTS["maxwell portal"] or QUESTS['einstein fridge'] or QUESTS["feynman mirror"]):
        MAPS[5][2][1].placeEnemy(ENEMIES['hooded man'])
        MAPS[5][2][1].lore = "You approach the statue and notice the mysterious Hooded Man beneath the tree.\nHe notices you approach and stops the incantation he was reciting.\nHe motions for you to come closer."
        MAPS[5][2][1].travelled = 1
        ENEMIES['hooded man'].info = "'I knew you could do it.'\n'I knew you were the one the prophecy spoke of.'\n'For too long the Quantum Order has kept me in isolation...'\n'They thought I was poisoning the minds of students and did not agree\nwith my methods.'\n'But now you have brought the Quantum Relics which will give me the power\nto shape the faculty as I see fit!'\nThe Hooded Man pulls back his hood to reveal the familiar face you only recall from legend!\nIt is Dr. Cassidy himself!"   
        QUESTS['end game start'] = 0

    if not QUESTS['end game start'] and ENEMIES['hooded man'].spoke and QUESTS['the dark lord']:
        MAPS[5][2][1].removeEnemy(ENEMIES['hooded man'])
        MAPS[5][2][1].placeEnemy(ENEMIES['dr. cassidy'])
        QUESTS['the dark lord'] = 0

    if ENEMIES['dr. cassidy'].spoke and QUESTS['university man']:
        MAPS[5][2][1].placeEnemy(ENEMIES['sir william mcmaster'])
        ENEMIES['dr. cassidy'].info = "Destroy Sir William McMaster and we can rule this university together!"
        QUESTS['university man'] = 0

    if not ENEMIES['sir william mcmaster'].alive and QUESTS['create chaos']:
        ENEMIES['dr. cassidy'].info = "Take the power you hold in your Iron Ring and destroy all of the professors!"
        DEATHS = [ENEMIES[i].alive for i in ['dr. minnick','dr. novog','dr. kitai','dr. knights','dr. preston','dr. kleimann','dr. buijs','dr. lapierre','dr. nagasaki']]
        if True in DEATHS:
            pass
        else:
            PLAYER.alive = False
            return 1
            
    elif not ENEMIES['dr. cassidy'].alive and QUESTS['restored order']:
        PLAYER.alive = False #does this so you can get out of the loop
        return 2

    else:
        return 0
        
        
def SpellCheck(Word,Psblties):
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
        

    
        
    


    
