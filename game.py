'''
Created on 9 sep. 2015

@author: Samsung
'''
from libs import man
from libs import helper_functions

# Global and initial variables
#Define clan members ([food,wood], eat, offense, defense, greating)
#peassantdef = [1,1,1,1, "Morning sir, have some work for me?"]
peassantdef = ([1,0],1,1,1, "Morning sir, have some work for me?")


spearmandef = ([2,2],1,5,2, "Yes sire, we can fight") 
#citizensdef = [peassantdef, spearmandef]

#Define buildings (cost, room, offense, defense)
housedef = (10, 5, 0, 0)

#Define crafts (produce, )
woodcutterprod = 2


# Stock [food, wood, stone]

#foodstock     = [food, water, beer]
#materialstock = [wood, stone, iron]
#craftstock    = [showel, saw, hamer]


# Helper functions
# Initialise Game
def startGame():
    global game, stock, day, daycount
    global peassant_grp, woodcutter_grp 
    global spearman_grp 
    global house_grp
    global man_grouplist, building_grouplist
    game = True
    daycount = 0
    stock = [0,0,0] 
    
    # Set groups
    peassant_grp = set([])
    woodcutter_grp = set([])
    spearman_grp = set([])
    house_grp = set([])
    
    # Group of groups
    man_grouplist = [peassant_grp,spearman_grp]
    building_grouplist = [house_grp]
    
    # Start citizens
    peassant = man.Peassant
    peassant_grp.add(peassant)
        
    print "Welcome in your village!"


# Funtions and Classes
def economyStatus(food, wood, stone, peassants, woodcutter, spearmen, houses, day):
    print "Current status of your economy"
    print "Day:       %6s" % day 
    print "Current stock"
    print "Food:      %6s" % food
    print "Wood:      %6s" % wood
    print "Stone:     %6s" % stone
    print "Clan members"
    print "Peassants: %6s" % peassants
    print "Woodcutter %6s" % woodcutter
    print "Spearman:  %6s" % spearmen
    print "Buildings"
    print "House      %6s" % houses

def backToMenu():
    print
    print "Choice"
    print "0    Back to menu"
    back_to_menu = raw_input("Choice: ")
    if back_to_menu != "":
        menu()
    else:
        print "Please choise 0."    

def actionMenu():
    print 
    print "Action menu"
    print "Nr:   Action:            "
    print "1     Hire Woodcutter    "
    #print "2     Hire Stone Miner   "
    #print "3     Hire Fisherman     "    
    print "0     Back to menu"
    print



def action():
    global game, stock, day, daycount
    global peassant_grp, woodcutter_grp 
    global spearman_grp 
    global house_grp
    choice = ""
    while choice != "0":
        actionMenu()
        choice = raw_input("Action choice: ")
        if choice == "1":
            peassant_grp.pop()
            
            # Pay cost
            stock[1] -= peassantdef[0]
            # Create
            peassant = man.Man(*peassantdef)
            peassant_grp.add(peassant)
            # Message
            print "We have a new peassant in our village\n"
        elif choice == "2":
            stock[1] -= spearmandef[0]
            spearman = man.Man(*spearmandef)
            spearman_grp.add(spearman)
            print "Good, we can use new strong spearman!\n"
        elif choice == "3":
            stock[1] -= housedef[0]
            house = man.Building(*housedef)
            house_grp.add(house)
            print "We have build a new house.\n"
        elif choice == "4":
            if len(peassant_grp) <= 0:
                print "Sorry, not enough peassants available"
            else:
                peassant_grp.pop()
                peassant = man.Man(*peassantdef)
                woodcutter_grp.add(peassant)
                print "New woodcutter! Number of peassant left: " + str(len(peassant_grp)) 
        else:
            print "Please choose from the action menu.\n"
    else:
        menu()


def menu():
    #Economy Statistics
    economyStatus(stock[0], stock[1], stock[2], len(peassant_grp), len(woodcutter_grp), len(spearman_grp), len(house_grp), daycount)
    print "\n" * 2
    print "Choose"
    #print "1    View current state of your economy"
    print "2    View action menu"
    print 
    print "0    Next day"
    print "\n" * 2
    menuchoice = raw_input("Menu choice: ")
    if menuchoice == "0":
        newday()
    elif menuchoice == "2":
        #actionMenu()
        action()
    else:
        print "What?!"

def newday():
    global daycount, stock
    # new day    
    daycount += 1
    # Food for citizens
    todaysfood = helper_functions.feedingGroup(man_grouplist)
    stock[0] -= todaysfood
    stock[1] += helper_functions.woodProduction(woodcutter_grp, woodcutterprod) 
    
    print "Good morning on this lovely new day.\nCitizens have eaten " + str(todaysfood) + " of food"    

# Event handlers
       


# Start Game
startGame()

while game:
    #print "\n" * 1
    menu()
    print "\n"
  
