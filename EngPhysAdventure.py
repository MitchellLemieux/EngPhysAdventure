from GameFunctions import *
import StartUp
import Opening

print "========================================================================"
print "Hello, and welcome to..."
print "___________ THE GREAT      __________.__"                 
print "\_   _____/ ____    ______ \______   \  |__ ___.__. ______"
print " |    __)_ /    \  / ___  > |     ___/  |  \   |  |/  ___/"
print " |        \   |  \/ /_/  /  |    |   |      \___  |\___ \ "
print "/_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
print "        \/     \//_____/  TEXT ADVENTURE  \/\/ (v4.20) \/ "
print "A campus full of interesting characters awaits"
print "Created by: Mitchell Lemieux & Tyler Kashak"
print "Special thanks to Erik, Eric, Megan, Brian, and Brendan <3\n"
print "Before you go any further there are some things you must know..."
print "Your orientation never changes. When you enter you will be facing the"
print "entrance of JHE and you will always face that way.\n"
print "The commands which allow you to interact with your environment are:"
print "forward = f, backward = b, left = l, right = r, up = u, down = d"
print "talk (person name), attack (person name), inspect (item name)"
print "equip (item name), drop (item name), stats will show your stats."
print "search will search the area, inventory will show the items on you."
print "Be sure to type the ENTIRE name of what you want to interact with."
print "========================================================================"

playername = raw_input("First, what is your name?\n")
print "========================================================================"


def Main():
    global PLAYER
    global ITEMS
    global MAPS
    global INTERACT
    global playername
    global QUESTS
    PLAYER.name = playername
    x = 2
    y = 3
    z = 1
    PLAYER.location[0] = x
    PLAYER.location[1] = y
    PLAYER.location[2] = z

    CurrentPlace = MAPS[x][y][z]
    print CurrentPlace.lore +"\n\n" + CurrentPlace.info + CurrentPlace.search()
    CurrentPlace.travelled = 0

    while(PLAYER.alive):
        direction = raw_input('What do you want to do?\n').lower().split(" ",1)
        for i in range(len(direction)):
           direction[i] = direction[i].strip() #Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]

            if verb in ['u','d','l','r','f','b']:
                CurrentPlace = Move(verb)

            elif (verb == 'search'):
                print CurrentPlace.search()

            elif (verb == 'stats'):
                Stats()
                
            elif (verb == 'inventory'):
                Inventory()

        elif (len(direction) == 2):
            verb = direction[0]
            objectName = direction[1]

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
            "I don't understand that command!"

        print "========================================================================"
    if not Story() and raw_input("Would you like to play again?[Y/N]: ").lower() == 'y':
        print "========================================================================"
        PLAYER.health = 100
        for i in PLAYER.inv:
            PLAYER.inv[i] = PLAYER.emptyinv[i]
        PLAYER.alive = True
        StartUp.Reset()
        MAPS = StartUp.WorldMap()
        ITEMS = StartUp.ItemDictionary()
        ENEMIES = StartUp.EnemyDictionary()
        INTERACT = StartUp.InteractDictionary()
        for i in QUESTS:
            QUESTS[i] = 1
        Main()
    elif Story() == 1:
        Opening.Closing()
        raw_input("Thanks for playing!!")
        print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"

    elif Story() == 2:
        Opening.Closing()
        print "Having defeated Dr.Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
    
Main()
