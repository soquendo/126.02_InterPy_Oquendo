
#Sebastian Oquendo
#SE 126.02
#02-20-22
#Lab6A

#------------------------------------------------------------------

#   lab6a       -   file stored in location defined in open
#   col         -   used to read one column at a time from file

#   fname       =   employee first name
#   lname       =   employee last name
#   phone       =   employee phone number
#   email       =   employee email
#   dept        =   employee department
#   deptPos     =   employee position in department

#--------------------------------------------------

import csv

fname = []
lname = []
phone = []
email = []
dept = []
deptPos = []

#==================================

def nameSearch():
    search = input("\nEnter employee's last name (case-sensitive): ")

    min = 0
    max = len(lname)-1
    guess = int((min+max)/2)
    while search != lname[guess] and min <= max:
        if search < lname[guess]:
            max = guess-1
        else:
            min = guess+1
        guess = int((min+max)/2)
    
    nameFound(search, guess)


def nameFound(search, guess):
    if search == lname[guess]:
        print("\nUser found")
        print("\n\t\t{0:8}{1:8}".format(fname[guess], lname[guess]))
        print("\n\t{0:11} \t{1:32}".format(phone[guess], email[guess]))
        print("\n\t{0:10} \t{1:13}".format(dept[guess], deptPos[guess]))
    else:
        print ("\nNot found")

#==================================

with open("D:\Lab6a-2.csv") as csvfile:
    lab6a = csv.reader(csvfile)

    for col in lab6a:
        fname.append(col[0])
        lname.append(col[1])
        phone.append(col[2])
        email.append(col[3])
        dept.append(col[4])
        deptPos.append(col[5])

nameSearch()

