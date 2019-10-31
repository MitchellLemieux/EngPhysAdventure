import time
#import pygame
#from pygame import mixer
import playsound  # Used for openning sound and star wars openning
import os
import fnmatch  # Used to fins the savefiles and display them
import CreativeMode
from printT import *
import colorama  # Colour module, no bolding on windows :(
from colorama import Fore, Back, Style

colorama.init()
CLEARSCREEN = '\033[2J'  # This is the clearscreen variable
lightgreen = Fore.LIGHTGREEN_EX

from GameFunctions import GAMESETTINGS, GAMEINFO #imports these global variables to be used in the start screen


DELAY = 1.5
# TODO Implement these based on the size of the screen
LINEBREAK = "========================================================================" #standard display with 72 characters
#CLEARSCREEN = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" #35 newlines
#Graphics , audio, difficulty, modes, advanced
#screen width, default read speed/On/Off, suggestion for green
#music on/off, sound levels eventually?
#Eventually easy-medium-hardcore
#eventually speed run, hardcore mode, dev mode, iron man eventually
#all of the settings individually not grouped into modes
def StartScreen():
    global GAMEINFO
    global GAMESETTINGS
    print Fore.LIGHTGREEN_EX  # This sets all text color to light green

    if GAMESETTINGS['DevMode']:
        pass  # If in dev mode do nothing and skip intro
# The pass statement in Python is used when a statement is required syntactically but you do not want code to execute.
    else:
        # If no Dev Mode do the blip intro
        print CLEARSCREEN
        audiopath = os.path.join(os.getcwd(), "MediaAssets","","EFXstartup.mp3") #points to the eddited star wars theme
        playsound.playsound(audiopath, False) # plays the startup sound with 'multi-threading'
        print "                " + Fore.RED + "A" + lightgreen + "____ ________"
        print "                /_  H|\_____  \ "
        print "                 |  O|  ___|  |"
        print "                 |  L| /___   <"
        print "                 |  L|  ___\   |"
        print "                 |  Y| /W O O D|"
        print "                 |___|/________/"
        print "                      " +Fore.RED + "Production" + lightgreen + "."
        time.sleep(3)  # Delay for intro sound
        print CLEARSCREEN


    startmenu = True  # startmenu is the variable that keeps you in the startmenu screen loop

    if GAMESETTINGS['DevMode']:  # If in DevMode it skips the loading screen
        startmenu = False  # turning off loading screen

    while startmenu:
        print CLEARSCREEN
        print "       ___________                __________.__"
        print "       \_   _____/    _     _____ \______   \  |__ ___.__. ______"
        print "        |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/"
        print "        |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ "
        print "       /_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
        print "               \/     \//_____/  " + Fore.RED + "TEXT ADVENTURE" + Fore.LIGHTGREEN_EX +"  \/\/         \/ "
        print "                             Now with colour!"
        print "                    Version " +str(GAMEINFO['versionname'])
        print "                    Release Date: " + GAMEINFO['releasedate'] + "                    \n\n"
        print "Play New Game[P]  Load Game[L]   Settings[S]   Disclaimers[D]  Exit[E]"
        choice = raw_input('Choose what you want to do: ').lower()
        # Play new Game
        if choice in ['p', 'play new game','play']:
            startmenu = False

        # Loading Screen and Game
        # TODO Maybe add this loading screen to CreativeMode so you can load in-game
        elif choice in ['l', 'load game','load', 'loadgame']:
             loadscreen = True
             while loadscreen:
                print CLEARSCREEN
                print "Load Game\n"
                # print os.listdir(path)  # Gives a list of all files in the directory
                # This Gets and save files in the cache and stores in lists
                loadnumber = 0  # The loadfile display incrementer
                loadnumberlist = []  # list to store loadnumbers
                loadnamelist = []  # list to store loadname
                # Iterates through display string which has all files in the directory
                for file in os.listdir(GAMEINFO['savepath']):
                    if file == "SaveFile basegame.plp":  # ignores the basegame file
                        next
                    # Searches for the keyword in the files of the savefile directory
                    elif fnmatch.fnmatch(file, 'SaveFile*'):  # looks for files that have SaveFile in the Name
                        loadnumber += 1  # Itterates the loadnumber for the next one
                        # Saving load number as string so can compare Lchoice string later
                        loadnumberlist.append(str(loadnumber))
                        # For some reason strip is being dumb and have to strip "SaveFile" and the " " separately
                        loadnamelist.append(file.lstrip("SaveFile").strip().rstrip(".plp"))

                # Displays the save files was numbered list starting from 1
                for i in range(loadnumber):
                    print "[" + loadnumberlist[i] + "]" + loadnamelist[i]
                print "[B]Back\n"

                Lchoice = raw_input('Choose which game you want to load: ')
                if Lchoice in ['b', 'back', 'leave', 'exit']:  # if you choose back the loop exits
                    loadscreen = False

                elif Lchoice in loadnamelist:  # if user enters loadname
                    loadscreen = False
                    startmenu = False
                    CreativeMode.loadGame(Lchoice)  # loads in the savefile global variables
                    GAMESETTINGS['loadgame'] = 1  # Sets this flag so the rest of setup is skipped and goes to main
                    GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
                    print CLEARSCREEN
                elif Lchoice in loadnumberlist:  # if user enters loadnumber has to lookup the load name
                    loadscreen = False
                    startmenu = False
                    CreativeMode.loadGame(loadnamelist[int(Lchoice)-1])  # converts loadnumber to loadgame index
                    GAMESETTINGS['loadgame'] = 1  # Sets this flag so the rest of setup is skipped and goes to main
                    GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time

                else:
                    print "\nPlease choose one of the options."

        # Setting Screen
        elif choice in ['s', 'settings','setting']:
            settingscreen = True
            while(settingscreen):
                print CLEARSCREEN
                # TODO Make a DEV mode that disables error catching and enables creative

                print "Settings\n*These may change if you load a previous game\n\n"
                print '[0]Disable Opening:  ' + str(GAMESETTINGS['DisableOpening'])
                print '[1]Speed Run:        ' + str(GAMESETTINGS['SpeedRun'])
                print '[2]Hardcore Mode:    ' + str(GAMESETTINGS['HardcoreMode'])
                print '[B]Back\n '

                Schoice = raw_input('Choose which settings you want to toggle: ').lower()
                if Schoice in ['b', 'back', 'leave', 'exit']:
                    settingscreen = False
                elif Schoice =='0':
                    # Have to make sure the values toggle to 0 and 1 not true and false for saving
                    GAMESETTINGS['DisableOpening'] = int(not(GAMESETTINGS['DisableOpening']))
                    # print "Hi I'm a dog"
                elif Schoice =='1':
                    GAMESETTINGS['SpeedRun'] = int(not(GAMESETTINGS['SpeedRun']))
                elif Schoice =='2':
                    GAMESETTINGS['HardcoreMode'] = int(not(GAMESETTINGS['HardcoreMode']))
                elif Schoice == '/420e69':  # Character that enables DevMode
                    GAMESETTINGS['DevMode'] = int(not(GAMESETTINGS['DevMode']))
                    # Prints throw-off style text while still giving the stat
                    print "\nPlease choose " + str(GAMESETTINGS['DevMode']) + "one of the options."
                else:
                    print "\nPlease choose one of the options."
            # Saving Settings Once out of the screen, These setting should be readable and changeable by a person

            f = open("settings.ini", "w+")
            for setting in GAMESETTINGS:
        # TODO Before release uncomment this line so DevMode isn't saved. DevMode in setting file is not for RELEASE
                #if setting == "DevMode": continue
                f.write(setting + "\n" + str(GAMESETTINGS[setting]) + "\n")
            f.close()

        # Disclaimer screen
        elif choice in ['d', 'disclaimers','disclaimer']:
            print CLEARSCREEN

            printT("Disclaimer (\S) (\S) This game is difficult, requires reading and focus on every piece of text, "
                   "and awareness of small details in order to advance the game. We feel here that we're trying to "
                   "provide an experience that's challenging but rewarding, not punishing. That being said we are "
                   "always open to feedback.(\S) This game is a work in progress and there may be bugs. We do our best "
                   "to avoid, catch, and fix errors promptly. If you do come across one however please submit them to "
                   "our bug response form: https://goo.gl/forms/Jo6P7oMj86OiLvE63 (\S) This is a work of fiction. "
                   "Names, characters, businesses, places, events, locales, and incidents are either the products of "
                   "the author's imagination or used in a fictitious manner. Any resemblance to actual persons, living "
                   "or dead, or actual events is purely coincidental. By playing this game you give up the right to"
                   "any information or files uploaded to the developers for benevolent development of the game.",72,0)
            raw_input("\nHit enter to continue")
        # Exiting
        elif choice in ['e', 'exit','leave']: 
            exit()
        else:
            print "\nPlease choose one of the starting options."

def Opening():
    #IT WORKS!
    audiopath = os.path.join(os.getcwd(), "MediaAssets","","StarWarsOpenningFadeOut.mp3") #points to the eddited star wars theme
    playsound.playsound(audiopath, False) #plays the sound with 'multithreading'
    time.sleep(0.5)
    print CLEARSCREEN
    print "                A____ ________"
    print "                /_  H|\_____  \ "
    print "                 |  O|  ___|  |"
    print "                 |  L| /___   <"
    print "                 |  L|  ___\   |"
    print "                 |  Y| /W O O D|"
    print "                 |___|/________/"
    print "                      Production."
    time.sleep(3.5) #4 seconds
    print CLEARSCREEN
    print ""
    print "         A short time ago on a campus not so far,"
    print "         far away....\n"
    time.sleep(3) #5.5 seconds
    print CLEARSCREEN
    print 
    print "___________                __________.__"                 
    print "\_   _____/ THE_GREAT_____ \______   \  |__ ___.__. ______"
    print " |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/"
    print " |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ "
    print "/_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
    print "        \/     \//_____/  TEXT ADVENTURE  \/\/ (v4.20) \/ "
    time.sleep(7.5)
    print ""
    print "T h e  c a m p u s  i s  i n  a  s t a t e  o f  u n r e s t."
    time.sleep(DELAY)
    print "A n  a n c i e n t  f o r c e  h a s  b e e n  a w o k e n"
    time.sleep(DELAY)
    print "a f t e r  t h e  e v e n t s  o f  a  d e b a u c h e r o u s"
    time.sleep(DELAY)
    print "e v e n i n g  a t  t h e  P h o e n i x.\n"
    time.sleep(DELAY*2)
    print "T h e  h e r o  a w a k e n s  i n  f r o n t  o f  J H E"
    time.sleep(DELAY)
    print "w i t h  a  c o n s i d e r a b l e  h e a d a c h e  b u t"
    time.sleep(DELAY)
    print "w i t h o u t  t h e i r  I R O N  R I N G.\n"
    time.sleep(DELAY*2)
    print "C l u e s  a b o u t  l a s t  n i g h t  l i t t e r  t h e"
    time.sleep(DELAY)
    print "c a m p u s.  N o  s t o n e  c a n  b e  l e f t  u n t u r n e d."
    time.sleep(DELAY)
    print "I t  w i l l  t r u l y  b e  a  t e s t  o f  s k i l l  a s"
    time.sleep(DELAY)
    print "w e l l  a s  w i t s  t o  s o l v e  t h i s  m y s t e r y.\n"
    time.sleep(DELAY*2)
    print "T h e  h e r o  m u s t  u n c o v e r  t h e  t r u t h"
    time.sleep(DELAY)
    print "a b o u t  l a s t  n i g h t  i f  t h e y  a r e  t o"
    time.sleep(DELAY)
    print "h a v e  a n y  h o p e  o f  r e t r i e v i n g  t h e i r"
    time.sleep(DELAY)
    print "I R O N  R I N G  a n d  r e t u r n i n g  b a l a n c e"
    time.sleep(DELAY)
    print "t o  t h e  f a c u l t y.\n"
    time.sleep(DELAY)
    print CLEARSCREEN
    # for i in range(14):
    #     print "\n"
    #     time.sleep(DELAY/2)

def Closing():
    print "And so, the fate of McMaster has been decided..."
    time.sleep(DELAY)
    print "Our hero has unlocked the secrets of McMaster University"
    time.sleep(DELAY)
    print "and lived to tell the tale.\n"
    time.sleep(DELAY)
    print "          THE GREAT ENG PHYS TEXT ADVENTURE\n"
    time.sleep(DELAY)
    print "Created by:\nMitchell Lemieux, Tyler Kashak, and Brendan Fallon\n"
    time.sleep(DELAY)
    print "Special Thanks:\nEric, Erik, Brian, Phil, and Megan\n"
    time.sleep(DELAY)
    print "                A____ ________"
    print "                /_  H|\_____  \ "
    print "                 |  O|  ___|  |"
    print "                 |  L| /___   <"
    print "                 |  L|  ___\   |"
    print "                 |  Y| /W O O D|"
    print "                 |___|/________/"
    print "                      Production."
    time.sleep(2)
    printT("This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are "
           "either the products of the author's imagination or used in a fictitious manner. Any resemblance to actual "
           "persons, living or dead, or actual events is purely coincidental. (\S)",72,0)
    time.sleep(2)
    print "___________                __________.__"                 
    print "\_   _____/ THE_GREAT_____ \______   \  |__ ___.__. ______"
    print " |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/"
    print " |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ "
    print "/_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
    print "        \/     \//_____/  TEXT ADVENTURE  \/\/ (v4.20) \/ \n"
    time.sleep(2)







#This works great but doesn't compile with displaying text. I got it to compile
#   pygame2exe but doesn't show any text in the exe so might need to use pygame
#   which would be dumb. Can get i
####mixer.init()
####mixer.music.load("StarWarsOpenningFadeOut.mp3")
####mixer.music.play()
####time.sleep(0.2) #needs this delay before the next comand?
####Opening()
####mixer.music.stop()
####mixer.music.load("ErikBeepBox-Song.wav")
####mixer.music.play()
####time.sleep(10)
####mixer.music.stop()

###Trying to make a pygame screen
###https://www.youtube.com/watch?v=gTvVDJofGdI
###creating basic window
##pygame.init() #initializes modules of pygame
##screen = pygame.display.set_mode((600,500)) #making a screen object with that pixel dimensions
##myfont = pygame.font.SysFont("Arial",12)
##done = False
##while not done:
##    for event in pygame.event.get(): #basic window with object
##        if event.type==pygame.QUIT:
##            done = True
##    text1 = myfont.render("Text",1,(0,255,0)) #makes the object attributes
##    screen.blit(text1, (400,10)) #adds font to the screen
##    pygame.draw.rect(screen,(255,0,0),pygame.Rect(100,100,100,100)) #draws a rectangle, 3 args screen object, colour, and 
##    pygame.display.update()


