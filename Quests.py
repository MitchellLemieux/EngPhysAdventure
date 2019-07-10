#ENG PHYS TEXT  ADVENTURE
#Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
#Wrote on Mar  21,2019: 

from GameFunctions import * #importing the global dictionaries/values
import time
import Opening #used for the EPTA all the way down quest
import os #used to put files in the cache folder
import playsound #used to play music and sound effects

global QUESTS

#List of quests that then get's built into a dictionary
#it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
          #sidequests
          'secret spaces',
          'EPTA all the way down',
          #Talk to hooded man
          "talk to mysterious man",
          #Nuke
          "preston get dumbbell",
          "buijs kill chris",
          "dan fix reactor",
          "novog get donut",
          "feynman mirror",
          #Optics
          "kitai get silicon substrate",
          "knights get book",
          "haugen kill soleymani",
          "einstein fridge",
          #Semiconductor
          "lapierre get coffee",
          "kleimann get solar cell",
          "minnick get oscilloscope",
          "get key to display case",
          "maxwell portal",
          #endgame stuff
          'end game start',
          'the dark lord' ,
          'university man',
          'restored order',
          'create chaos'
          ]

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest:1})
    

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
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Secret.wav"), False) #plays the sound with 'multithreading'
        
    
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']: #when you put the pen in the laptop it restarts the game
    # TODO as homework see if there's a way to do this with recursion instead of simulating it
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
    
    # Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1].placeEnemy(ENEMIES["dr. kitai"])
        MAPS[2][4][2].placeEnemy(ENEMIES["dr. preston"])
        MAPS[1][6][2].placeEnemy(ENEMIES["dr. lapierre"])
        MAPS[5][4][1].removeEnemy(ENEMIES["hooded man"])
        ENEMIES['hooded man'].spoke = False
        QUESTS["talk to mysterious man"] = 0
        #small item
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Song_Correct.wav"), False)

    # Nuke quests
    if ENEMIES['dr. preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1].placeEnemy(ENEMIES["dr. buijs"])
        QUESTS["preston get dumbbell"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

        
    if ENEMIES['dr. buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0].placeEnemy(ENEMIES['dan fitzgreen'])
        ENEMIES['dan fitzgreen'].quest = True
        QUESTS['buijs kill chris'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dan fitzgreen'].spoke and INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        MAPS[2][6][0].placeEnemy(ENEMIES['dr. novog'])
        MAPS[4][5][0].placeEnemy(ENEMIES['stefan boltzmann'])
        QUESTS["dan fix reactor"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
        
    if ENEMIES['dr. novog'].quest and QUESTS["novog get donut"]:
        QUESTS['novog get donut'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if INTERACT['ancient mirror'].quest and QUESTS["feynman mirror"]:
        QUESTS["feynman mirror"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

    # Optics quests
    if ENEMIES['dr. lapierre'].quest and QUESTS["lapierre get coffee"]:
        MAPS[5][4][1].placeEnemy(ENEMIES['dr. knights'])
        QUESTS["lapierre get coffee"]= 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
        
    if ENEMIES['dr. knights'].quest and QUESTS["knights get book"]:
        MAPS[1][6][0].placeEnemy(ENEMIES['dr. haugen'])
        QUESTS["knights get book"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. haugen'].quest and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        ENEMIES['dr. haugen'].alive = False
        MAPS[1][6][0].removeEnemy(ENEMIES['dr. haugen'])
        MAPS[1][6][0].placeItem(ITEMS["haugen's clothes"])
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
        

    if INTERACT['fridge'].quest and QUESTS['einstein fridge']:
        QUESTS['einstein fridge'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

    # Semiconductor quests
    if ENEMIES['dr. kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2].placeEnemy(ENEMIES['dr. kleimann'])
        QUESTS['kitai get silicon substrate'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. kleimann'].quest and QUESTS["kleimann get solar cell"]:
        MAPS[3][4][1].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["kleimann get solar cell"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. minnick'].quest and QUESTS["minnick get oscilloscope"]:
        ENEMIES['dr. minnick'].quest = False
        ENEMIES['dr. minnick'].drop ='gauss eye' #this has to be lowercase or it throws a key error - All items are defined as lower case when stored
        ENEMIES['dr. minnick'].need = "faraday's cage" #this has to be lowercase or it throws a key error
        ENEMIES['dr. minnick'].info = "I need to complete Kenrick's design... use my glasses to find what we need!"
        ENEMIES['dr. minnick'].Sinfo = "'Great! Now we can open the window to the electronics world!'\nYou step back and watch as Dr. Minnick adds Faraday's Cage to the oscilloscope.\n'I do not know what this oracle will have to say.'\n'It is just my responsibiliy to give you access to their knowledge.'\nYour vision begins to go blurry as you hear a low whirr grow louder and Kenrick's oscilloscope glows with\nconsiderable intensity!\nYou are shocked as you open your eyes. It seems as if you were dropped into the set of 'Tron'.\nA figure approaches as your vision slowly returns.\nThe figure is revealled to be James Clerk Maxwell!\n'We have waited many years for your coming.'\n'You will be the one to determine the fate of this faculty.'\n'My quantum relic along with the two others will give you the power to have your ring returned to you.'\n'Once you have all three you will be able to access your ring from the statue of McMaster.'\n'Good luck.'"
        MAPS[3][4][1].removeEnemy(ENEMIES['dr. minnick'])
        MAPS[1][7][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["minnick get oscilloscope"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if INTERACT['display case'] and QUESTS["get key to display case"]:
        QUESTS["get key to display case"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["maxwell portal"]:
        QUESTS['maxwell portal'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

    # endgame

    if QUESTS['end game start'] and not(QUESTS["maxwell portal"] or QUESTS['einstein fridge'] or QUESTS["feynman mirror"]):
        MAPS[5][2][1].placeEnemy(ENEMIES['hooded man'])
        print "\nYou feel a strange pull towards the McMaster Statue.\n"
        MAPS[5][2][1].lore = "You approach the statue and notice the mysterious Hooded Man beneath the tree.\nHe notices you approach and stops the incantation he was reciting.\nHe motions for you to come closer."
        MAPS[5][2][1].travelled = 1
        ENEMIES['hooded man'].info = "'I knew you could do it.'\n'I knew you were the one the prophecy spoke of.'\n'For too long the Quantum Order has kept me in isolation...'\n'They thought I was poisoning the minds of students and did not agree\nwith my methods.'\n'But now you have brought the Quantum Relics which will give me the power\nto shape the faculty as I see fit!'\nThe Hooded Man pulls back his hood to reveal the familiar face you only recall from legend!\nIt is Dr. Cassidy himself!"   
        QUESTS['end game start'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if not QUESTS['end game start'] and ENEMIES['hooded man'].spoke and QUESTS['the dark lord']:
        MAPS[5][2][1].removeEnemy(ENEMIES['hooded man'])
        MAPS[5][2][1].placeEnemy(ENEMIES['dr. cassidy'])
        QUESTS['the dark lord'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. cassidy'].spoke and QUESTS['university man']:
        MAPS[5][2][1].placeEnemy(ENEMIES['sir william mcmaster'])
        ENEMIES['dr. cassidy'].info = "Destroy Sir William McMaster and we can rule this university together!"
        QUESTS['university man'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if not ENEMIES['sir william mcmaster'].alive and QUESTS['create chaos']:
        ENEMIES['dr. cassidy'].info = "Take the power you hold in your Iron Ring and destroy all of the professors!"
        DEATHS = [ENEMIES[i].alive for i in ['dr. minnick','dr. novog','dr. kitai','dr. knights','dr. preston','dr. kleimann','dr. buijs','dr. lapierre','dr. nagasaki']]
        if True in DEATHS:
            playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
            pass
        else:
            PLAYER.alive = False
            playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

            return 1
            
    elif not ENEMIES['dr. cassidy'].alive and QUESTS['restored order']:
        PLAYER.alive = False  # does this so you can get out of the main loop
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

        return 2

    else:
        return 0
