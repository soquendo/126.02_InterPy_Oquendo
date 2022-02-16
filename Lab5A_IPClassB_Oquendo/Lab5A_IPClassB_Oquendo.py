#   Sebastian Oquendo
#   Lab5A
#   02-16-22
#   SE126.02

#   lab5a   = file in location stored in location defined in open
#   col     = used to read one column at a time in file
#   ipclass = class of IP
#   ipfile  = list of from file
#   iplist  = first octet of each item
#   ip      = first octet casted as int

import csv

ipfile = []

with open("D:\Lab5a.txt") as txtfile:
    lab5a = csv.reader(txtfile)

    for col in lab5a:
        
        ipfile.append(col[0])

for x in range(0, len(ipfile)):

    iplist = ipfile[x].split('.')
    ip = int(iplist[0])
    if ip >= 128 and ip <= 191:
        ipclass = "B"
        print("\nClass B address: {0}".format(ipfile[x]))
        print("Subnet Mask 255.255.0.0\n")
