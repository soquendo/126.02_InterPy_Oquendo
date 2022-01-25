
#Sebastian Oquendo
#SE126.02
#Lab 2B
#01-23-22


# file          is the file stored in the location defined in open     
# row           is used to read one row at a time from file

#-----------------------------

#variables
#   compType     = states whether machine is desktop or laptop
#   brand        = computer brand
#   cpuType      = number of people currently registered to attend
#   ramType      = size of RAM
#   firstDisk    = size capacity of first disk
#   totalHDD     = number of hard drives
#   secondDisk   = size capacity of second disk if available
#   sysOS        = operating system
#   yr           = year

#-----------------------------

import csv

totalComp = 0

with open("D:\lab2b-1.csv") as csvfile:
    file = csv.reader(csvfile)
    print("Type     Brand     CPU   RAM  1st Disk   No HDD    2nd Disk    OS  YR")

    for column in file:

        totalComp += 1

        compType = column[0]
        if compType == "D":
            compType == "Desktop"
        if compType == "L":
            compType == "Laptop"

        brand = column[1]
        cpuType = column[2]
        ramType = column[3]
        firstDisk = column[4]
        totalHDD = int(column[5])
        
        if totalHDD > 1:
          secondDisk = column[6]
          sysOS = column[7]
          yr = column[8]
        else:
          sysOS = column[6]
          yr = column[7]
          secondDisk = ""


      #secondDisk = column[6]
      #sysOS = column[7]
      #yr = column[8]


          
    print("{0:8} {1:9} {2:5} {3:4} {4:4} {5:8} {6:8} {7:3}".format(compType, brand, cpuType, ramType, firstDisk, totalHDD, secondDisk, sysOS))




print("\n")