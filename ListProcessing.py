# file          is the file stored in the location defined in open     
# row           is used to read one row at a time from file
#
# Notes:
#   row[0] refers to the first piece of data in the row --- id number
#   row[1] refers to the second piece of data in the row -- age
#   row[2] refers to the third piece of data in the row --- registered to vote
#   row[3] refers to the fourth piece of data in the row -- voted
# 
# Variables used:
#   id                      individuals ID number
#   age                     individuals age
#   registered              individual registered to vote
#   voted                   individual voted 
#   notEligibleToVote       individuals not eligible to vote
#   oldEnoughNotReg         individuals who are old enough to vote but did not register
#   eligibleToVoteNoVote    individuals who are eligible to vote but did vote
#   numberVoted             individuals who voted
#   records                 number of records processed
#   row                     represents a row in the csv file
#==========================================================================================

import csv

idList = []
ageList = []
regList = []
votedList = []

numberVoted = 0
notEligibleToVote = 0
oldEnoughNotReg = 0
eligibleToVoteNoVote = 0
numberVoted = 0
numRecords = 0

#===== Printing a list (all are empty) ====
print("idList = ", idList)
print("ageList = ", ageList)
print("RegList = ", regList)
print("votedList = ", votedList, "\n")

#===== Readings a CSV file into a list =====
with open("E:\EMT126\DemoVote.csv") as csvfile:
    file = csv.reader(csvfile)
    for row in file:
      idList.append(row[0])
      ageList.append(int(row[1]))
      regList.append(row[2])
      votedList.append(row[3])

#===== Printing a list =====
print("ID  =",idList, "\n")
print("age =",ageList, "\n")
print("Reg =",regList, "\n")
print("Voted =",votedList, "\n\n")

#===== Printing the size of each list =====
print("ID = ", len(idList))
print("age =", len(ageList))
print("Reg =", len(regList))
print("Voted =", len(votedList), "\n\n\n")

for i in range(0, 12):
    print(idList[i], ", ", ageList[i],  ", ", regList[i],  ", ", votedList[i])


