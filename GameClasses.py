"""
ENG PHYS TEXT BASED ADVENTURE
Mitchell Lemieux and Tyler Kashak
Wrote on April 14,2018: Icemageddon
"""
import operator
from random import *
import colorama  # Colour module, no bolding on windows :(
from colorama import Fore, Back, Style

colorama.init()
CLEARSCREEN = '\033[2J'  # This is the clearscreen variable
lightgreen = Fore.LIGHTGREEN_EX

def six_tuple_add(a, b, c, d, e, f):  # adds 6 tuples element-wise, used to calculate stats of character. If only need n elements added put (0,0,0) for 6-n arguments
    i = tuple(map(operator.add,a,b))
    j = tuple(map(operator.add,c,d))
    k = tuple(map(operator.add,e,f))
    ij = tuple(map(operator.add,i,j))
    return tuple(map(operator.add,ij,k))

def two_tuple_add(a, b):  # adds 2 tuples element-wise
    return tuple(map(operator.add,a,b))


# WHEN UPDATING ANY CLASS ATRIBUTE WILL NEED TO UPDATE IN CSVSaver to Reflect it!
#       Unless someone does something fancy to automatically update it but I don't feel it's necessary.

class Equipment:
    def __init__(self,name,location,image,info,worn,stats,health):
        self.name = str(name)
        self.image = str(image) 
        self.info = str(info)
        self.worn = str(worn)
        self.stats = stats
        self.location = location
        self.health = health
    
class Character:
    def __init__(self,name,location,health,inv,emptyinv, building = 0):
        self.name = str(name)
        self.location = location
        self.inv = inv
        self.emptyinv = emptyinv
        self.health = health
        self.maxhealth = 100
        self.basestats = [0,0,0]
        self.stats = six_tuple_add(self.inv['head'].stats, self.inv['body'].stats, self.inv['hand'].stats, self.inv['off-hand'].stats, tuple(self.basestats), (0, 0, 0)) #adds tuples together to new stats to make actual stats
        self.alive = True
        self.spoke = False  # What is this used for?
        self.building = 0  # This is the building they're are in, 0 by default. TODO add this into location tuple
        
        for i in inv:
            inv[i].location = self.location
        
    def updateStats(self): #updates stats based on changing equipment
        self.stats = six_tuple_add(self.inv['head'].stats, self.inv['body'].stats, self.inv['hand'].stats, self.inv['off-hand'].stats, tuple(self.basestats), (0, 0, 0))

    def equip(self,Equip):
        drop = 0
        if self.inv[Equip.worn] == Equip:
            print '\nThis item is already equipped\n'
        elif (self.location == list(Equip.location) and self.inv[Equip.worn] == self.emptyinv[Equip.worn]):
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print "\n"+Equip.info + "\n"
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + "."
        elif(self.location == list(Equip.location)):
            drop = self.inv[Equip.worn]
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print "\n"+ Equip.info
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + ', the ' + drop.name + ' has been dropped.\n'
        else:
            print "\nYou can't find that around here. Maybe it's your hungover typing.\n"
        self.updateStats()
        return drop

    def drop(self,Equip):  # Equip is an object not a name
        drop = 0
        if(Equip.name == self.inv[Equip.worn].name):
            self.inv[Equip.worn] = self.emptyinv[Equip.worn]
            print "\nYou've dropped the " + Equip.name
            drop = Equip
        else:
            print "Maybe you're still drunk?. You aren't carrying " + Equip.name + "."
        self.updateStats()
        return drop

    def ShowInventory(self):
        Head = "head\t\t"+self.inv['head'].name+"\t"+str(self.inv['head'].stats)+"\n"
        Body = "body\t\t"+self.inv['body'].name+"\t"+str(self.inv['body'].stats)+"\n"
        Hand = "hand\t\t"+self.inv['hand'].name+"\t"+str(self.inv['hand'].stats)+"\n"
        OffHand = "off-hand\t"+self.inv['off-hand'].name+"\t"+str(self.inv['off-hand'].stats)+"\n"
        print Head + Body + Hand + OffHand

class Enemy:
    def __init__(self,name,info,location,stats,health,drop,need,Sinfo,Dinfo):
        self.name = str(name)
        self.info = str(info)
        self.location = location
        self.stats = stats
        self.health = health
        self.Sinfo = Sinfo  # special info displayed if you give them what they need
        self.Dinfo = Dinfo  # death info displayed if they need
        self.need = need  # what the need, if you talk to them with this item you'll get the drop and it will set the quest flag to True
        self.drop = drop
        self.alive = True
        self.quest = False
        self.spoke = False
        
class Interact:
    def __init__(self,name,location,info,Sinfo,need,drop):
        self.name = name
        self.location = location
        self.info = info
        self.Sinfo = Sinfo
        self.need = need
        self.drop = drop
        self.quest = False

class Map:  #Map Location Storage
    def __init__(self, name, location, info, lore, walls, inside, size=None, links=[]): #size = (None) means default is none object unless otherwise defined
        self.name = str(name)       # Name of location
        # Dim is the dimension/ building number associated with the place, by default Overworld is 0, Bsb is 1, etc
        self.location = location    # Map coordinates tuple (X,Y,Z,Dim) TODO Make make ground level 0 and basements -1
        self.info = str(info)  # A more detailed description of the suroundings than the search function
        self.lore = str(lore)  # A monologue of the area and what you do when you get there
        self.items = []  # list of equipment objects at that location
        self.ENEMY = []  # list of enermy objects at that location
        self.walls = walls
        self.travelled = 1  # This defines if you've been there before TODO Name should be changed to untravlled
        self.inside = inside #Boolean that says if it's indoors for interriors and seeing the time
        self.mapped = 0  # TODO make consistent flag convention for 0 as default and 1 as activated
        # TODO Interriors rewarding at end
        # There is probably a better way to do this building stuff, maybe having an inherited ininterior class
        #   BUT This is what I'm going with!
        self.size = size  # size of interior (xRange,yRange, zRange). This tuple also flags it has/is an interior
        # When you go into the building from the side it enters the doorway on that size
        # If there's not doors on all sides have exterior outer area with links down (see diagram)
        self.links = links  # This is a list containing tuple coordinate pointers (direction, X, Y, Z, Building)
        # for doorways and Portals. A link will activate when moving the specified direction out of that space
        # ex) BSBDoor.links = [("l",2,4,1,0)], if exiting BSB player moves left to (3,3,3) in Overworld (building 0)
        # More complicated example would have multiple links depending on the direction. This creates a distorted spaces
        # ex) BSBLawn.links = [("f",0,6,0,1),("l",2,4,1,0), ("b",0,0,0,1)] this means depending on where the player
        #   moves they will will go to a different spot on the interior (so you don't have to step around BSB) or JHE
        # Walls can be used to close and open links as they won't let the player move into it and are mutable
        # Using tuples here because they're faster but if want to be changed can use nested lists (mutable)

        
        #self.interrior = interrior #interrior is a list of inner map objects (so infinite nesting)
        #self.exits = exits #pairs of coordinates coresponding to interrior entrance/exit and their coresponding exterirrior exits/entrances     
        
        #OR Make another coordinate d, dimension to specify interriors, but I'm leaning away from this
        #   although it would look cleaner on a spreadsheet
    def placeItem(self,item):  # the item object, works with the drop method in the character class
        if item:
            self.items.append(item)
            item.location=self.location
            
    def placeEnemy(self,Enemy):
        self.ENEMY.append(Enemy)
        Enemy.location = self.location
        
    def placeInteract(self,Interact):
        if Interact:
            self.items.append(Interact)
            Interact.location = self.location

    def removeWall(self, wall): #this is used to remove walls of rooms given the wall. WALLS have to be a lisst not a tuple to be mutable
        if wall in self.walls: 
            self.walls.remove(wall) #removes the wall from the list. wall attribute is direction it's blocking such as 'l'. HOWEVER The walls have to be in square [] not circle brackets () so its a list instead of a tuple. Lists are mutable, tuples are not
            
    def removeItem(self,item):  # had to be rewritted with load or else load function would create duplciate glitch
        for i in self.items:  # weird way to write it but loops through the items in that lcoation and if the name matches it removes it
            if i.name ==item.name:
                self.items.remove(i)
            
    def removeEnemy(self,enemy):
        if enemy in self.ENEMY:
            self.ENEMY.remove(enemy)

    def removeInteract(self,Interact):  # had to be rewritted with load or else load function would create duplciate glitch
        for i in self.items:  # weird way to write it but loops through the items in that lcoation and if the name matches it removes it
            if i.name == Interact.name:
                self.items.remove(i)

    # This function is the main thing that says what's in the area.
    def search(self,MAPS):  # Is passed MAPS dictionary so it can search area around it
        #also test the displays of things. [People], ~Places~, <Things>, /Interactables/ (put these next to descriptions)
        description = "\n"
        length = len(self.items)
        # (\S) used for printT newline
        # Initialize the {shortkey} used with object,interact,enemy for quick commands.
        shortkey = 5  # Starts at 5 because 1-4 are reserved for inventory quick commands
        # This big if statement basically does a printout to account for single object/enemy in the area grammer
        if length:
            description = "\nYou see"
            if length > 1:  # If there's more than one item/interact in the area
                for i in range(length):
                    if (i == length-1):
                        if isinstance(self.items[i],Equipment):
                            description = description+" and a {" + str(shortkey) + "}"+ Fore.MAGENTA + "<"+self.items[i].name + ">" + lightgreen +".\n" #item highlight, checks to see if object is of class equipment and if not it's an interactable
                            shortkey += 1  # increments the shortkey
                        else:
                            description = description+" and a {" + str(shortkey) + "}" + Fore.CYAN + "/"+self.items[i].name + "/" + lightgreen + ".\n" #inspectable highlight
                            shortkey += 1  # increments the shortkey
                    else:
                        if isinstance(self.items[i],Equipment):
                            description = description + " a {" + str(shortkey) + "}"+ Fore.MAGENTA + "<"+self.items[i].name + ">" + lightgreen +","
                            shortkey += 1  # increments the shortkey
                        else:
                            description = description + " a {" + str(shortkey) + "}" + Fore.CYAN + "/"+self.items[i].name + "/" + lightgreen + ","
                            shortkey += 1  # increments the shortkey
            else:  # if there's only 1 item/interact in the area
                if isinstance(self.items[0],Equipment):
                    description = description + " a {" + str(shortkey) + "}"+ Fore.MAGENTA + "<"+self.items[0].name + ">" + lightgreen +".\n" # equipment highlight
                    shortkey += 1  # increments the shortkey
                else:
                    description = description + " a {" + str(shortkey) + "}" + Fore.CYAN + "/"+self.items[0].name + "/" + lightgreen + ".\n" # inspectable highlight
                    shortkey += 1  # increments the shortkey
        
        if self.ENEMY: 
            for enemy in self.ENEMY:
                if enemy.alive and enemy.location == (2,4,1,0): #if enermy is in JHE lobby they are playing eng phys text adventure lol (including yourself)
                    description = description + "(\S){" + str(shortkey) + "}" + Style.BRIGHT + Fore.YELLOW + "[" + enemy.name + "]" + Style.RESET_ALL + lightgreen + " is playing the Eng Phys Text Based Adventure. WAIT What!?"
                    shortkey += 1  # increments the shortkey
                elif enemy.alive:
                    description = description + "(\S){" + str(shortkey) + "}" + Style.BRIGHT + Fore.YELLOW + "[" + enemy.name + "]" + Style.RESET_ALL + lightgreen + " is " \
+ choice(["standing in the corner","wandering around","reading a book","creating a grand unified field theory",
          "eating a frighteningly large burrito","playing runescape","browsing math memes",
          "taking a hit from a laser bong","laying down crying","watching the Big Lez show on full volume",
          "eating a Big Mac", "eating too much Lava Pizza", "contemplating how much Mayo is too much",
          "bathing in Mayonnaise", "in a sushi coma", "phasing in and out of this dimension", "drinking spicy Pho broth",
          "reading a book under a tree", "wondering how you can read their thoughts?", "playing 4D chess",
          "pondering necromancy", "unsuccessfully painting their WarHammer miniature with Mili",
          "Synthesizing Gold Nanoparticles", "creating an AI Dog", "petting a cat", "carrying a soccer ball",
          "playing football by themself", "balancing a tennis racket on their nose", "digging down in Minecraft",
          "catching a shiny Pikachu", "checking their Hearthstone Bot", "solving time travel", "watching Gilmore Girls",
          "computing the eigenvalue of the inverse Mobius strip", "watching Little House on the Prairie",
          "getting shot by an auto-turret in Rust", "trying to think of a capstone idea", "being watched"]) + "."
                    shortkey += 1  # increments the shortkey


                else:
                    description = description + "(\S)Oh look, its the " \
                                  + choice(["decaying ", "broken ", "bloodied ", "mutilated ", "scrambled ", "soulless ", "degraded ", "decrepit ", "blank empty stare of the ", "mouldy "]) \
                                  + choice(["corpse of ", "body of ", "cadaver of ", "hunk of meat that used to be ", "remains of ", "chalk outline of ", "snack that used to be "]) \
                                  + "{" + str(shortkey) + "}" + Style.DIM + Fore.YELLOW + "[" + enemy.name + "]" + Style.RESET_ALL + lightgreen + "."
                    shortkey += 1  # increments the shortkey

        # if self.interact:
        #     for item in self.interact:
        #         description = description + "/" + item.info + "/\n"
                
        if (description == ""):
            description = "(\S)There isn't a whole lot to see."

        # --- Auto Surrounding Descriptions ---
            # Finding the locations around current location
        location = self.location  # gets coordinates tuple
        letterdirections = ['u', 'd', 'f', 'b', 'l', 'r']  # letter based list of directions to check against walls
        lettersthere = ""
        tupledirections = [(0,0,1,0), (0,0,-1,0), (0,1,0,0), (0,-1,0,0), (-1,0,0,0), (1,0,0,0)]  # tuple based list of directions to add to current location
        surroundings = [None] * 6  # Name storage, defaulted to none. Order of: Left, right, Front, Back, Up, Down
        i = 0  # Counter for direction indexing
        for direction in letterdirections:  # Looping through all the directions
            if direction not in self.walls:  # seeing if the way you can go is in the walls
                # Gets tuple of requested adjacent spot by adding the direction in the right order
                dx, dy, dz, dim = tuple(map(operator.add,location,tupledirections[i]))
                if MAPS[dx][dy][dz][dim]:  # if the map location exists
                    surroundings[i] = MAPS[dx][dy][dz][dim].name  # store the name into the surroundings variable
                    lettersthere += direction + ","
            i += 1

            # Reading out the Surroundings
        # TODO Add discovery mechanic where it prints locations as you see them
                # Short Description
        worddirections = ['[U] ','[D] ','[F] ','[B] ','[L] ','[R] ']
        description += "(\S) (\S)There are " + str(6 - surroundings.count(None)) + " obvious exits: " + lettersthere + "(\S)"

                # TODO for even shorter/harder list only directions
        for i in range(6):  # use index to reference direction
            if surroundings[i]:  # if the direction is seen
                description += worddirections[i] + surroundings[i] + "\t"  # print the word direction + name
            if worddirections[i] in ['[D] ','[B] '] and surroundings[i]:  # Adds a spaces to make 3 x 2 printout
                description += " (\S) "
                #TODO Add wordy description


            
        return description


        # Don't need to return the 'Global' objects from function as affecting scope outside the function

            

