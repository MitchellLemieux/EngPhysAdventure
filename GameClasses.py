#ENG PHYS TEXT BASED ADVENTURE
#Mitchell Lemieux and Tyler Kashak
#Wrote on April 14,2018: Icemageddon

import operator
from random import *


def tupleAdd(a,b,c,d): #adds 4 tuples element-wise, used to calculate stats of character
    i = tuple(map(operator.add,a,b))
    j = tuple(map(operator.add,c,d))
    return tuple(map(operator.add,i,j))

class Equipment:
    def __init__(self,name,location,image,info,worn,stats,health):
        self.name = str(name)
        self.image = str(image) 
        self.info = str(info)
        self.worn = str(worn)
        self.stats = stats
        self.location = location
        self.health = health
    
class Character: #When the equip function is called we need to make sure the item is actually in the room
    
    def __init__(self,name,location,health,inv,emptyinv):
        self.name = str(name)
        self.location = location
        self.inv = inv
        self.emptyinv = emptyinv
        self.health = health
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats)
        self.alive = True
        self.spoke = False
        
        for i in inv:
            inv[i].location = self.location
        
    def updateStats(self):
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats)
        
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

    def drop(self,Equip):
        drop = 0
        if(Equip == self.inv[Equip.worn]):
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
        self.Sinfo = Sinfo
        self.Dinfo = Dinfo
        self.need = need
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
    def __init__(self,name,coords,info,lore,walls):
        self.name = str(name)       #Name of location
        self.coords = coords        #Map coordinates (X,Y,Z)
        self.info = str(info)
        self.lore = lore#Description of the location
        self.items = []
        self.ENEMY = []
        self.interact = []
        self.walls = walls
        self.travelled = 1

    def placeItem(self,item): #Works with the drop method in the character class
        if item:
            self.items.append(item)
            item.location=self.coords
            
    def placeEnemy(self,Enemy):
        self.ENEMY.append(Enemy)
        Enemy.location = self.coords
        
    def placeInteract(self,Interact):
        self.interact.append(Interact)
        Interact.location = self.coords

    def removeWall(self, wall): #this is used to remove walls of rooms given the wall. WALLS have to be a lisst not a tuple to be mutable
        if wall in self.walls: 
            self.walls.remove(wall) #removes the wall from the list. wall attribute is direction it's blocking such as 'l'. HOWEVER The walls have to be in square [] not circle brackets () so its a list instead of a tuple. Lists are mutable, tuples are not
            
    def Remove(self,item):
        if item in self.items:
            self.items.remove(item)
            
    def removeEnemy(self,enemy):
        if enemy in self.ENEMY:
            self.ENEMY.remove(enemy)

    def search(self):
        description = "\n"
        length = len(self.items)
        if length:
            description = "\nYou see"
            if length > 1:
                for i in range(length):
                    if (i == length-1):
                        description = description+" and a "+self.items[i].name + ".\n"
                    else:
                        description = description + " a "+self.items[i].name + ","
            else:
                description = description + " a " +self.items[0].name + ".\n"
        
        if self.ENEMY:
            for enemy in self.ENEMY: 
                if enemy.alive:
                    description = description + enemy.name + " is " + choice(["standing in the corner.\n","wandering around.\n","reading a book.\n","creating a grand unified field theory.\n","eating a frighteningly large burrito.\n","playing runescape.\n","browsing math memes .\n","watching the Big Lez show on full volume.\n","eating a Big Mac.\n"])
                else:
                    description = description + "Oh look, its the " + choice(["decaying ", "broken ", "bloodied ", "mutilated "]) + choice(["corpse of ", "body of ", "cadaver of ", "hunk of meat that used to be ", "remains of "]) + enemy.name + ".\n"
        if self.interact:
            for item in self.interact:  
                description = description + item.info + "\n"
                
        if (description == ""):
            description = "\nThere isn't a whole lot to see."
            
        return description



