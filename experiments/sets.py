'''
Created on 7 feb. 2016

@author: Eric Cornet
'''

from libs import class_lib

peassant_grp = set([])
woodcutter_grp = set([])

# Start citizens
peassant = class_lib.Peassant
peassant_grp.add(peassant)
peassant = class_lib.Peassant
peassant_grp.add(peassant)

print len(peassant_grp)


def actionPromt():
    print "Woodcutters     w"
    choice = raw_input("Choose job: ")
    return choice

def action(worker, choice):
    global peassant_grp, woodcutter_grp
    if choice == "w":
        woodcutter_grp.add(worker)

def newWorkers():    
    global peassant_grp, woodcutter_grp
    print "New citizens have arrived:"
    for worker in peassant_grp:
        print "Have some job for me, Sire?"
        choice = actionPromt()
        action(worker, choice)

newWorkers()


print len(peassant_grp)
print len(woodcutter_grp)
