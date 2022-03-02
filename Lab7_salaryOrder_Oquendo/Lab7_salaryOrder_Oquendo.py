#   Sebastian Oquendo
#   Lab 7A
#   SE126.02
#   02-23-22

#   lab7        -   file stored in location defined in open
#   col         -   used to read one column at a time from file

#   fname       =   employee first name
#   lname       =   employee last name
#   dept        =   employee department
#   deptPos     =   employee position in department
#   salary      =   employee salary
#   totalSalary =   total salaries of all employees


#==================================================

#   Write a Python program that will:
#   A.  List the 10 highest salaries in order.
#       a. When listing the salaries include, on the same line, the salary, last name and 
#   department
#   B. Determine the average annual salary for all employees in the MIS Department.
#   C. List the 10 lowest salaries in order.
#       a. When listing the salaries include, on the same line, the salary, last name and 
#       department
#   D. What would it cost the company if every employee received a 5% raise.
#   E. Sort the data in Alphabetical order by department.
#       a. List the first 5 and the last 5 records.

#==================================================

import csv

fname = []
lname = []
dept = []
deptPos = []
salary = []

tempList = []
abcList = []

homeDept = []
invDept = []
lifeDept = []
misDept = []
transDept = []

with open("D:\Lab7.csv") as csvfile:
    lab7 = csv.reader(csvfile)

    for col in lab7:
        fname.append(col[0])
        lname.append(col[1])
        dept.append(col[2])
        deptPos.append(col[3])
        salary.append(int(col[4]))

totalSalary = 0
totalSalaryMIS = 0

def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

def mySort(lname, salary, dept):
    length = len(lname)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (salary[j] > salary[j + 1]):

                swap(lname, j)
                swap(salary, j)
                swap(dept, j)


def abc(fname, lname, dept):
    for i in range(0, length):
        for j in range(0, length - 1):
            if (lname[j] > lname[j + 1]):
            
                swap(fname, j)
                swap(lname, j)
                swap(dept, j)

length = len(lname)

for i in range(0, length):
    tempList.append(lname[i] + dept[i])  

for b in range(0, len(dept)):
    if dept[b] == "Investments":
        invDept.append(lname[b] + fname[b] + dept[b])
    if dept[b] == "Homeowners":
        homeDept.append(lname[b] + fname[b] + dept[b])
    if dept[b] == "Life":
        lifeDept.append(lname[b] + fname[b] + dept[b])
    if dept[b] == "MIS":
        misDept.append(lname[b] + fname[b] + dept[b])
    if dept[b] == "Transportation":
        transDept.append(lname[b] + fname[b] + dept[b])

for i in range(0, len(misDept)):
    if salary[i] > 1:
        totalSalaryMIS = salary[i] + totalSalaryMIS
        avgSalaryMIS = totalSalaryMIS/(len(misDept))

for d in range(0, len(salary)):
    if salary[d] > 1:
        totalSalary = salary[d] + totalSalary
        fivepct = totalSalary * .05

mySort(lname, salary, dept)

#A

print("\nHighest Company Salaries")
for i in range(length -1, length -11, -1):
    print(salary[i], lname[i], dept[i])
        

#B
print("\nAverage salary for MIS Dept.: ${0:7.2f}".format(avgSalaryMIS))


#C
print("\nLowest Company Salaries")
#print("\n\nSalary, Last Name, Dept")
for s in range(9, -1, -1):
    print(salary[s], lname[s], dept[s])


#D
print("\nCost of 5% raise for all employees: ${0:9.2f}".format(fivepct))


#E -------------- couldn't make it work --------
#abc(fname, lname, dept)
#for i in range(0, 4):
   #if dept[i] == "Investments":
       #print(lname[i], fname[i], dept[i])

