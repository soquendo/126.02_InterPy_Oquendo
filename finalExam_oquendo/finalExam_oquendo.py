
#   Sebastian Oquendo
#   SE126.02
#   Final Exam
#   03-16-22

#   =======================================================================

#   Write a program that will sort the file in alphabetical order (last name)
#   Once the data is sorted display the first 15 records on the screen. Each 
#   row should display the entire record. 
#   (last name, first name, phone number and state)
#
#	After the first 15 records are displayed search the file for a specific
#	last name. If the name is found display the available information on 
#	the person to the screen. If the name is not found display the 
#	error message #	"Not Found!!!". You must use the binary search.

#   =======================================================================

#   exam1   =   file stored in location define in open
#   col     =   used to read one column at a time from file
#
#   fname   =   person's first name
#   lname   =   person's last name
#   state   =   person's state
#   phone   =   person's phone number
#
#   -----------------------------------------

import csv

fname = []
lname = []
state = []
phone = []
tempList = []
abcList = []

with open("D:\exam1.txt") as txtfile:
    exam1 = csv.reader(txtfile)

    for col in exam1:
        fname.append(col[0])
        lname.append(col[1])
        state.append(col[2])
        phone.append(col[3])

def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

def mySort(lname, fname, phone, state):
    length = len(lname)
    for i in range(0, length):
        for j in range(0, length -1):
            if (lname[j] > lname[j + 1]):

                swap(lname, j)
                swap(fname, j)
                swap(phone, j)
                swap(state, j)

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
        for i in range(0, 1):
            print("\n{0:10} {1:10}  {2:12}  {3:5}\n".format(lname[guess], fname[guess], phone[guess], state[guess]))

        #print("\nUser found")
        #print("\n\t\t{0:9}{1:9}".format(fname[guess], lname[guess]))
        #print("\n\t{0:5} \t{1:12}".format(state[guess], phone[guess]))
    else:
        print ("\nNot Found!!!")

length = len(lname)

mySort(lname, fname, phone, state)

for i in range(0, 15):
    abcList.append(lname[i] + fname[i] + phone[i] + state[i]) 

length = len(abcList)

print("\nDisplaying first 15 records..\n")
print("Last Name  First Name  Phone Number  State")
for i in range(0, length):
    
    print("{0:10} {1:10}  {2:12}  {3:5}".format(lname[i], fname[i], phone[i], state[i]))
print("\n")
    #print(lname[i], " ",   fname[i], " -      ", state[i], " -        ", phone[i])

nameSearch()



