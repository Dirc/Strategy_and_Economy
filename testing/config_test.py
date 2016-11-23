'''
Created on 25 jan. 2016

@author: Dirc
'''

import os
from libs.config import Config

config = Config()

print config.getConfig("peassantdef","food") 
print config.getConfig("peassantdef","wood") 
print config.getConfig("peassantdef","eat") 
print config.getConfig("peassantdef","offense") 
print config.getConfig("peassantdef","defense") 
print config.getConfig("peassantdef","greating") 


print
#print config.infoConfig()
peassantdef = config.getConfig("peassantdef", "eat")
print type(peassantdef)
print peassantdef


