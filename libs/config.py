'''
Created on 25 jan. 2016

@author: Dirc

TODO:
- 
'''

import os
import ConfigParser


class Config(object):
    
    def __init__(self, conf_file = 'conf/settings.cfg'):
        self.rel_conf_file = conf_file 
        self.config        = ConfigParser.ConfigParser()
        self.app_base      = os.path.dirname(os.path.dirname(__file__))
        self.conf_file     = os.path.join(self.app_base,self.rel_conf_file)
        self.config.read(self.conf_file)

    def getConfig(self, section, prop):
        return self.config.get(section, prop)
    
    def infoConfig(self):
        return self.app_base, self.conf_file
    
    def getSections(self):
        return self.config.sections()


if __name__ == "__main__":
    c = Config()
    print c.infoConfig()
