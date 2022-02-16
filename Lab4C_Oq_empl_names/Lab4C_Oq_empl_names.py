#Sebastian Oquendo
#SE 126.02
#02-09-22
#Lab4C

#------------------------------------------------------------------


#   lab4c           -   file stored in location defined in open
#   col             -   used to read one column at a time from file

#   fnameList       =   employee first name
#   lnameList       =   employee last name
#   emphoneList     =   employee phone number
#   ememList        =   employee email
#   deptList        =   employee department
#   emposList       =   employee position in department
#   empCount        =   total number of employees

#-----------------------------------------------------------------

import csv

fnameList = []
lnameList = []
emphoneList = []
ememList = []
deptList = []
emposList = []

empCount = 0

with open("D:\Lab4c.txt") as txtfile:
    lab4c = csv.reader(txtfile)

    for col in lab4c:
        fnameList.append(col[0])
        lnameList.append(col[1])
        emphoneList.append(col[2])
        ememList.append(col[3])
        deptList.append(col[4])
        emposList.append(col[5])
    


answer = "Y"
while answer == "Y":

    length = len(lnameList)
    found = "False"

    search = input("\nEnter employee's last name (case-sensitive): ")
 
    for x in range(0, len(lnameList)):
        if search == lnameList[x]:
            found = "True"
            position = x

    if found == "True":
       print("\n\t{0:8}{1:8}".format(fnameList[position], lnameList[position]))
       print("\n\t{0:11} \t{1:32}".format(emphoneList[position], ememList[position]))
       print("\n\t{0:10} \t{1:13}".format(deptList[position], emposList[position]))
        
       print("\nTotal Records Searched Through: {0}".format(len(lnameList)))
    else:
        print("\n*ERROR: User Not Found*")
         
        print("\nTotal Records Searched Through: {0}".format(len(lnameList)))

    answer = input("\nWould you like to search again? [Y/N]: ").upper()
 
    

print("\nSearch complete")