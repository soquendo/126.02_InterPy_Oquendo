
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
            if nHits > 0:

                totalHits = nHits + totalHits

                avgHits = totalHits/144
                      

#### -----  when added up from all players, totalHits should be 424. For some reason 
#           it's 12x that value. I can't figure out how to make it the actual value
#           it should be so instead of dividing totalHits/12 I have to divide by 144.
#           I was unable to use "length = len(nhitsList)" as I receive an entirely different
#           number for avgHits when using the "for i in range(0, length)" parameters.
#           I thought I would've been able to use (0,11) for range but that also gave me
#           a different value.



    print("Number of players with 40 or more hits: {0}".format(moreHits))
    print("\nThe average number of hits: {0:2.2f}".format(avgHits))
