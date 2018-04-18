#Developer testing 
from GameFunctions import *

print "=================================================================================="
print "Hello, and welcome to..."
print "___________THE GREAT       __________.__"                 
print "\_   _____/ ____    ____   \______   \  |__ ___.__. ______"
print " |    __)_ /    \  / ___\   |     ___/  |  <   |  |/  ___/"
print " |        \   |  \/ /_/  >  |    |   |   Y  \___  |\___ \ "
print "/_______  /___|  /\___  /   |____|   |___|  / ____/____  >"
print "        \/     \//_____/ TEXT ADVENURE    \/\/ (v4.20) \/\n"
print "Created by: Mitchell Lemieux & Tyler Kashak"
print "Special Thanks: Erik, Eric, Brian, Megan, and Brendan <3\n"
print "Before you go any further there are some things you must know..."
print "Your orientation never changes. When you enter you will be facing the"
print "entrance of JHE and you will ALWAYS face that way."
print "The commands which allow you to interact with your environment are:"
print "forward = f, backward = b, left = l, right = r, up = u, down = d"
print "talk = (person name), attack = (person name), inspect = (item name)"
print "Typing stats will show your stats (ATTACK/DEFENCE/SPEED)."
print "Typing search will give you an idea of your surroundings."
print "Typing an item/person to interact with type the ENTIRE name as you read it."
print "Thats it. Good luck!"
print "=================================================================================="

playername = raw_input("First, what is your name?\n")
PLAYER.name = playername

x = PLAYER.location[0]
y = PLAYER.location[1]
z = PLAYER.location[2]
CurrentPlace = MAPS[x][y][z]
print CurrentPlace.lore + "\n" + CurrentPlace.info + "\n" + CurrentPlace.search()
CurrentPlace.travelled = 0

while(PLAYER.alive):
    
  
    #Getting input and splitting it at the spaces
    direction = raw_input('What do you want to do?\n').lower().split(" ",1)
    #print direction
    
    if len(direction) == 1:

        verb = direction[0]
        
        if verb in ['u','d','l','r','f','b']:
            CurrentPlace = Move(verb)

        elif (verb == 'search'):
            print CurrentPlace.search()
            
        elif (verb == 'stats'):
            Stats()


    elif (len(direction) == 2):
        verb = direction[0]
        objectName = direction [1]
        
        if verb == 'equip':
            Equip(objectName)
        
        if verb == 'drop':
            Drop(objectName)

        if verb == 'attack':
            Attack(objectName)

        if verb == 'talk':
            Talk(objectName)
            
        if verb == 'inspect':
            Inspect(objectName)
                        

    

