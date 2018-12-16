from GameFunctions import *
import StartUp
from Opening import * #this imports the code and all the code dependancies (functions imported in that)

#If there was a title screen it would go here
#Version: Alpha v0.27 - 
#Updated: Dec 15, 2018

#Opening()

playername = raw_input("First, what is your name?\n")

print "========================================================================"

def Main():
    global PLAYER
    global ITEMS
    global MAPS
    global INTERACT
    global playername
    global QUESTS
    KEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys())
    VERBS =['search','stats','inventory','equip','drop','attack','talk','inspect','eat']
    
    PLAYER.name = playername
    if playername == "Tyler Kashak":
        print "\nYou are now playing as: THE MAN\n"
        PLAYER.health = 999
       
    x = 2
    y = 3
    z = 1
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z

    CurrentPlace = MAPS[x][y][z]
    print CurrentPlace.lore +"\n\n" + CurrentPlace.info + CurrentPlace.search()
    CurrentPlace.travelled = 0
    
    stepcount = 0   #these are speedrunning counters
    commandcount = 0
    timestart = time.time()
    print "Your time starts now!"
    while(PLAYER.alive):
        direction = raw_input('What do you want to do?\n').lower().split(" ",1)
        
        for i in range(len(direction)):
           direction[i] = direction[i].strip() #Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)


            if verb in ['u','d','l','r','f','b']:
                CurrentPlace = Move(verb)
                stepcount += 1 #increments the stepcount and then displays after you take a step
            elif (verb == 'search'):
                x = PLAYER.location[0]
                y = PLAYER.location[1]
                z = PLAYER.location[2]
                print MAPS[x][y][z].search()

            elif (verb == 'stats'):
                Stats()
                
            elif (verb == 'inventory'):
                Inventory()
            else:
               print "\nI don't understand that command!\n"

        elif (len(direction) == 2):
            verb = direction[0]
            if len(verb)>1:
                verb = SpellCheck(verb,VERBS)
            objectName = SpellCheck(direction[1],KEYS)

            if verb == 'equip':
                Equip(objectName)
                
            elif verb == 'drop':
                Drop(objectName)

            elif verb == 'attack':
                Attack(objectName)
                
            elif verb == 'talk':
                Talk(objectName)

            elif verb == 'inspect':
                Inspect(objectName)

            elif verb == 'eat':
                Eat(objectName)
            else:
               print "\nI don't understand that command!\n"

        commandcount += 1 #increments the command count after every command but doesn't print
        print "========================================================================"
        Story()

        
    timeend = time.time()
    runtime = timeend-timestart
    if Story()== 0:
        print "========================================================================"
        DisplayTime(runtime) #displays the runtime for speed running
        print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
        raw_input("Thanks for playing!! Better luck next time!")
    elif Story() == 1:
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing()
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
            DisplayTime(runtime)
            print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
            raw_input("Thanks for playing!!")
    elif Story() == 2:
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Closing()
            print "Having defeated Dr. Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
            DisplayTime(runtime)
            print "Total Step Count: ", stepcount, "\nTotal Command Count: ", commandcount
            raw_input("Thanks for playing!!")
Main()
