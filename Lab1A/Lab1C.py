#Sebastian Oquendo
#SE126.02
#Lab1C
#01-12-22

#=============================

#VAR DICTIONARY

#roomCap = number of people allowed in room at one time
#numAttend = number of people looking to attend event
#overCap = number of people exceeding room capacity
#extra = amount of people who can still attend

#=============================

#FUNCTIONS

def cap():
    roomCap = int(input("\n\tWhat is the capacity of the room?: "))

    return roomCap

def attend():
    numAttend = int(input("\n\tHow many people are attending the event?: "))

    return numAttend

def register(roomCap, numAttend):
    difference = roomCap - numAttend

    return difference

def check():
    answer = input("\n\tDo you want to check another room? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        return newcheck

#=============================

#MAIN

answer = "y"

while answer == "y":
    
    cap()
    attend()
    register()

    #extra = roomCap - numAttend
    #overCap = numAttend - roomCap


    if difference > 0:

        print("\n\tThe conference can be held. {0} more people can attend.".format(extra))
        
    else:
        print("\n\t{0} people will have to be told they cannot attend the event.".format(overCap))

    while answer != "y" and answer != "n":
        
        answer = input("\n\tDo you want to check another room? [y/n]: ").lower()
    

#print ("Press any key to exit")