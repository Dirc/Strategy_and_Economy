'''
Created on 9 sep. 2015

@author: Samsung
'''
from libs.man import Peassant


print "\n-----------\n"

peassant_grp = set([])
peassant = Peassant()
peassant_grp.add(peassant)
peassant = Peassant()
peassant_grp.add(peassant)
peassant = Peassant()
peassant_grp.add(peassant)
print peassant_grp

print "\n-----------\n"




#helper_functions.addPeassant(peassant_grp)
#helper_functions.addPeassant(peassant_grp)

for pes in peassant_grp:
    print pes.dailyfood()
print len(peassant_grp)



print "\n-----------\n"

