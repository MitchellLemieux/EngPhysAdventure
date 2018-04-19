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
    def __init__(self,name,location,image,info,worn,stats):
        self.name = str(name)
        self.image = str(image) 
        self.info = str(info)
        self.worn = str(worn)
        self.stats = stats
        self.location = location
    
class Character: #When the equip function is called we need to make sure the item is actually in the room
    
    def __init__(self,name,location,health,inv,emptyinv):
        self.name = str(name)
        self.location = location
        self.inv = inv
        self.emptyinv = emptyinv
        self.health = health
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats)
        self.alive = True
        
        for i in inv:
            inv[i].location = self.location
        
    def updateStats(self):
        self.stats = tupleAdd(self.inv['head'].stats,self.inv['body'].stats,self.inv['hand'].stats,self.inv['off-hand'].stats)
        
    def equip(self,Equip):
        drop = 0
        if self.inv[Equip.worn] == Equip:
            print 'This item is already equipped'
        elif (self.location == list(Equip.location) and self.inv[Equip.worn] == self.emptyinv[Equip.worn]):
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print Equip.info
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + ".\n"
        elif(self.location == list(Equip.location)):
            drop = self.inv[Equip.worn]
            self.inv[Equip.worn] = Equip
            Equip.location = self.location
            print Equip.info
            print "You've equipped the " + Equip.name +' to your ' + Equip.worn + ', the ' + drop.name + ' has been dropped.'
        else:
            print "That doesn't seem to be around here."
        self.updateStats()
        return drop

    def drop(self,Equip):
        drop = 0
        if(Equip == self.inv[Equip.worn]):
            self.inv[Equip.worn] = self.emptyinv[Equip.worn]
            print "You've dropped the " + Equip.name
            drop = Equip
        else:
            print "You aren't carrying that item."
        self.updateStats()
        return drop

    def move(self,direction):
        if (direction == 'f'):
            self.location[1] += 1
        if (direction == 'b'):
            self.location[1] -= 1
        if (direction == 'l'):
            self.location[0] -=  1
        if (direction == 'r'):
            self.location[0] += 1
        if (direction == 'u'):
            self.location[2] += 1
        if (direction == 'd'):
            self.location[2] -= 1

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
        
class Interact:
    def __init__(self,name,location,info,Sinfo,need,drop):
        self.name = name
        self.location = location
        self.info = info
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
            item.location = self.coords
            
    def placeEnemy(self,Enemy):
        self.ENEMY.append(Enemy)
        Enemy.location = self.coords
        
    def placeInteract(self,Interact):
        self.interact.append(Interact)
        Interact.location = self.coords
        
    
    def Remove(self,item):
        if item in self.items:
            self.items.remove(item)
            
    def RemoveEnemy(self,enemy):
        if enemy in self.ENEMY:
            self.ENEMY.remove(item)

    def search(self):
        description = ""
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
                    description = description + "\n" + enemy.name + " is " + choice(["standing in the corner.\n","wandering around.\n","reading a book.\n","creating a grand unified field theory.\n","eating a frighteningly large burrito.\n","playing runescape.\n"])
                else:
                    description = description + "\nOh look, its the " + choice(["decaying ", "broken ", "bloodied ", "mutilated "]) + choice(["corpse of ", "body of ", "cadaver of", "hunk of meat that used to be ", "remains of "]) + enemy.name + ".\n"
        if self.interact:
            for item in self.interact:  
                description = description + item.info + "\n"
                
        if (description == ""):
            description = "\nThere isn't a whole lot to see.\n"
            
        return description



