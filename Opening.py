import time
#import pygame
#from pygame import mixer
import playsound
import os
from GameFunctions import GAMESETTINGS, GAMEINFO #imports these global variables to be used in the start screen


DELAY = 1.5

LINEBREAK = "========================================================================" #standard display with 72 characters
CLEARSCREEN = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" #35 newlines

def StartScreen():
    global GAMEINFO
    global GAMESETTINGS
    audiopath = os.path.join(os.getcwd(), "MediaAssets","","EFXstartup.mp3") #points to the eddited star wars theme
    playsound.playsound(audiopath, False) #plays the sound with 'multithreading'
    print "                A____ ________"
    print "                /_  H|\_____  \ "
    print "                 |  O|  ___|  |"
    print "                 |  L| /___   <"
    print "                 |  L|  ___\   |"
    print "                 |  Y| /W O O D|"
    print "                 |___|/________/"
    print "                      Production."
    time.sleep(3)
    print CLEARSCREEN
    start = True
    while(start):
        print LINEBREAK
        print "___________                __________.__"                 
        print "\_   _____/    _     _____ \______   \  |__ ___.__. ______"
        print " |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/"
        print " |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ "
        print "/_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
        print "        \/     \//_____/  TEXT ADVENTURE  \/\/         \/ "
        print "                    Version Alpha " +str(GAMEINFO['version']) + "                    \n\n"
        print "Play New Game[P]   Settings[S]  Disclaimers[D]   Exit[E]  "
        #TODO add load game functionality
        #print "Play New Game[p]   Load Game[L]    Settings[S]   Exit[E]  "      
        choice = raw_input('Choose what you want to do: ').lower()
        if choice in ['p', 'play new game','play']:
            start = False
##        elif choice in ['l', 'load game','load']:
##            print linebreak
##            print "Load Game\n\n"
        
        elif choice in ['s', 'settings','setting']:
            settingscreen = True
            while(settingscreen):
                print LINEBREAK
                print "Settings\n\n[0]Disable Opening:  "+ str(int(GAMESETTINGS['DisableOpening']))+'\n[1]Speed Run:        ' + str(int(GAMESETTINGS['SpeedRun'])) +'\n[2]Hardcore Mode:    ' + str(int(GAMESETTINGS['HardcoreMode'])) +'\n[3]Disable Music:    ' + str(int(GAMESETTINGS['DisableMusic'])) +'\n[B]Back '
                Schoice = raw_input('Choose which settings you want to toggle: ').lower()
                if Schoice in ['b', 'back', 'leave', 'exit']:
                    settingscreen = False
                elif Schoice =='0':
                    GAMESETTINGS['DisableOpening'] = not(GAMESETTINGS['DisableOpening'])
                elif Schoice =='1':
                    GAMESETTINGS['SpeedRun'] = not(GAMESETTINGS['SpeedRun'])
                elif Schoice =='2':
                    GAMESETTINGS['HardcoreMode'] = not(GAMESETTINGS['HardcoreMode'])
                elif Schoice =='3':
                    GAMESETTINGS['DisableMusic'] = not(GAMESETTINGS['DisableMusic'])                   
                else:
                    print "\nPlease choose one of the options."
        elif choice in ['d', 'disclaimers','disclaimer']:
            print LINEBREAK
            print "Disclaimer\n\nThis game is difficult, requires reading and focus on every piece of text, and awareness of small details in order to advance the game.\n\n"
            print "We feel here that we're trying to provide an experience that's challenging but rewarding, not punishing. That being said we are always open to feedback.\n\n"
            print "This game is a work in progress and there may be bugs. We do our best to avoid, catch, and fix errors promptly. If you do come across one however please submit them to our bug response form:\n\n"
            print "This is a work of fiction. Names, characters, businesses, places, events, locales, and incidents are either the products of the author's imagination or used in a fictitious manner. Any resemblance to actual persons, living or dead, or actual events is purely coincidental.\n\n"
            print "By playing this game you give up the right to any information or files uploaded to the developers for benevolent development of the game.\n\n"

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
    for i in range(14):
        print "\n"
        time.sleep(DELAY/2)

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
    print "This is a work of fiction. Names, characters, businesses, places, events,'nlocales, and incidents are either the products of the author's imagination\nor used in a fictitious manner. Any resemblance\nto actual persons, living or dead, or actual events is\npurely coincidental.\n\n"
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


