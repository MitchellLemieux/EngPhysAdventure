from GameFunctions import *
import StartUp
import Opening

Opening.Opening()

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
        Story()
        for i in range(len(direction)):
           direction[i] = direction[i].strip() #Getting rid of the spaces at the end of words

        if len(direction) == 1:
            verb = direction[0]

            if verb in ['u','d','l','r','f','b']:
                CurrentPlace = Move(verb)

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
               print "\nI don't understand that command!\n"

        print "========================================================================"
    if Story()== 0 and raw_input("Would you like to play again?[Y/N]: ").lower() == 'y':
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
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Opening.Closing()
            print "After performing the purge of the faculty you join Dr.Cassidy in shaping the New Order.\nAs Dr.Cassidy's apprentice you reign over McMaster University with an iron fist.\nEngineering Physics is established as the premium field of study and all funding is directed to you.\nYou unlock secrets of untold power which allows you to reinforce your overwhelming grasp on the university.\nYour deeds have given you complete power and you reign supreme for eternity.\nTHE END"
            raw_input("Thanks for playing!!")
    elif Story() == 2:
        if raw_input("Type 'C' to continue\n").lower() == 'c': 
            Opening.Closing()
            print "Having defeated Dr.Cassidy you proved yourself to be a truly honourable engineer.\nWith the forces of evil defeated, McMaster University will continue to operate in peace.\nAll faculties exist in harmony and the integrity of the institution has been preserved.\nYou go on to lead a successful life as an engineer satisfied that you chose what was right.\nTHE END."
            raw_input("Thanks for playing!!")
Main()
