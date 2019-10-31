"""
This Parser is defined to be our version of the natural language processor.
It's main goal is to take in inputs from the user in a way that reduces frustration of trying to do actions.
Some of this will be done through teaching/tutorials, some through having the ability to quickly address things,
some is done through being able to interpret a wide variety of language, and the last is having robustness to handle
the wide variety of situations that may be encountered.
Generally the Eng Phys Text Adventure is very simple two word(ish) parser.
It's looking for a Verb (function) and a Noun (object).
Our basic level is having an explicit system with Verb Full Noun (with spellchecking)

1. The next layer of abstraction is Verb then partial noun.
2. Verb then noun at any point.
3. Any combination of verb and noun.
4. Multiple objects and commands in single line
5. Quick verb and quick noun address
e. Any combination of these with spellchecking included.

Research
Could support adjectives or multiple words to be mores specific and distinguish
Get rid of certain words like the, in, about, etc
Infocom-type parsers are based on the grammer of english. A lot more complex but more robust. Would be too advanced to
implement and might just use authoring at that point.
http://www.ifwiki.org/index.php/Infocom-type_parser
When something is mentioned in the description but not interactable in the game it is a crime (people want it):
    http://www.ifwiki.org/index.php/Mimesis
A game that lacks mimesis is not necessarily a failure,
    and a game that contains nothing but mimesis is not necessarily enjoyable.
Need to make sure to communicate allowable actions to player so it's clear, no paralysis, etc
    https://emshort.blog/2010/06/07/so-do-we-need-this-parser-thing-anyway/
    Lots of time goes to accounting for thounds of player options rather than creating interesting stories or puzzles
Formal Parser testing
    https://emshort.blog/2008/11/24/lick-tree-purchase-antlers/

* I would rather restrict the player options but make it clear. Their can be synonym words but not going too far
If we say it can do anything we can't account for it all, but if we tell them the basics they only do that so there's
no more point to develope anything further

* Part of helping the game may come from making sure nouns and verbs are distinct but that may be impossible.
* The next best possibility is to make sure that these are all distinguishable based on situational context e.g. (what
is in the immediate area, what type of object is the noun referring to, and possibly how the order or size the word.
* This will be a large work in progress needed lots of testing and implementation. Other material should be referenced
but make no mistake that this parser will be VERY GAME SPECIFIC. Meaning not only will it most likely only work for this
game but only for this implementation/update of the game. That's hopefully why this is the last update with a lot of
the balancing and testing happening at the end.

This is a parser based game or text based adventure

Ours boils down to basically several different vanilla commands (after getting rid of others)
These functions should be object based methods but whatever for now. that will be rebuild
Equip:
Get
Drop:
Move:
Attack:
Talk:
Inspect/Interact:
Open
Examine
Read
Inventory:
Eat:
Look:


Download latest update then add this and update the feature list.
"""

# How does the spellcheck work?

# How can we use parts of the noun/object?

# How can we search within a sentence to find the verb and the noun?

# How can we make the parser robust?

# How can teach and handle cases that lead the user to understand the parser the best?

# How can we keep the text input fun and engaging, for any level of player?
from GameFunctions import *
import CreativeMode

ALLKEYS = sorted(ITEMS.keys() + ENEMIES.keys() + INTERACT.keys())  # keys of all objects used for spellcheck function
# acceptable game commands called 'verbs'. Need to add verb to this list for it to work in game decision area
VERBS = ['search', 'inventory', 'equip', 'drop', 'attack', 'talk', 'inspect', 'eat', 'up', 'down', 'left', 'right',
         'back', 'forward', 'kill', 'get', 'wear', 'look', 'drink', 'inhale', 'ingest', 'devour', 'north', 'south',
         'east', 'west', 'fight', 'examine', 'exit', 'leave', 'quit', 'speak', 'throw', 'go', 'move',
         'walk', 'run', 'turn', 'remember', "wait", "sleep", 'sit', 'die', 'pick', 'use', 'give', 'say', 'help',
         'recall','shortcuts']
# DIRECTIONS = []  # TODO Make these wordlist verbs defined here
DEVVERBS = ['/stats', '/savegame', '/loadgame', '/restart', '/']  # lists of Verbs/keywords ONLY the developer can use
DEVVERBS.extend(VERBS)  # Combining all the normal verbs into DEVVERBS to make the extended list when in dev mode

VERBSHORCUTS = ['a', 'b', 'd', 'dr', 'e', 'ea', 'ex', 'f', 'g', 'h', 'i', 'l', 'r', 're', 's', 't', 'u', 'us']


"""
Shortcuts
a = attack
b = back
c = 
d = down
dr = drop
e = equip
ea = eat
ex = examine
f = front
g = give
h = help
i = inventory
j = 
k = 
l = left
m = 
n = 
o = 
p = 
q = 
r = right
re = recall
s = search
t = talk
u = up
us = use
v = 
w = 
x = 
y = 
z = 
"""

shortcutprint = "Shortcuts(\S)a = attack(\S)b = back(\S)d = down(\S)dr = drop(\S)e = equipt(\S)ea = eat" \
                        "(\S)ex = examine(\S)f = front(\S)g = give(\S)h = help(\S)i = inventory(\S)l = left(\S)" \
                        "r = right(\S)re = recall(\S)s = search(\S)t = talk(\S)u = up(\S)us = use" \
                        "(\S) (\S)For <objects>,/interacts/, or [people] use the shortkey number beside the name or a subword of the name" \
                        "(\S) e.g. dr 1 (examine the thing with {1} beside it)" \
                        "(\S)" \
                        "(\S) e.g. a brian (attack Brian the Weeb)"



def Parser(command,PLAYER,ITEMS,MAPS,INTERACT,QUESTS,ENEMIES,GAMEINFO,GAMESETTINGS):
    GAMEINFO['log'].append(command)
    # this splits it at the first spacing making it the first verb and then the rest as the object noun
    # CURRENTLY the rest of the parser calls simply a function based on the verb and passes it the object noun name
    wordlist = command.lower().split(" ", 1)  # Split at first space for verb

    for i in range(len(wordlist)):  # Getting rid of the spaces in strings using .strip()
        wordlist[i] = wordlist[i].strip()

    # ------------------------------1 word Commands-------------------------------------
    if len(wordlist) == 1:  # if it's a single word command
        verb = wordlist[0]  # it has to be a verb if it's a single word command
        #  --- Verb Spellchecking ---
        if len(verb) > 1:
            # if dev mode enabled it accepts special verbs which allows you to use special functions
            if verb == '/420e69': pass  # Does no spell checking so someone doesn't accidentally get 420e69
            elif verb in VERBSHORCUTS: pass  # Does no spell checking if it's a shortcut
            elif GAMESETTINGS['DevMode']: verb = SpellCheck(verb, DEVVERBS)
            else: verb = SpellCheck(verb, VERBS)

        #  --- Parsing ---
        if verb in ['l','r','f','b','u','d','up', 'down', 'left', 'right', 'back', 'forward','north', 'south', 'east', 'west', 'ahead', 'backward']:
            CurrentPlace = Move(verb)  # TODO check if CurrentPlace is actually returned and if so, use it
            GAMEINFO['stepcount'] += 1  # increments the stepcount after taking a step (whether sucessful or not)
        elif verb in [ 's','search', 'look']:
            x, y, z, dim = PLAYER.location
            printT("(\S) ~" + MAPS[x][y][z][dim].name.upper() + "~ (\S)" + MAPS[x][y][z][dim].search(MAPS), 72, 0.5)

        # TODO if word based description: re-enable stats and remove from DEVVERBs
        elif (verb == '/stats'):
            Stats()
        elif verb in ['i','inventory']:
            Inventory()
        elif verb == '/savegame':
            # TODO add: computer name, words and characters per minute, # enemies killed, # items eaten, # items equiped, # enemies talked, # quantum relecs found
            GAMEINFO['runtime'] += (time.time() - GAMEINFO[
                'timestart'])  # adds the runtime (initilized to zero) to the session runtime to make the total runtime
            GAMEINFO['timestart'] = time.time()  # resets timestart so it's not doubly added at the end
            logGame(GAMEINFO['log'])  # logs the game when you save it
            CreativeMode.saveGame(GAMEINFO['playername'])  # saves all data
            print "Your game has been saved!: SaveFile " + GAMEINFO['playername']
        elif verb == '/loadgame':  # this function loads the game off of the save file. Was having problems with loading
            CreativeMode.loadGame(GAMEINFO['playername'])  # loads in the savefile global variables
            GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
        elif verb == '/restart':  # this restarts the game to the base game
            CreativeMode.loadGame("basegame")  # loads in the savefile global variables
            GAMEINFO['timestart'] = time.time()  # reset local variable starttime to current time
        elif verb == '/420e69':  # This toggles game to dev mode for debugging in game
            GAMESETTINGS['DevMode'] = int(not (GAMESETTINGS['DevMode']))
            # Prints throw-off style text while still giving the stat
            print "\nYour hungover brain struggles to understand that command" + str(GAMESETTINGS['DevMode']) + "!\n "
            # This section writes devmode to settings.ini file so you can get back to the settings
            # TODO Before release comment out this section so DevMode isn't saved. DevMode in setting file is not for RELEASE
            f = open("settings.ini", "w+")
            for setting in GAMESETTINGS:
                f.write(setting + "\n" + str(GAMESETTINGS[setting]) + "\n")
            f.close()
        # This normal function exits the game but also saves your progress so you can pick back up.
        # Now at least for normal people you can't metagame by saving and loading files
        elif verb in ['exit', 'leave', 'quit', "die"]:
            # A FULL Copy of /savegame function bassically
            if raw_input(
                    "\n\nAre you sure you want to save and quit the game?\nYour game will be saved.\nType Y if you wish to save and leave,\nanythine else to continue: \n").lower() in [
                "y", 'yes', 'yeah']:
                GAMEINFO['runtime'] += (time.time() - GAMEINFO[
                    'timestart'])  # adds the runtime (initilized to zero) to the session runtime to make the total runtime
                GAMEINFO['timestart'] = time.time()  # resets timestart so it's not doubly added at the end
                logGame(GAMEINFO['log'])  # logs the game when you save it
                CreativeMode.saveGame(GAMEINFO['playername'])  # saves all data
                print "Your game has been saved! " + GAMEINFO[
                    'playername']  # Don't indicate the save file has save file in the name
                raw_input(
                    "We're sad to see you go :( \nI hope whatever you're doing is more fun.\nPress anything to leave")
                exit()
        elif verb in ['re',"remember", "recall"]:
            x, y, z, dim = PLAYER.location
            place = MAPS[x][y][z][dim]
            print "You entered " + place.name + "\n"
            printT(place.lore)
        elif verb in ["wait", "sleep", "sit"]:
            printT("Time passes.")
        elif verb in ['h', "help"]:
            printT(GAMEINFO['help'], 72, 0.10)
        elif verb == "shortcuts":
            printT(shortcutprint, 72, 0.10)
        else:
            print "\nYour hungover brain struggles to understand that command!\n"

    # ------------------------------2+ word Commands-------------------------------------

    elif (len(wordlist) == 2):  # If the command is more than one word long
        verb = wordlist[0]

        #  --- Verb Spellchecking ---
        if len(verb) > 1:
            # if dev mode enabled it accepts special verbs which allows you to use special functions
            if verb in VERBSHORCUTS: pass  # Does no spell checking if it's a shortcut
            elif GAMESETTINGS['DevMode']: verb = SpellCheck(verb, DEVVERBS)
            else: verb = SpellCheck(verb, VERBS)
        # Implemented a pass on the spellcheck for creativemode, will fix this BS later
        # TODO Fix this BS (I.E. make the spellchecker work for multi nounbased structure OR have commands be combined

        # --- Object Spellchecking and Shortcuts ---
        if verb == "/": objectName = wordlist[1]  # Doesn't do spell check if creative command

        #       --- ShortKey Object Shortcut  ---
        # ShortKey matching to give it the right objectName
        elif str.isdigit(wordlist[1]): # if the object is a number assume it's a shortkey
            x, y, z, dim = PLAYER.location
            shortkey = int(wordlist[1])  # converts from string to int because we know it's an int
            # makes a list of objects of all items in area including Inventory First
            surroundingobjects = [PLAYER.inv['head'],PLAYER.inv['body'],PLAYER.inv['hand'],PLAYER.inv['off-hand']]\
                                 + MAPS[x][y][z][dim].items + MAPS[x][y][z][dim].ENEMY
            if shortkey > len(surroundingobjects):
                printT("You sure you're okay? There's no " + "{" + str(shortkey) + "} around here.")
                return  # returns out of the function because invalid input
            for i in range(1,len(surroundingobjects)+1):  #Shifted loop because starting at 1
                if i == shortkey:
                    objectName = surroundingobjects[i-1].name.lower()  # assigns the object name to the same position as seen
                    if objectName == "empty":  # if you request something with an empty object it exists
                        playerslot = ["head","body","hand","off-hand"]
                        printT("Your hungover brain realizes you aren't wearing anything on your " + str(playerslot[i]) +".")
                        return
        # TODO make exclusion list for custom parser things like these that you don't want spellchecking on 2nd word
        elif verb in ['go', 'move', 'walk', 'run', 'turn', 'look', 'pick', 'say']: objectName = wordlist[1]  # no spell check for certain thing

        #       --- Object SubWord Search ---
        # This function allows you to put in one+ word object names and still find a match
        else:
            #       --- Setup ---
            x, y, z, dim = PLAYER.location
            # A list of objects of all items in area including Inventory First
            surroundingobjects = [PLAYER.inv['head'], PLAYER.inv['body'], PLAYER.inv['hand'], PLAYER.inv['off-hand']] \
                             + MAPS[x][y][z][dim].items + MAPS[x][y][z][dim].ENEMY

            surobjectsfullnames = []  # list contains full names of the items around
            surobjectswords = []  # list contains
            for object in surroundingobjects:
                name = object.name.lower()
                if name == wordlist[1]:  # If the word is typed perfectly save it and stop the loop
                    objectName = wordlist[1]
                    break  # break out of the loop for efficiency
                else:  # creates list of full names and broken apart ones
                    surobjectsfullnames.append(name)
                    surobjectswords += name.split(" ")

            #       --- Filtering Duplicates and extraneous words ---
            extraneouswords = ["of", "dr.", "the","in"]
            duplicatewords = []

            # getting rid of ALL occurances of extraneous words
            for word in extraneouswords:
                for x in range(surobjectswords.count(word)):
                    surobjectswords.remove(word)

            # Finding duplicate words so they can't be used
            surobjectswords.sort()
            for i in range(len(surobjectswords) - 1):
                if surobjectswords[i] == surobjectswords[i + 1]:
                    if surobjectswords[i] not in duplicatewords:
                        duplicatewords.append(surobjectswords[i])

            # Removing duplicate words
            # Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
            surobjectswords = list(dict.fromkeys(surobjectswords))

            #       --- Matching and returning full names ---
            # search through each word in wordlist[1], spell check each, Search for match
            objectlist = wordlist[1].split()
            for word in objectlist:
                if word in duplicatewords:
                    continue


            # SILENCE FOR DEMO
            # print wordlist[1]
            # print surroundingobjects
            # print surobjectsfullnames
            # print surobjectswords
            # print duplicatewords
            # print objectlist

            # Old spellcheck for full name still works
            objectName = SpellCheck(wordlist[1], ALLKEYS)  # Does do spell check if normal



        #  --- Parsing ---
        if verb in ['e','equip', 'get', 'wear']:
            Equip(objectName)

        elif verb in ['dr','drop', 'throw']:
            Drop(objectName)

        elif verb in ['a','attack', 'kill', 'fight']:
            Attack(objectName)

        elif verb in ['t','talk', 'speak']:
            Talk(objectName)

        elif verb in ['ex','inspect', 'examine']:
            Inspect(objectName)

        elif verb in ['ea','eat', 'drink', 'inhale', 'ingest', 'devour']:
            Eat(objectName)

        elif verb in ['go', 'move', 'walk', 'run', 'turn']:  # this may or may not work
            CurrentPlace = Move(objectName)
            GAMEINFO['stepcount'] += 1  # increments the stepcount after taking a step (whether sucessful or not)

        elif verb == "/":  # if using a CreativeMode command
            CreativeMode.creative_parser(objectName)
        elif verb == "look":  # used just for look around case
            if objectName == "around":
                x, y, z, dim = PLAYER.location
                printT("(\S) ~" + MAPS[x][y][z][dim].name.upper() + "~ (\S)" + MAPS[x][y][z][dim].search(MAPS), 72, 0.5)
        elif verb == "pick":  # Allows for pick up to be a thing
            if objectName.lstrip().startswith("up"):  # if up is the second word
                objectName = objectName.lstrip().split("up")[1].lstrip()  # strips down to just the object name
                Equip(objectName)  # Equipts it
        elif verb in ['us',"use"]:  # this makes it so you can use items if the interacble is in the area
            x, y, z, dim = PLAYER.location
            # checks all interactables in area to see if item is needed
            for interactable in MAPS[x][y][z][dim].items:  # for all itmes+interactables in the area
                if isinstance(interactable, Interact):  # if it's in interactable
                    if interactable.need == objectName:
                        print "\nYou use the " + objectName + " with the " + interactable.name + ".\n"
                        Inspect(interactable.name.lower())
        elif verb in ['g','give']:
            x, y, z, dim = PLAYER.location
            # checks all Enemies in area to see if item is needed
            for enemy in MAPS[x][y][z][dim].ENEMY:  # for all enemy in the area
                if enemy.need == objectName:
                    print "\nYou give the " + objectName + " to " + enemy.name + ".\n"
                    Talk(enemy.name.lower())
        elif verb == "say":
            printT("You say " + objectName)
        else:
            print "\nYour hungover brain struggles to understand that command!\n"

