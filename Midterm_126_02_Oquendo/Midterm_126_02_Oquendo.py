
#-- Sebastian Oquendo
#-- SE126.02
#-- 02-09-22
#-- Midterm




# midterm       is the file stored in the location defined in open     
# col           is used to read one column at a time from file

# pName     =   player's name
# pRace     =   player's race
# pChar     =   player character
# nHits     =   number of hits
# moreHits  =   counter for players with 40+ hits
# totalHits =   total sum of hits for all players
# avgHits   =   average number of hits per player

#=================================

import csv

with open("D:\Midterm.csv") as csvfile:
    midterm = csv.reader(csvfile)

    pnameList = []
    praceList = []
    pcharList = []
    nhitsList = []

    #--- Player Name      Player Race         Player Character        Number of Hits -- 

    moreHits = 0
    totalHits = 0
    new_totalHits = 0

    for col in midterm:
        pnameList.append(col[0])
        praceList.append(col[1])
        pcharList.append(col[2])
        nhitsList.append(int(col[3]))

        pName = col[0]
        pRace = col[1]
        pChar = col[2]
        nHits = int(col[3])

        if nHits >= 40:
            moreHits +=1

            print("{0:10} {1:11}{2:7}{3:6}".format(pName, pRace, pChar, nHits))

        
        for i in range(0, 12):
            while nHits > 0:

                totalHits = nHits + totalHits

                avgHits = totalHits/12
                      
    print("Number of players with 40 or more hits: {0}".format(moreHits))
    print(totalHits)
    print(avgHits)
    



     


    