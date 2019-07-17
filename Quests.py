# ENG PHYS TEXT  ADVENTURE
# Mitchell Lemieux, Tyler Kashak, and Brendan Fallon
# Wrote on Mar  21,2019:
"""
This Quests.py file is used to write the story, quests, and events of the game by changing objects based on conditions.
EngPhysStory() is the main Eng Phys storyline  and returns once its finished
Quests generally only happen once and are sidequests unrelated to the storyline that do something special
Events are reoccurring based on the condition for the game

"""
# TODO Maybe split up these funcions into seperate files

from GameFunctions import * #importing the global dictionaries/values
import time
import Opening #used for the EPTA all the way down quest
import os #used to put files in the cache folder
import playsound #used to play music and sound effects
import AsciiArt

global QUESTS

# List of quests and storylines that then get's built into a dictionary
# This dictionary is just flags to keep track of quest completion to advance or end quests
# it's defined here for convience of working but is dealing with a global variable defined in gamefunctions

questlist = [
          #sidequests
          'secret spaces',
          'EPTA all the way down',
          #Events
          'PAP',
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
          # PHILpocalypse  # After you give Phil is braces he sobers up and becomes tired Phil.
          # After he asks for a coffee "Man I could really use a coffee but I don't want to spend the money
          # if you give him coffee he gives you a free wish "OH YEAH I AM CAFFINATED. I feel like I can do anyhing!"
          # If you give him a cappuccino the PHILpocalypse storyline begins:
          # You see his eyes dilate "OH YEAH I"M FEELING GREAT", He snaps his fingers and there's a flash.
          # You wake in JHE field "Not again" and everyone on the map is gone. Eventually you meet a Phil clone
          ]

# building the quest dictionary because you can't just overwrite the dumb dictionaries for some dumb reason
for quest in questlist:
    QUESTS.update({quest:1})

def sidequests():
    global PLAYER
    global QUESTS
    global ITEMS
    global ENEMIES
    global INTERACT
    global MAPS
    # Side Quests
    # Secret Spaces
    if INTERACT['coat of arms'].quest and QUESTS["secret spaces"]:  # Unlocks the secret space once you get the scroll
        MAPS[0][2][1][0].removeWall("d")
        QUESTS["secret spaces"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets", "", "OOT_Secret.wav"),
                            False)  # plays the sound with 'multithreading'

    # EBTA All the way Down
    # when you put the pen in the laptop it opens the thing
    if INTERACT["lenovo laptop"].quest and QUESTS['EPTA all the way down']:
        # TODO as homework see if there's a way to do this with recursion instead of simulating it
        # TODO put drums here
        playgame = raw_input(
            '========================================================================\nWould you like to play? \n').lower()
        if playgame == "yes" or playgame == "y":
            print "You click on the game and it begins in the terminal. The drumming \nintensifies. You're not sure if you made the right choice.\n========================================================================\n\n\n"
            import \
                CreativeMode  # this is imported here not at the top to avoid recursive import errors (show up as global names not being defined in the compiler
            QUESTS[
                'EPTA all the way down'] = 0  # Truns off the quest, has to be before the game saves so the quest is ended when you come back
            CreativeMode.saveGame(str(GAMEINFO['layersdeep']))  # saving game to be reloaded after death or won the game
            log = GAMEINFO['log']  # keeps the log as a temporary variable to keep a running log in the nested game
            Opening.Opening()
            newplayername = raw_input("First, what is your name?\n")
            layers = GAMEINFO['layersdeep']  # saves layersdeep to a temporary variable for after the load
            CreativeMode.loadGame("basegame")  # should display the exact start
            GAMEINFO[
                'layersdeep'] = layers + 1  # increments the global layers deep because you're now in a lower level, using the memory of the local variable

            GAMEINFO['playername'] = PLAYER.name = newplayername  # this is done for the log
            GAMEINFO['gamestart'] = time.time()  # Settign the game and timestart for for this layer
            GAMEINFO['timestart'] = GAMEINFO['gamestart']
            # Passes the log and adds onto it to keep a HUGE running log (TODO Make this more effecient with log appending)
            GAMEINFO['log'] = log + [str(playgame), "--NESTED GAME--", GAMEINFO['layersdeep'], GAMEINFO['versionname'],
                                     GAMEINFO['playername'], time.ctime(GAMEINFO['timestart']),
                                     "--LOG START--"]  # log list is a list that keeps track of player movements for game debugging. Each ellement of the list is written in a new line to the log file when the game ends or is saved.
        elif playgame == "no" or playgame == "n":
            print "You decide against it, fearing the worst. You safely edject the pen, \ndrop it on the floor, and smash it to pieces. Better safe than sorry.\nThe drumming stops.\n========================================================================"
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log
        else:
            print "It was a yes or no question. When you look back the files are gone.\nEven flexpde. Good riddance.\n========================================================================"
            QUESTS['EPTA all the way down'] = 0
            GAMEINFO['log'] += [str(playgame)]  # adds your command to the log

def ebta_story():
    global PLAYER
    global QUESTS
    global ITEMS
    global ENEMIES
    global INTERACT
    global MAPS

    
    # Talk to hooded man
    if ENEMIES['hooded man'].spoke and QUESTS["talk to mysterious man"]:
        MAPS[4][4][1][0].placeEnemy(ENEMIES["dr. kitai"])
        MAPS[2][4][2][0].placeEnemy(ENEMIES["dr. preston"])
        MAPS[1][6][2][0].placeEnemy(ENEMIES["dr. lapierre"])
        MAPS[5][4][1][0].removeEnemy(ENEMIES["hooded man"])
        ENEMIES['hooded man'].spoke = False
        QUESTS["talk to mysterious man"] = 0
        #small item
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Song_Correct.wav"), False)

    # Nuke quests
    if ENEMIES['dr. preston'].quest and QUESTS["preston get dumbbell"]:
        MAPS[2][5][1][0].placeEnemy(ENEMIES["dr. buijs"])
        QUESTS["preston get dumbbell"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

        
    if ENEMIES['dr. buijs'].quest and QUESTS['buijs kill chris']:
        MAPS[2][5][0][0].placeEnemy(ENEMIES['dan fitzgreen'])
        ENEMIES['dan fitzgreen'].quest = True
        QUESTS['buijs kill chris'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dan fitzgreen'].spoke and INTERACT['broken reactor'].quest and QUESTS["dan fix reactor"]:
        MAPS[2][6][0][0].placeEnemy(ENEMIES['dr. novog'])
        MAPS[4][5][0][0].placeEnemy(ENEMIES['stefan boltzmann'])
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
        MAPS[5][4][1][0].placeEnemy(ENEMIES['dr. knights'])
        QUESTS["lapierre get coffee"]= 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
        
    if ENEMIES['dr. knights'].quest and QUESTS["knights get book"]:
        MAPS[1][6][0][0].placeEnemy(ENEMIES['dr. haugen'])
        QUESTS["knights get book"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. haugen'].quest and QUESTS['haugen kill soleymani']:
        QUESTS['haugen kill soleymani'] = 0
        ENEMIES['dr. haugen'].alive = False
        MAPS[1][6][0][0].removeEnemy(ENEMIES['dr. haugen'])
        MAPS[1][6][0][0].placeItem(ITEMS["haugen's clothes"])
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)
        

    if INTERACT['fridge'].quest and QUESTS['einstein fridge']:
        QUESTS['einstein fridge'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

    # Semiconductor quests
    if ENEMIES['dr. kitai'].quest and QUESTS['kitai get silicon substrate']:
        MAPS[1][5][2][0].placeEnemy(ENEMIES['dr. kleimann'])
        QUESTS['kitai get silicon substrate'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. kleimann'].quest and QUESTS["kleimann get solar cell"]:
        MAPS[3][4][1][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["kleimann get solar cell"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    # Minnick's Glasses activate the need quest in all further items. So quest is driven by interacts from here
    if ENEMIES['dr. minnick'].quest and QUESTS["minnick get oscilloscope"]:
        ENEMIES['dr. minnick'].quest = False
        ENEMIES['dr. minnick'].drop = 'gauss eye' #this has to be lowercase or it throws a key error - All items are defined as lower case when stored
        ENEMIES['dr. minnick'].need = "faraday's cage" #this has to be lowercase or it throws a key error
        ENEMIES['dr. minnick'].info = "I need to complete Kenrick's design... use my glasses to find what we need!"
        ENEMIES['dr. minnick'].Sinfo = "'Great! Now we can open the window to the electronics world!'\nYou step back and watch as Dr. Minnick adds Faraday's Cage to the oscilloscope.\n'I do not know what this oracle will have to say.'\n'It is just my responsibiliy to give you access to their knowledge.'\nYour vision begins to go blurry as you hear a low whirr grow louder and Kenrick's oscilloscope glows with\nconsiderable intensity!\nYou are shocked as you open your eyes. It seems as if you were dropped into the set of 'Tron'.\nA figure approaches as your vision slowly returns.\nThe figure is revealled to be James Clerk Maxwell!\n'We have waited many years for your coming.'\n'You will be the one to determine the fate of this faculty.'\n'My quantum relic along with the two others will give you the power to have your ring returned to you.'\n'Once you have all three you will be able to access your ring from the statue of McMaster.'\n'Good luck.'"
        MAPS[3][4][1][0].removeEnemy(ENEMIES['dr. minnick'])
        MAPS[1][7][0][0].placeEnemy(ENEMIES['dr. minnick'])
        QUESTS["minnick get oscilloscope"] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if INTERACT['display case'] and QUESTS["get key to display case"]:
        QUESTS["get key to display case"] = 0

    if ENEMIES['dr. minnick'].quest and QUESTS["maxwell portal"]:
        QUESTS['maxwell portal'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_HeartContainer.wav"), False)

    # endgame

    if QUESTS['end game start'] and not(QUESTS["maxwell portal"] or QUESTS['einstein fridge'] or QUESTS["feynman mirror"]):
        MAPS[5][2][1][0].placeEnemy(ENEMIES['hooded man'])
        print "\nYou feel a strange pull towards the McMaster Statue.\n"
        MAPS[5][2][1][0].lore = "You approach the statue and notice the mysterious Hooded Man beneath the tree.\nHe notices you approach and stops the incantation he was reciting.\nHe motions for you to come closer."
        MAPS[5][2][1][0].travelled = 1
        ENEMIES['hooded man'].info = "'I knew you could do it.'\n'I knew you were the one the prophecy spoke of.'\n'For too long the Quantum Order has kept me in isolation...'\n'They thought I was poisoning the minds of students and did not agree\nwith my methods.'\n'But now you have brought the Quantum Relics which will give me the power\nto shape the faculty as I see fit!'\nThe Hooded Man pulls back his hood to reveal the familiar face you only recall from legend!\nIt is Dr. Cassidy himself!"   
        QUESTS['end game start'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if not QUESTS['end game start'] and ENEMIES['hooded man'].spoke and QUESTS['the dark lord']:
        MAPS[5][2][1][0].removeEnemy(ENEMIES['hooded man'])
        MAPS[5][2][1][0].placeEnemy(ENEMIES['dr. cassidy'])
        QUESTS['the dark lord'] = 0
        playsound.playsound(os.path.join(os.getcwd(), "MediaAssets","","OOT_Fanfare_Item.wav"), False)

    if ENEMIES['dr. cassidy'].spoke and QUESTS['university man']:
        MAPS[5][2][1][0].placeEnemy(ENEMIES['sir william mcmaster'])
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

def events():
    global PLAYER
    global QUESTS
    global ITEMS
    global ENEMIES
    global INTERACT
    global MAPS

    # PAP Event
    # TODO Make time not GMT so it doesn't matter which time zone you're in
    insttime = time.gmtime(time.time() - 4*60*60 )  # Used to debug and test the time based events by adding timer
    print time.asctime(insttime)  # Prints out the ascci time to debug
    #insttime = time.localtime()  # Instantaneous struct_time object at the time of reading

    # Thunder, cowboys, Bell, PAP sound

    # Simulated times to trigger the event, based on seconds from Epoch

    # gmtenthirty = gmfourtwenty + 6 * 60 * 60 + 10 * 60  # 10:30pm
    # insttime = time.gmtime(gmtenthirty)     # 10:30pm time object
    # TODO Make it so if you Do all intractables + (even empty ones) + Quests after winning the game you unlock PAP
    if INTERACT['red book'].quest == True:
        gmfourtwenty = 1562765901.005 + 24240 - 141 - (4*60*60)  # 4:20pm, Subtracting the 4 hours for gm time
        insttime = time.gmtime(gmfourtwenty)  # 4:20pm time object
    if INTERACT['blue book'].quest == True:
        insttime = time.localtime()  # Instantaneous struct_time object at the time of reading



    LINEBREAK = "========================================================================"  # standard display with 72 characters

    # Setting up the Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if insttime.tm_hour == 4 or insttime.tm_hour == 16 and insttime.tm_min == 20 and QUESTS["PAP"]:
        QUESTS["PAP"] = 0
        # Signaling Event, depends whether you're inside or outside
        print "A Bolt of lightening strikes the top of JHE"
        # TODO make this an interior after so you decide to go in
        MAPS[2][4][3][0].info = "~?~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "As you reach the top of the stairs you can feel the heat intensify. " \
"Where the way was blocked before is a melted hole just big enough for you to fit through. You expect to enter the " \
"hallway but see all the interior walls have been removed. All that remains are stone walls and boarded up windows. " \
"Textbooks and broken lab equipment litter the ground. You turn the corner to the lecture hall where you would " \
"fall asleep in 8:30 1D04 lecture. Glowing red hot in the centre of the room is the Pack-a-Punch Machine! " \
"(\S) (\S) Enscribed on the side in graffiti is 'BLAZE IT'."
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].placeInteract(INTERACT["pack-a-punch"])
    # Event Main Activity "Pack-a-Punching" when you inspect the machine
    elif (PLAYER.location == list(INTERACT["pack-a-punch"].location)) and INTERACT["pack-a-punch"].quest:
        PAPScreen = True
        upgradechoice = 0
        sacrificechoice = 0
        while PAPScreen:
            print LINEBREAK
            AsciiArt.PackScreen()
            # Displaying Options
            if upgradechoice == 0: print "Item 1: Choose an Item to Upgrade"
            else: print "Item 2: Choose an Item to Sacrifice"
            k = 0
            for i in PLAYER.inv:
                if PLAYER.inv[i].name == EMPTYINV[i].name:  # skips empty items
                    #print "THIS B**** EMPTY - YEET"
                    continue  # advance to the next i

                k += 1
                if (k != int(upgradechoice)):
                    print "[" + str(k) + "]" + PLAYER.inv[i].name + " " + str(PLAYER.inv[i].stats)
            print "[" + str(k+1) + "]Back\n"
            # Input and Check Input
            try:
                if upgradechoice == 0:
                    upgradechoice = input('Choose the number of the item you want to Pack-a-Punch: ')
                    if upgradechoice <= 0 or upgradechoice > k+1:
                        print "Please enter a valid option."
                        upgradechoice = 0
                else:
                    sacrificechoice = input('Choose the number of the item you want to sacrifice: ')
                    if sacrificechoice <= 0 or sacrificechoice > k+1:
                        print "Please enter a valid option."
                        sacrificechoice = 0
                    elif upgradechoice == sacrificechoice:
                        print "Please enter a valid option"
                        sacrificechoice = 0

            except:
                print "Please input a number selection"

            # Back Options Options
            if upgradechoice == k+1:  # if you choose back on upgrade choice screen the loop exits
                PAPScreen = False  # Break the loop to exit it
            elif sacrificechoice == k+1:  # if you choice back on sacrifice screen it resets to screen 1
                upgradechoice = 0
                sacrificechoice = 0

            # PAP Operation
            if (0 < upgradechoice < k+1) and (0 < sacrificechoice < k+1):
                PAPScreen = False

                # Getting the item objects
                k = 0
                for i in PLAYER.inv:
                    if PLAYER.inv[i].name == EMPTYINV[i].name:  # skips empty items
                        # print "THIS B**** EMPTY - YEET"
                        continue  # advance to the next i
                    k += 1
                    if k == upgradechoice:
                        upgrade = PLAYER.inv[i]  # copying the object to a temp variable
                    elif k == sacrificechoice:
                        sacrifice = PLAYER.inv[i]  # copying object to a temp variable

                if raw_input("Upgrading: " + upgrade.name + "\nSacrificing: " + sacrifice.name + "\n\nThis cannot be undone. \nType Y if this is correct:").lower() in ["y", 'yes', '1']:
                    1+1  # do nothing
                else:  # goes back to the loop and start again
                    break
                    upgradechoice = 0
                    sacrificechoice = 0
                # Dropping the items
                PLAYER.drop(upgrade)  # Item is removed from the player
                PLAYER.drop(sacrifice)  # Item is removed from the player
                # Upgrading the one item based on the sacrifice
                print "The Machine Reads: 'Pack-a-Punching Please Wait'"
                upgrade.name = "Better " + upgrade.name  # Adding Better to left side of name each time it's upgraded
                sumUStats = upgrade.stats[0] + upgrade.stats[1] + upgrade.stats[2]  # taking the sum of the stats of each item
                sumSStats = sacrifice.stats[0] + sacrifice.stats[1] + sacrifice.stats[2]
                # Sum of item stats of sacrifice has to be 1/10th that of the PAP item to double or add (whichever is better), or else they just add
                if sumUStats/10 <= sumSStats:
                    # Doubling stats of the item
                    if sumUStats + sumSStats > sumUStats*2:
                        upgrade.stats = (upgrade.stats[0] + sacrifice.stats[0], upgrade.stats[1] + sacrifice.stats[1],
                                         upgrade.stats[2] + sacrifice.stats[2])  # replacing stats tuple with sum
                    else:
                        upgrade.stats = (upgrade.stats[0]*2, upgrade.stats[1]*2, upgrade.stats[2]*2)  #replacing stats tuple with doubling them
                else:
                    # Adding the Stats
                    upgrade.stats = (upgrade.stats[0]+sacrifice.stats[0], upgrade.stats[1]+sacrifice.stats[1], upgrade.stats[2]+sacrifice.stats[2])  #replacing stats tuple

                MAPS[2][4][3][0].placeItem(upgrade)   # Placing the Upgraded Item on the ground
                print "The Pack-a-Punch wirls and screaches, glowing bright, before spitting out the " + upgrade.name + " onto the ground!"
                # TODO add pack-a-punch sound




        # Resetting quest flag so you don't always inspect it once you enter the room
        INTERACT["pack-a-punch"].quest = False



    # Resetting the Event
    elif (QUESTS["PAP"] == 0) and (not(PLAYER.location == (2,4,3,0))) and (not(insttime.tm_min == 20)):
        QUESTS["PAP"] = 1
        print "DONT BLAZE IT"
        MAPS[2][4][3][0].info = "~3RD FLOOR JHE Stairs~:\nYou can only go back down the stairs."
        MAPS[2][4][3][0].lore = "You see solid block of sheet metal covering the door. Was it always this way?"
        MAPS[2][4][3][0].travelled = 1
        MAPS[2][4][3][0].removeInteract(INTERACT["pack-a-punch"])

    # TENThirty Event
    # If time object hour is 4am or 4pm and the minute is 20 (so lasting 1 minute)
    if insttime.tm_hour == 10 or insttime.tm_hour == 22 and insttime.tm_min == 30:
        if not(PLAYER.inv['body'] == EMPTYBODY):  # If  your body isn't empty
            print "10:30 NO SHIRTY"
            print "You feel compelled to take your shirt off and drop it on the ground"
            # Drops the item you have on you, don't forget it has to be name of the item and lowercase.
            # Also can't be PLAYER.drop function because then it doesn't go onto the ground
            Drop(PLAYER.inv['body'].name.lower())








    # Killcount counter in player will trigger the police eventually
