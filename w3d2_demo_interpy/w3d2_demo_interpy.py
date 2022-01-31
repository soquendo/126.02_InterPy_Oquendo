
#importing date class from datetime module
from datetime import date


months = ["", "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

#creating the date object of today's date
todays_date = date.today()
#td = date.today()

print("Current date: ", todays_date)

#fetching the current year, month and day of today
print("Current year:", todays_date.year)
print("Current month:", todays_date.month) #date.today().month
print("Current day:", todays_date.day) #importing date class form datetime module


print("\n\n")

month = months[todays_date.month]
print(month)

todays_month = date.today().month
print(todays_month)


#if todays_date.month == 1:
    #print("January")


#if todays_date.month() == 1:
#    month = "January"



names = ["Sally", "Larry", "Tom", "April", "Ken"]
ages = [ 22, 31, 18, 25, 40]

searchName = input("Person's name: ")


randomVar = -1
noName = len(names)
for x in range(0, noName):
    if (searchName == names[x]):
        found = x
        randomVar = 0


if (randomVar == 0):
    print(names[x], " is ", ages[found], " years old")
else:
    print("Error -- Name not found")


    #from 1-5000
    # first guess 2500, second 1250, third 625... add 1250+625 and divide by 2 .. answer is between 625 and 935.. add together 1560 .. div by 2.. 730
    # too low , add 935+730, 1665 /2 .. 837 .. 837+730 = 1572 / 2 .. 