'''
Created on 25 jan. 2016

@author: Dirc
'''

import os
import ConfigParser


class Config(object):
    
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.abs_base = os.path.dirname(os.path.dirname(__file__))
        self.conf_file =  os.path.join(self.abs_base,'conf','settings.cfg')
        self.config.read(self.conf_file)

    def getConfig(self, section, prop):
        return self.config.get(section, prop)
    
    def infoConfig(self):
        return self.app_base, self.config_file



