#   Sebastian Oquendo
#   SE126.02
#   03-09-22
#   Lab #9
#=========================================================

# Lab 9 will require to open a csv file sort it by last name then write the sorted list to a csv file

# The following commands will allow you to write lists to a csv file.

# import csv

# with open(path, 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(list 1)
#     writer.writerow(list 2)

# Before you upload the file make sure the path is "E:\Python126\Lab9BWrite.csv"

# Lab9Write.csv is the name of the file you are writing to.

# Read the data from this file sort the list on last name then write the last name and first name to the file LabWrite.csv.

#=========================================================


import csv

fname = []
lname = []
tempList = []



# Before you upload the file make sure the path is "E:\Python126\Lab9BWrite.csv"
with open("E:\Python126\Lab9BWrite.csv") as csvfile:
    lab9 = csv.reader(csvfile)

    for col in lab9:
        fname.append(col[0])
        lname.append(col[1])
    
def swap(list, x):
    temp = list[x]
    list[x] = list[x + 1]
    list[x + 1] = temp

def mySort(lname, fname):
    length = len(lname)
    for i in range(0, length):
        for j in range(0, length - 1):
            if (lname[j] > lname[j + 1]):

                swap(lname, j)
                swap(fname, j)

mySort(lname, fname)

for i in range(0, len(lname)):
    print(lname[i], ", ", fname[i])

# Before you upload the file make sure the path is "E:\Python126\Lab9BWrite.csv"
with open("E:\Python126\Lab9BWrite.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(lname)
    writer.writerow(fname)
