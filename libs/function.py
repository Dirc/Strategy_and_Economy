'''
Created on 25 nov. 2016

@author: Eric Cornet
'''

class Function(object):
    '''
    classdocs
    '''


    def __init__(self, name, production):
        '''
        Constructor
        '''
        self.name       = name
        self.production = production
    
    def getName(self):
        return self.name
    
    def production(self):
        return self.production
    