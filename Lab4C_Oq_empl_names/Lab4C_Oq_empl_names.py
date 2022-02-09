#Sebastian Oquendo
#SE 126.02
#02-09-22
#Lab4C

#--------------

# 0  fName   =   employee first name
# 1  lName   =   employee last name
# 2  emPhone =   employee phone number
# 3  emem    =   employee email
# 4  dept    =   employee department
# 5  emPos   =   employee position in department



#--------------

import csv

with open("D:\Lab4c.csv") as csvfile:
    lab4c = csv.reader(csvfile)
 

    fnameList = []
    lnameList = []
    emphoneList = []
    ememList = []
    deptList = []
    emposList = []
    

    for col in lab4c:
        fnameList.append(col[0])
        lnameList.append(col[1])
        emphoneList.append(col[2])
        ememList.append(col[3])
        deptList.append(col[4])
        emposList.append(col[5])


    
    length = len(lnameList)
    found = "False"
    search = input("Enter a name ")
    for pos in range(0, length):
        if(search == names[pos]):
            found = "True"
            position = pos
        if found == "True":
            print(names[position])
        else:
            print("Name not on list")
