'''
Created on 25 nov. 2016

@author: Eric Cornet
'''

# Super class
class Building:
    def __init__(self, wood, stone, offense, defense):
        self.wood    = wood
        self.stone   = stone
        self.offense = offense
        self.defense = defense
        self.cost    = [self.wood, self.stone]
        
    def attack(self):
        return self.offense, self.defense    
        

class House(Building):
    def __init__(self):
        Building.__init__(self, config.getConfig("house","wood"),
                                config.getConfig("house","stone"),
                                config.getConfig("house","offense"),
                                config.getConfig("house","defense"),)
        self.room = config.getConfig("house","room")

    def add(self):
        pass
        
