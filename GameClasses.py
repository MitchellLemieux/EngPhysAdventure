"""
ENG PHYS TEXT BASED ADVENTURE
Mitchell Lemieux and Tyler Kashak
Wrote on April 14,2018: Icemageddon
"""
import operator
from random import *

def tupleAdd(a,b,c,d,e,f): #adds 6 tuples element-wise, used to calculate stats of character. If only need n elements added put (0,0,0) for 6-n arguments
    i = tuple(map(operator.add,a,b))
    j = tuple(map(operator.add,c,d))
    k = tuple(map(operator.add,e,f))
    ij = tuple(map(operator.add,i,j))
    return tuple(map(operator.add,ij,k))

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
    def __init__(self,name,location,health,inv,emptyinv):
        self.name = str(name)
        self.location = location
        self.inv = inv
        self.emptyinv = emptyinv
        self.health = health
        self.maxhealth = 100
        self.basestats = [0,0,0]
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats,tuple(self.basestats),(0,0,0)) #adds tuples together to new stats to make actual stats
        self.alive = True
        self.spoke = False
        
        for i in inv:
            inv[i].location = self.location
        
    def updateStats(self): #updates stats based on changing equipment
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats,tuple(self.basestats),(0,0,0))

    def equip(self,Equip):
        drop = 0
        if self.inv[Equip.worn] == Equip:
            print '\nThis item is already equipped\n'
        elif (self.location == list(Equip.location) and self.inv[Equip.worn] == self.emptyinv[Equip.worn]):
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print "\n"+Equip.info
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + ".\n"
        elif(self.location == list(Equip.location)):
            drop = self.inv[Equip.worn]
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print "\n"+ Equip.info
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + ', the ' + drop.name + ' has been dropped.\n'
        else:
            print "\nThat doesn't seem to be around here.\n"
        self.updateStats()
        return drop

    def drop(self,Equip):  # Equip is an object not a name
        drop = 0
        if(Equip.name == self.inv[Equip.worn].name):
            self.inv[Equip.worn] = self.emptyinv[Equip.worn]
            print "\nYou've dropped the " + Equip.name
            drop = Equip
        else:
            print "You aren't carrying that item."
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
        self.item = None
        self.Sinfo = Sinfo #special info displayed if you give them what they need
        self.Dinfo = Dinfo #death info displayed if they need
        self.need = need #what the need, if you talk to them with this item you'll get the drop and it will set the quest flag to True
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
    def __init__(self,name,coords,info,lore,walls,inside, size = ((None)), building = 0, links = ((None))): #size = (None) means default is none object unless otherwise defined
        self.name = str(name)       #Name of location
        self.coords = coords        #Map coordinates (X,Y,Z)
        self.info = str(info)  # Description of areas around it and name, TODO Make this generate automatically
        self.lore = lore  # Description of the location
        self.items = []  # list of equipment objects at that location
        self.ENEMY = []  # list of enermy objects at that location
        self.walls = walls
        self.travelled = 1
        self.inside = inside #Boolean that says if it's indoors for interriors and seeing the time
        self.mapped = 0  # TODO make consistent flag convention
        # TODO Interriors rewarding at end
        # There is probably a better way to do this building stuff, maybe having an inherritted interrior class BUT
        #   This is what I'm going with!
        self.size = size  # size of interior (xRange,yRange, zRange). If this is a filled tuple it has an interior
        # When you go into the building from the side it enters the doorway on that size
        # If there's not doors on all sides have exterior outer area with links down (see diagram)
        self.building = building  # The building number associated with the place, by default Overworld is 0
        self.links = links  # This is a coordinate pointer (X, Y, Z, Building) for doorways and Portals
        # Moving in the direction into the door links you to the position. So Needs to be nested tuples for multiple
        # Using tuples here because they're faster but if want to be changed (Mutuble) can use lists

        
        #self.interrior = interrior #interrior is a list of inner map objects (so infinite nesting)
        #self.exits = exits #pairs of coordinates coresponding to interrior entrance/exit and their coresponding exterirrior exits/entrances     
        
        #OR Make another coordinate d, dimension to specify interriors, but I'm leaning away from this
        #   although it would look cleaner on a spreadsheet
    def placeItem(self,item):  # the item object, works with the drop method in the character class
        if item:
            self.items.append(item)
            item.location=self.coords
            
    def placeEnemy(self,Enemy):
        self.ENEMY.append(Enemy)
        Enemy.location = self.coords
        
    def placeInteract(self,Interact):
        if Interact:
            self.items.append(Interact)
            Interact.location = self.coords

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
            if i.name ==Interact.name:
                self.items.remove(i)

    def search(self): #TODO improve search to automatically spit out the direction stuff,
        #also test the displays of things. [People], ~Places~, <Things>, /Interactables/ (put these next to descriptions)
        description = "\n"
        length = len(self.items)
        if length:
            description = "\nYou see"
            if length > 1:
                for i in range(length):
                    if (i == length-1):
                        if isinstance(self.items[i],Equipment):
                            description = description+" and a <"+self.items[i].name + ">.\n" #item highlight, checks to see if object is of class equipment and if not it's an interactable
                        else:
                            description = description+" and a /"+self.items[i].name + "/.\n" #inspectable highlight
                    else:
                        if isinstance(self.items[i],Equipment):
                            description = description + " a <"+self.items[i].name + ">,"
                        else:
                            description = description + " a /"+self.items[i].name + "/,"
            else:
                if isinstance(self.items[0],Equipment):
                    description = description + " a <" +self.items[0].name + ">.\n" #equipment highlight
                else:
                    description = description + " a /" +self.items[0].name + "/.\n" #inspectable highlight
        
        if self.ENEMY: 
            for enemy in self.ENEMY:
                if enemy.alive and enemy.location == (2,4,1): #if enermy is in JHE lobby they are playing eng phys text adventure lol (including yourself)
                    description = description + "[" + enemy.name + "] is playing the Eng Phys Text Based Adventure. WAIT What!?\n"
                elif enemy.alive:
                    description = description + "[" + enemy.name + "] is " \
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
          "getting shot by an auto-turret in Rust", "trying to think of a capstone idea", "being watched"]) + ".\n"


                else:
                    description = description + "Oh look, its the " \
                                  + choice(["decaying ", "broken ", "bloodied ", "mutilated ", "scrambled ", "soulless ", "degraded ", "decrepit ", "blank empty stare of the ", "mouldy "]) \
                                  + choice(["corpse of ", "body of ", "cadaver of ", "hunk of meat that used to be ", "remains of ", "chalk outline of ", "snack that used to be "]) \
                                  + "[" + enemy.name + "].\n"

        # if self.interact:
        #     for item in self.interact:
        #         description = description + "/" + item.info + "/\n"
                
        if (description == ""):
            description = "\nThere isn't a whole lot to see."
            
        return description

    def goInside(self,CurrentPlace,MAPS,PLAYER,ENEMIES,direction):
        """
        This function is used to not only go inside the interrior of the building but move within there
        """
        if  not(CurrentPlace.size): #if the previous place was not inside you step into the interrior
            print "You are trying to go inside"
            
            
        return 

