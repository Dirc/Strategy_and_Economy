'''
Created on 24 jan. 2016

@author: Dirc
'''

from libs.class_lib import Peassant

def feedingGroup(man_grouplist):
    total = 0
    for group in man_grouplist:
        for man in group:
            total += man.dailyfood()
    return total


def woodProduction(woodcutter_grp, woodcutterprod):
    woodprod = len(woodcutter_grp) * woodcutterprod      
    return woodprod

# NIET AF!!!!
def addPeassant(peassant_grp):
    #global peassant_grp
    peassant = Peassant()
    peassant_grp.add(peassant)
    return peassant_grp