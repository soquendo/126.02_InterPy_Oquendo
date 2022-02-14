#Sebastian Oquendo
#SE 126.02
#02-09-22
#Lab4C

#------------------------------------------------------------------


#   Lab4c       -   file stored in location defined in open
#   col         -   used to read one column at a time from file

#   fName       =   employee first name
#   lName       =   employee last name
#   emPhone     =   employee phone number
#   emEmail        =   employee email
#   dept        =   employee department
#   emPos       =   employee position in department
#   empCount    =   total number of employees

#-----------------------------------------------------------------


def nameSearch(search):

        for pos in range(0, 73):
            if search == lnameList[pos]:
                #empInfo()
                print("\nTotal Employees Searched Through: {0}".format(len(lnameList)))
                print("\n {0}\n {1}\n {2}\n {3}\n {4}\n {5}\n".format(fnameList[pos], lnameList[pos], emphoneList[pos], ememList[pos], deptList[pos], emposList[pos]))

            else:
                print("\n*ERROR: User Not Found*")
                print("\nTotal Employees Searched Through: {0}".format(len(lnameList)))

                  

def empInfo():

        print("{0:8} {1:8}".format(fnameList[pos], lnameList[pos]))
        print("{0:11} {1:32}".format(emphoneList[pos], ememList[pos]))
        print("{0:10} {1:13}".format(deptList[pos], emposList[pos]))



#-----------------------------------------------------------------------

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
    
answer = "y"
while answer == "y":

    search = input("Enter employee's last name (case-sensitive): ")
    nameSearch(search)
    