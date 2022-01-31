#Sebastian Oquendo
#SE126.02
#Lab 4A
#01-31-22


# lab4a         is the file stored in the location defined in open     
# col           is used to read one column at a time from file

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
#   totalComp    = total amount of computers
#   toReplaceD   = total number of desktops to replace
#   toReplaceL   = total number of laptops to replace
#   desktopCost  = total cost to replace outdated desktops
#   laptopCost   = total cost to replace outdated laptops

#-----------------------------

import csv

with open("D:\lab4a.csv") as csvfile:
    lab4a = csv.reader(csvfile)
    #print("Type     Brand     CPU   RAM  1st Disk   No HDD    2nd Disk    OS  YR")

    compList = []
    cbrandList = []
    cpuList = []
    ramList = []
    hddoneList = []
    whichhdList = []
    hdtwoList = []
    opsysList = []
    yearList = []

    desktopCost = 0
    laptopCost = 0
    toReplaceD = 0
    toReplaceL = 0
    moreRam = 0

    for col in lab4a:
        compList.append(col[0])
        cbrandList.append(col[1])
        cpuList.append(col[2])
        ramList.append(col[3])
        hddoneList.append(col[4])
        whichhdList.append(int(col[5]))

        compType = col[0]
        if compType == "D":
            compType = "Desktop"
        if compType == "L":
            compType = "Laptop"

        #2000 for desktop
        #1500 for laptop

        brand = col[1]
        if brand == "DL":
            brand = "Dell"
        if brand == "GW":
            brand = "Gateway"

        cpuType = col[2]
        ramType = int(col[3])

        length = len(ramList)
        for i in range(0, length):
            moreRam+= 1

        #if ramType > 8:
            #moreRam += 1

        firstDisk = col[4]
        totalHDD = int(col[5])
        
        if totalHDD > 1:
          secondDisk = col[6]
          sysOS = col[7]
          yr = int(col[8])

          hdtwoList.append(col[6])
          opsysList.append(col[7])
          yearList.append(int(col[8]))

          if compType == "Desktop":
            if yr <= 2020:
                desktopCost += 2000
                toReplaceD += 1
          elif compType == "Laptop":
            if yr <= 2020:
                laptopCost += 1500
                toReplaceL += 1

        else:
          sysOS = col[6]
          yr = int(col[7])
          secondDisk = " "

          opsysList.append(col[6])
          yearList.append(int(col[7]))

          if compType == "Desktop":
            if yr <= 2020:
                desktopCost += 2000
                toReplaceD += 1
          elif compType == "Laptop":
            if yr <= 2020:
                laptopCost += 1500
                toReplaceL += 1

print("There are {0} machines with RAM greater than 8GB".format(moreRam))

       
print("\n")
