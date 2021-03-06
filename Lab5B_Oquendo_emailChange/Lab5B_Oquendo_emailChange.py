
#Sebastian Oquendo
#SE 126.02
#02-16-22
#Lab5B

#--------------------------------------------

#   lab5B       -   file stored in location defined in open
#   col         -   used to read one column at a time from file

#   fname       =   employee first name
#   lname       =   employee last name
#   phone       =   employee phone number
#   email       =   employee email
#   dept        =   employee department
#   deptPos     =   employee position in department
#   newEmails   =   new list of corrected emails

#--------------------------------------------

#   Using the “sequential search” write a program that changes the email
#   address for all employees who work in the MIS Department.  Currently 
#   all employees  “top-level-domain (TLD) is .com.  .com should be changed
#   to .net for all employees in the MIS Deplartment.  You must use a
#   sequential search. You may use a for loop or a while loop when searching.
#   Before the progrqam exits display the number of addresses that were
#   changed. You must use a function that searches for the email address and
#   a function that changes the email address.
#--------------------------------------------

import csv

fname = []
lname = []
phone = []
email = []
dept = []
deptPos = []
newEmails = []

#--------------------------------------------

def deptSearch():
    for x in range(0, len(dept)):
        if dept[x] == "MIS":
            changeEmail(x)
           

def changeEmail(x):
    newEmail = email[x].replace(".com", ".net")
    newEmails.append(newEmail)
               
#--------------------------------------------

with open("D:\Lab5B.txt") as txtfile:
    lab5B = csv.reader(txtfile)

    for col in lab5B:
        fname.append(col[0])
        lname.append(col[1])
        phone.append(col[2])
        email.append(col[3])
        dept.append(col[4])
        deptPos.append(col[5])
        

#----------------------------------------------

fixedEm = 0

deptSearch()

for i in range(0, len(newEmails)):
    fixedEm += 1
        
print("\nTotal Records Corrected: {0}".format(fixedEm))

print("\nProcess Complete")
