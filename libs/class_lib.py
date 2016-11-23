'''
Created on 9 sep. 2015

@author: Samsung
'''

import os
from libs.config import Config
from msilib.schema import ReserveCost

config = Config()


spearmandef = ([2,2],1,5,2, "Yes sire, we can fight") 
#citizensdef = [peassantdef, spearmandef]

#Define buildings (cost, room, offense, defense)
housedef = (10, 5, 0, 0)

#Define crafts (produce, )
woodcutterprod = 2


# Super class
class Man:    
    def __init__(self, food, wood, eat, offense, defense, greating):
        self.food     = food
        self.wood     = wood 
        self.eat      = eat
        self.offense  = offense
        self.defense  = defense
        self.greating = greating
        
        self.cost = [self.food,self.wood]
    
    def cost(self):
        return self.cost
        
    def costString(self):
        return "Food %3s\nWood %3s" % (self.food,self.wood)
            
    def dailyfood(self):
        return self.eat
    
    def attack(self):
        return self.offense, self.defense
    
    def greating(self):
        return self.greating  

# Subclasses of Man
class Peassant(Man):
    
    def __init__(self):
        Man.__init__(self, config.getConfig("peassantdef","food"),
                           config.getConfig("peassantdef","wood"),
                           config.getConfig("peassantdef","eat"),
                           config.getConfig("peassantdef","offense"),
                           config.getConfig("peassantdef","defense"),
                           config.getConfig("peassantdef","greating") )

    def produce(self):
        pass



class Spearman(Man):
    def __init__(self):
        #Man.__init__(self, peassantdef[0], peassantdef[1], peassantdef[2], peassantdef[3], peassantdef[4])
        Man.__init__(self, *spearmandef)
        
    def fight(self):
        pass

        
# Super class
class Building:
    def __init__(self, cost, offense, defense):
        self.cost    = cost 
        self.offense = offense
        self.defense = defense
        
    def attack(self):
        return self.offense, self.defense    
        

class House(Building):
    def __init__(self, room):
        Building.__init__(self, cost, offense, defense)
        self.room = room


        
        
            