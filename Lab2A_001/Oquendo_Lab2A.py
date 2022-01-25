

#Sebastian Oquendo
#SE126.02
#Lab 2A
#01-19-22


# file          is the file stored in the location defined in open     
# row           is used to read one row at a time from file
#
#   row[0] refers to the first piece of data in the row --- roomName
#   row[1] refers to the second piece of data in the row -- maxLimit
#   row[2] refers to the third piece of data in the row --- currentReg

#-----------------------------

#variables
#   roomName        = room in use
#   maxLimit        = maximum number of people allowed in room at one time
#   currentReg      = number of people currently registered to attend
#   roomsChecked    = total number of rooms checked
#   overLimit       = total number of rooms over the limit

#-----------------------------

import csv

roomsChecked = 0
overLimit = 0

with open("D:\lab2a.csv") as csvfile:
    file = csv.reader(csvfile)
    print("Room                            Max                Min                Over")

    for row in file:
      roomName = row[0]
      maxLimit = int(row[1])
      currentReg = int(row[2])

      difference = int(row[1]) - int(row[2])

      if currentReg <= maxLimit:
          roomsChecked +=1

      if currentReg > maxLimit:
          overCap = currentReg - maxLimit
          overLimit +=1
          roomsChecked +=1


          
          print("{0:20} {1:14} {2:18} {3:18}".format(roomName, maxLimit, currentReg, overCap))


print("\nProcessed {0} records".format(roomsChecked))
print("There are {0} rooms over the limit".format(overLimit))
print("\n")