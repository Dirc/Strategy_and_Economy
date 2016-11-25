'''
Created on 9 sep. 2015

@author: Dirc
'''

from libs.config import Config

config = Config()


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
    
    def __init__(self, non_used_option=None):
        Man.__init__(self, config.getConfig("peassantdef","food"),
                           config.getConfig("peassantdef","wood"),
                           config.getConfig("peassantdef","eat"),
                           config.getConfig("peassantdef","offense"),
                           config.getConfig("peassantdef","defense"),
                           config.getConfig("peassantdef","greating") )
        self.function = "unemployed"
        
        self.dummy = non_used_option

    def setFunction(self,new_function):
        self.function = new_function
    
    def getFunction(self):
        return self.function
            
    def produce(self):
        pass


class Spearman(Man):

    def __init__(self, non_used_option=None):
        Man.__init__(self, config.getConfig("peassantdef","food"),
                           config.getConfig("peassantdef","wood"),
                           config.getConfig("peassantdef","eat"),
                           config.getConfig("peassantdef","offense"),
                           config.getConfig("peassantdef","defense"),
                           config.getConfig("peassantdef","greating") )
        self.dummy = non_used_option
        
    def fight(self):
        pass
