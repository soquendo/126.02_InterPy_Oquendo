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

for b in range(0, len(dept)):
    if dept[b] == "MIS":
       totalSalaryMIS = salary[b] + totalSalaryMIS
       avgSalaryMIS = totalSalaryMIS/(len(salary[b]))

for d in range(0, len(salary)):
    if salary[d] > 1:
        totalSalary = salary[d] + totalSalary
        fivepct = totalSalary * .05




        
#B
print("Average salary for MIS Dept.: ${0:7.2f}".format(avgSalaryMIS))

#D
print("Total cost of increasing all employee salaries by 5%: ${0:9.2f}".format(fivepct))

#print(salary[x].ljust(7), lname[x].cjust(20), dept[x].rjust(15))
print("Total employees: ", len(salary))


#for i in range(0,5):

#for i in range(length of list -1, 6, -1)

#for i in range(length of list -1, len of list - 5, -1)