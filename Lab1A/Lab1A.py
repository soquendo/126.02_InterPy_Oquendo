#Sebastian Oquendo
#SE126.02
#Lab1A
#01-12-22


#roomCap = number of people allowed in room at one time
#numAttend = number of people looking to attend event
#overCap = number of people exceeding room capacity
#extra = amount of people who can still attend

#==================
answer = "y"

while answer == "y":
    

    roomCap = int(input("\n\tWhat is the capacity of the room?: "))

    numAttend = int(input("\n\tHow many people are attending the event?: "))

    extra = roomCap - numAttend

    overCap = numAttend - roomCap

    if roomCap > numAttend:
      
        print("\n\tThe conference can be held. {0} more people can attend.".format(extra))
        
    else:
        print("\n\t{0} people will have to be told they cannot attend the event.".format(overCap))
       
    answer = input("\tDo you want to check another room? [y/n]: ").lower()

   
    

#print ("Press any key to exit")